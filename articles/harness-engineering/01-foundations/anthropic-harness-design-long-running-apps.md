# Harness Design for Long-Running Application Development

- **출처:** [Anthropic Engineering](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- **저자:** Prithvi Rajasekaran (Anthropic)
- **날짜:** 2026-03-30
- **태그:** `#Harness` `#MultiAgent` `#ClaudeCode` `#AINativeDev` `#Anthropic`

---

## 핵심 아이디어

GAN(Generative Adversarial Network)에서 영감을 받은 **멀티 에이전트 구조 (Planner → Generator → Evaluator)**로 수 시간에 걸친 자율 코딩 세션에서 완성도 높은 풀스택 앱을 만든다.

---

## 1. Naive 접근의 한계 — 두 가지 실패 모드

### 실패 모드 1: Context Coherence 상실
- 컨텍스트 윈도우가 채워질수록 모델이 일관성을 잃음
- **"Context Anxiety"** — 모델이 컨텍스트 한계에 가까워졌다고 판단하면 작업을 조기에 마무리하려 함
- **해결:** Context Reset — 컨텍스트를 완전히 초기화하고 새 에이전트를 시작, 구조화된 핸드오프로 이전 상태 전달
- Compaction(요약 유지)과 다름 — compaction은 같은 에이전트가 계속하므로 anxiety가 지속됨

### 실패 모드 2: Self-Evaluation 실패
- 에이전트가 자기가 만든 결과물을 평가하면 **항상 긍정적으로 평가** — 명백히 별로인 결과물도 "좋다"고 함
- 특히 디자인 같은 주관적 작업에서 심각
- **해결:** Generator와 Evaluator를 분리 — 별도 에이전트가 평가하면 비판적 튜닝이 훨씬 쉬워짐

---

## 2. 프론트엔드 디자인 — 주관적 품질을 점수화하기

**핵심 통찰:** "이 디자인이 아름다운가?"는 일관적으로 답하기 어렵지만, **"우리의 디자인 원칙을 따르는가?"**는 구체적으로 채점 가능

### 4가지 채점 기준

1. **Coherence** — 색상, 타이포, 레이아웃이 하나의 분위기와 정체성을 만들어내는가
2. **Originality** — 템플릿/기본값이 아닌 의도적인 창의적 결정이 있는가 (보라색 그라디언트 + 흰 카드 = AI 슬롭의 전형적 징후)
3. **Technical Execution** — 타이포 계층, 간격 일관성, 색상 조화, 대비율
4. **Usability** — 인터페이스가 하는 일을 이해할 수 있는가, 주요 액션을 찾을 수 있는가

**Design과 Originality에 가중치를 높게 설정** — Claude는 기본적으로 기술적 품질은 괜찮지만 디자인/독창성이 밋밋하기 때문

### GAN 루프 구조

```
Generator (프론트엔드 생성)
    ↓
Evaluator (Playwright MCP로 실제 페이지 탐색 + 점수 + 비평)
    ↓
Generator (피드백 기반 개선 or 완전히 새로운 방향 전환)
    ↓
5~15회 반복 (한 번에 최대 4시간)
```

**인상적인 사례:** 네덜란드 미술관 웹사이트 → 10번째 반복에서 2D 레이아웃을 완전히 버리고 **CSS 원근법으로 3D 갤러리 공간**을 구현 — 에이전트가 스스로 창의적 도약을 한 것

---

## 3. 풀스택 코딩으로 확장 — 3-Agent Architecture

### Planner Agent
- 1~4문장 프롬프트 → 전체 제품 스펙으로 확장
- 기술적 세부사항이 아닌 **제품 컨텍스트와 고수준 설계**에 집중
- 세부 기술 스펙을 잘못 잡으면 하류로 에러가 전파되므로, **결과물만 제약하고 경로는 에이전트가 결정**하도록 함
- AI 기능을 자연스럽게 제품에 포함하도록 지시

### Generator Agent
- Sprint 단위로 한 번에 하나의 기능 구현
- 스택: React + Vite + FastAPI + SQLite
- 매 Sprint 끝에 자기 평가 후 QA로 핸드오프
- Git으로 버전 관리

### Evaluator Agent (QA)
- **Playwright MCP**로 실제 앱을 클릭하며 테스트
- UI 기능, API 엔드포인트, DB 상태 검증
- Sprint Contract — Generator와 Evaluator가 작업 시작 전에 **"완료 조건"을 협상**
- 기준 미달 시 Sprint 실패 → 상세 피드백으로 재시도

### Sprint Contract 패턴

```
Generator: "이번 Sprint에서 X를 만들겠습니다. 성공 기준은 Y입니다."
Evaluator: "Z 테스트도 추가하세요. 그러면 동의합니다."
→ 합의 후 개발 시작
```

통신은 **파일 기반** — 한 에이전트가 파일을 쓰면 다른 에이전트가 읽고 응답

---

## 4. Solo vs Harness 결과 비교 (Retro Game Maker)

**프롬프트:** "Create a 2D retro game maker with level editor, sprite editor, entity behaviors, and playable test mode"

| | Solo | Harness |
|---|---|---|
| 비용 | 낮음 | **20배 이상** |
| 기능 범위 | 기본 에디터 | 16개 기능 / 10 Sprints |
| UI 품질 | 공간 낭비, 경직된 워크플로우 | 풀 뷰포트, 일관된 디자인 언어 |
| 핵심 기능 | **게임 플레이 안 됨** (broken wiring) | **게임 플레이 작동** |
| AI 통합 | 없음 | AI 스프라이트 생성, AI 레벨 디자인 |

---

## 5. Harness 반복 개선 — 단순화의 원칙

### 핵심 원칙

> "Harness의 모든 컴포넌트는 모델이 스스로 못한다는 가정을 인코딩한 것. 그 가정을 스트레스 테스트해야 한다."

### Opus 4.5 → Opus 4.6 전환 시 변경사항

- Sprint 구조 제거 가능 — 4.6은 2시간 이상 일관된 코딩 가능
- Context Reset 불필요 — 4.6은 context anxiety 해결
- Evaluator는 Sprint별이 아닌 **최종 1회 패스**로 변경
- **모델이 좋아질수록 harness는 단순해져야 하지만, 더 어려운 작업에서는 여전히 가치 있음**

### DAW 생성 결과 (Opus 4.6)

- **프롬프트:** "Build a fully featured DAW in the browser using the Web Audio API"
- 4시간, $124
- Generator가 2시간 이상 연속 코딩
- QA가 여전히 실질적 갭을 발견 (스텁 기능, 미구현 인터랙션)
- 최종 결과: 실제로 프롬프트만으로 간단한 곡 제작 가능

---

## 6. 핵심 교훈

1. **모델을 실험하고 trace를 읽어라** — 현실적 문제에서 어디가 약한지 파악
2. **복잡한 작업은 분해 + 특화 에이전트로** — Planner, Generator, Evaluator
3. **새 모델이 나오면 harness를 재검토하라** — 불필요해진 부분 제거, 새로운 가능성 추가
4. **Harness 설계 공간은 모델이 좋아져도 줄지 않는다 — 이동할 뿐** — 더 어렵고 흥미로운 문제로 초점이 옮겨감
5. **Evaluator의 독립 분리가 핵심 레버** — 자기 평가는 항상 관대함
6. **Sprint Contract 패턴** — 작업 전 완료 조건 합의가 품질을 보장
7. **"가장 단순한 해결책부터 시작하고, 필요할 때만 복잡도를 높여라"**

---

## Soo에게 의미 있는 이유

이 글은 Anthropic이 직접 작성한 harness 설계 가이드로, AInD 컨설팅의 핵심 레퍼런스다.

**직접적으로 적용 가능한 패턴들:**
- **Planner-Generator-Evaluator 3-Agent 구조** — 복잡한 프로젝트에 즉시 적용 가능
- **Sprint Contract** — 에이전트 간 "완료 조건 합의" 패턴은 품질 보장의 핵심
- **Evaluator 분리** — 자기 평가의 한계를 구조적으로 해결
- **Harness 단순화 원칙** — 새 모델 출시 시 기존 harness의 어떤 부분이 불필요해졌는지 재검토

**Holocron 프로젝트와의 연관:** Holocron이 모니터링하려는 대상이 바로 이런 멀티 에이전트 harness의 실행 과정이다. Generator가 코딩하고, Evaluator가 테스트하는 전체 흐름을 한 화면에서 보는 것이 Holocron의 비전과 정확히 일치한다.
