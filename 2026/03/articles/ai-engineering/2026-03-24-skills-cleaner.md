# skills-cleaner — Claude Code 스킬 중복 감지 및 정리 플러그인

- **출처:** [github.com/amebahead/skills-cleaner](https://github.com/amebahead/skills-cleaner)
- **제작자:** amebahead (GeekNews Show GN)
- **GeekNews 토론:** [news.hada.io](https://news.hada.io/topic?id=27762) · ⬆️ 8
- **라이선스:** MIT
- **태그:** `#ClaudeCode` `#Skills` `#PluginManagement` `#DuplicateDetection` `#HarnessOps`

---

## 1. 해결하려는 문제 — 스킬이 쌓이면 벌어지는 일

Claude Code의 스킬과 플러그인 생태계가 폭발적으로 성장하면서(오늘만 해도 everything-claude-code, gstack, Impeccable, obsidian-skills, awesome-claude-code가 동시 트렌딩), 사용자의 `.claude/` 디렉토리에는 수십 개의 스킬이 쌓이게 된다. 이것이 만드는 문제는 세 가지이다:

**첫째, 컨텍스트 윈도우 소모.** 모든 활성 스킬은 에이전트의 시스템 프롬프트에 포함되어 컨텍스트 윈도우를 차지한다. 스킬이 20개면 수천 토큰이 스킬 설명에만 소비되며, 이는 실제 태스크에 사용할 수 있는 공간을 줄인다. 컨텍스트가 꽉 차면 초기 지시사항이 밀려나면서 에이전트 행동의 품질이 저하된다.

**둘째, 스킬 간 충돌.** 비슷한 기능의 스킬이 서로 다른 지시를 포함할 수 있다. 예를 들어 스킬 A가 "항상 TypeScript를 사용하라"고 하고, 스킬 B가 "프로젝트에 맞는 언어를 선택하라"고 하면, 에이전트의 행동이 비결정적(non-deterministic)이 된다. 어떤 세션에서는 A의 지시를 따르고, 다른 세션에서는 B를 따르는 불일치가 발생한다.

**셋째, "어떤 스킬이 있는지 모른다" 문제.** 여러 플러그인을 설치하다 보면 어떤 스킬이 어디서 왔는지, 현재 활성화된 스킬이 무엇인지 파악하기 어려워진다.

skills-cleaner는 이 세 가지 문제를 **3개의 슬래시 커맨드**로 해결한다.

---

## 2. 세 가지 커맨드

### `/list-skills` — 스킬 인벤토리

설치된 모든 스킬을 **출처별로 그룹화**하여 보여준다:

```
Installed Skills (16 total)

personal (2 skills)
  my-custom-skill    Custom automation tool
  my-helper          Helper for daily tasks

superpowers (10 skills)
  brainstorming      Explore intent and requirements
  writing-plans      Create implementation plans from specs
  ...

gstack (8 skills)
  office-hours       YC-style product rethinking
  review             Staff engineer code review
  ...
```

출처가 **personal**(사용자가 직접 추가)인지, **plugin**(마켓플레이스에서 설치)인지를 구분하여 표시한다. 이것만으로도 "내가 지금 어떤 스킬을 가지고 있는지"의 가시성이 확보된다.

### `/search-skills` — 스킬 검색

이름으로 스킬을 검색하고 파일 경로까지 보여준다:

```
Search: "debug" → 2 results

  debugging
    Source: superpowers (plugin)
    Path: ~/.claude/plugins/cache/superpowers/skills/systematic-debugging/SKILL.md

  debug-helper
    Source: personal
    Path: ~/.claude/skills/debug-helper/SKILL.md
```

같은 기능의 스킬이 여러 곳에 있는지 빠르게 확인할 수 있다.

### `/clean-skills` — 핵심 기능: 유사도 분석 및 정리

이것이 skills-cleaner의 핵심이다. **5단계 파이프라인**으로 작동한다:

---

## 3. `/clean-skills`의 5단계 파이프라인 — 기술적 깊이

### Stage 1: 수집 (Collect)

두 경로에서 SKILL.md 파일을 수집한다:
- `~/.claude/skills/**/SKILL.md` — 개인 스킬
- `~/.claude/plugins/cache/**/SKILL.md` — 플러그인 스킬

각 스킬에서 이름, 설명, 전체 본문, 파일 경로, 출처(personal/plugin)를 추출한다.

### Stage 2: 병렬 비교 (Parallel Compare)

**이것이 기술적으로 가장 흥미로운 부분이다.** N개의 스킬에서 N*(N-1)/2 쌍을 생성하고, **각 쌍을 별도의 서브에이전트에서 병렬로 비교**한다. 16개 스킬이면 120쌍, 각각 독립적으로 분석된다.

비교는 4차원으로 이루어진다:
1. **목적 유사성(Purpose)** — 같은 문제를 해결하는가?
2. **트리거 유사성(Trigger)** — 같은 상황에서 호출되는가?
3. **프로세스 유사성(Process)** — 워크플로가 겹치는가?
4. **출력 유사성(Output)** — 같은 유형의 결과를 생성하는가?

**중요한 판단 규칙:**
- 같은 주제를 다루지만 역할이 다르면(예: 요청 vs 수신) → **보완적**이지, 중복이 아니다 → 낮은 점수
- 한 스킬이 다른 스킬의 원칙을 빌려왔지만 다른 도메인에 적용하면 → 낮은 점수
- 워크플로의 다른 단계에 있는 스킬들은 → 중복이 아니다

이 규칙이 있기 때문에 단순한 텍스트 유사도가 아닌 **의미적 유사도(semantic similarity)**를 평가할 수 있다.

배치 전략: 30쌍 이하면 모두 병렬 실행, 초과하면 10개씩 배치.

### Stage 3: 리포트 (Report)

**70% 이상의 유사도를 가진 쌍만** 리포트에 포함한다. 시각적 유사도 바와 등급 시스템:

```
Skills Similarity Report
14 skills · 91 pairs · Threshold: 70%

Found 3 similar pairs:

#1  executing-plans  VS  subagent-driven-development
    ██████████████████░░ 85%  ·  plugin VS plugin

    Overlap
      · Both execute implementation plans via subagents
      · Both include a code review stage

    Diff
      · executing-plans: runs in a separate session
      · subagent-driven-development: runs in the current session

    → Choose one based on whether session isolation is needed
```

등급 체계:
- 🔴 **90%+** — 제거 후보 (거의 동일)
- 🟡 **70-89%** — 검토 권장 (기능 겹침)
- 🟢 **70% 미만** — 고유 (리포트에서 제외)

### Stage 4: 대화형 선택 (Interactive Select)

유사도 높은 순서대로 **한 쌍씩** 보여주며 결정을 묻는다:

```
#1  executing-plans  VS  subagent-driven-development  (85%)

    a) Remove executing-plans
    b) Remove subagent-driven-development
    c) Keep both (skip)
```

**자동 건너뛰기 규칙:** 스킬 A 제거를 선택한 후, A가 포함된 후속 쌍은 자동으로 건너뛴다.

모든 쌍 검토 후 **최종 확인 게이트:**
```
To be removed: executing-plans, my-redundant-skill
Proceed? (y/n)
```

### Stage 5: 삭제 실행 (Execute)

확인 후 실제 삭제를 수행하고, 각각의 결과를 보고한다:

```
Removing executing-plans...
  ✅ Deleted: ~/.claude/skills/executing-plans/

Removing old-brainstorm...
  ✅ Deleted: ~/.claude/plugins/cache/superpowers/.../old-brainstorm/
  ⚠️  May be restored on plugin update. To prevent: claude plugins remove superpowers
```

**개인 스킬**은 직접 삭제하지만, **플러그인 스킬**은 삭제 후 "플러그인 업데이트 시 복원될 수 있다"는 경고와 영구 제거 방법을 안내한다.

---

## 4. 설계의 탁월한 점들

### "Common Mistakes" 테이블

SKILL.md에 **에이전트가 흔히 저지르는 실수와 올바른 접근법**을 명시적으로 정리한 테이블이 있다. 이것은 스킬 작성의 모범 사례를 보여준다:

| 흔한 실수 | 올바른 접근 |
|---|---|
| 단일 에이전트에서 순차 비교 | 항상 병렬 서브에이전트 사용 |
| 70% 미만 쌍을 리포트에 포함 | 70% 이상만 포함 |
| 안내만 하고 실제 삭제 안 함 | 확인 후 `rm -rf` 실행 |
| 최종 확인 없이 삭제 | 반드시 확인 게이트 필요 |
| 삭제 성공 여부 미검증 | `ls`로 삭제 후 검증 |
| 보완적 스킬을 중복으로 판단 | 역할이 다르면 낮은 점수 |
| 하나의 삭제 실패로 전체 중단 | 에러 표시 후 다음으로 계속 |

이 "Common Mistakes" 패턴은 **스킬을 설계할 때 에이전트의 실패 모드를 미리 예측하고 방지하는 방법**으로, 다른 스킬 개발에도 적용할 수 있는 기법이다.

### 서브에이전트 병렬 처리

120쌍을 순차적으로 비교하면 시간이 매우 오래 걸리지만, **각 쌍을 독립적 서브에이전트로 병렬 실행**하면 극적으로 빨라진다. 이 패턴은 Claude Code의 서브에이전트 기능을 활용한 것으로, **"분할 가능한 작업은 병렬화하라"**는 에이전트 설계 원칙의 구체적 적용이다.

### 안전한 삭제 프로토콜

삭제 프로세스가 다층적 안전 장치를 갖추고 있다:
1. 리포트로 먼저 확인 (정보 제공만, 행동 없음)
2. 한 쌍씩 대화형 결정 (사용자 제어)
3. 최종 확인 게이트 (마지막 방어선)
4. 삭제 후 검증 (`ls`로 확인)
5. 실패 시 계속 진행 (하나의 실패가 전체를 막지 않음)

이것은 gstack의 `/careful`, `/freeze`, `/guard`와 같은 **"에이전트 안전 장치"** 설계 패턴과 일맥상통한다.

---

## 5. 더 큰 맥락 — "메타 도구"의 필요성

skills-cleaner는 **"도구를 관리하는 도구(meta-tool)"**의 카테고리에 속한다. 스킬 생태계가 성장하면서, 스킬 자체를 관리하는 도구의 필요성이 급증하고 있다. 오늘 트렌딩된 프로젝트들과의 관계를 보면:

- **everything-claude-code** (+4,453/일) → 스킬을 만든다
- **gstack** → 28개의 전문 스킬을 제공한다
- **Impeccable** → 20개의 디자인 스킬을 제공한다
- **obsidian-skills** → Obsidian 전용 스킬을 제공한다
- **awesome-claude-code** → 스킬 목록을 큐레이션한다
- **skills-cleaner** → **이 모든 스킬을 설치한 후의 관리 문제를 해결한다**

이것은 소프트웨어 생태계의 전형적 성숙 패턴이다. npm이 폭발적으로 성장한 후 `npm audit`, `depcheck`, `npm-check-updates` 같은 메타 도구가 등장한 것과 같은 맥락이다. Claude Code 스킬 생태계도 같은 경로를 밟고 있으며, skills-cleaner는 그 초기 사례이다.

앞으로 예상되는 메타 도구의 발전 방향:
- **스킬 충돌 감지** — 유사도를 넘어, 상충되는 지시를 구체적으로 식별
- **스킬 성능 벤치마크** — 특정 스킬이 에이전트 성능에 미치는 영향 측정
- **스킬 의존성 관리** — 스킬 간 의존 관계 추적 (A 스킬이 B 스킬의 출력을 필요로 하는 경우)
- **컨텍스트 윈도우 예산 관리** — 각 스킬이 차지하는 토큰 수를 측정하고 예산 내에서 관리

---

## 6. Soo에게 의미 있는 이유

**첫째, 기업에 에이전트를 대규모 배포할 때 반드시 필요한 운영 도구.** 한 명의 개발자가 5-10개 스킬을 관리하는 것은 수동으로 가능하지만, 50명의 팀이 각각 다른 스킬을 설치하고 운용하는 기업 환경에서는 스킬 관리의 자동화가 필수적이다. skills-cleaner의 패턴(인벤토리 → 유사도 분석 → 대화형 정리)은 기업 에이전트 운용 가이드라인에 포함될 수 있다.

**둘째, "Common Mistakes" 테이블 패턴.** 스킬을 설계할 때 에이전트의 실패 모드를 미리 정의하는 이 패턴은 AInD 컨설팅에서 고객 기업의 맞춤 스킬을 만들 때 직접 적용 가능한 기법이다. 에이전트에게 "하지 마라"를 명시하는 것이 "하라"보다 종종 더 효과적이라는 것을 보여준다.

**셋째, 에이전트 운용 성숙도 모델의 한 단계.** 에이전트 도입의 성숙도를 단계별로 정의할 수 있다: Level 1(도구 사용) → Level 2(스킬 설치) → Level 3(스킬 관리/최적화) → Level 4(자체 스킬 개발). skills-cleaner는 Level 3의 구체적 도구이며, 이 성숙도 모델 자체가 컨설팅 프레임워크가 될 수 있다.
