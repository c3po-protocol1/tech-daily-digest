# Effective Harnesses for Long-Running Agents

- **출처:** [Anthropic](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- **저자:** Justin Young
- **날짜:** 2025년 11월 26일
- **코드:** [quickstart 리포](https://github.com/anthropics/claude-quickstarts/tree/main/autonomous-coding)
- **태그:** `#Anthropic` `#LongRunning` `#ContextWindow` `#Handoff` `#ClaudeAgentSDK`

---

## 핵심 문제

장기 실행 에이전트의 근본 문제: **각 새 세션이 이전에 일어난 일의 기억 없이 시작**된다. 교대 근무하는 엔지니어가 매 교대마다 기억을 잃는 것과 같다. 컨텍스트 윈도우는 유한하고, 대부분의 복잡한 프로젝트는 단일 윈도우 안에서 완료할 수 없으므로, 에이전트에게는 코딩 세션 사이의 격차를 메우는 방법이 필요하다.

## Compaction만으로는 부족한 이유

Claude Agent SDK는 compaction(컨텍스트 소진 없이 작업할 수 있도록 이전 대화를 압축하는 기능)을 포함하고 있다. 이론적으로는 에이전트가 임의로 긴 시간 동안 유용한 작업을 할 수 있어야 한다.

**그러나 실제로는:** Opus 4.5 같은 프론티어 모델을 Claude Agent SDK에서 여러 컨텍스트 윈도우에 걸쳐 루프로 실행해도, "claude.ai 클론을 만들어라" 같은 고수준 프롬프트만으로는 프로덕션 품질 웹앱을 만들지 못했다.

## 두 가지 실패 패턴 (구체적 사례)

### 실패 1: One-shotting (한 번에 다 하려 함)

에이전트가 전체 앱을 한 세션에 구현하려 시도한다. 이로 인해:
- 구현 중간에 컨텍스트 소진 → 기능이 반쯤 구현되고 문서화되지 않은 채 세션 종료
- 다음 세션이 무슨 일이 일어났는지 추측해야 함
- 기본적인 앱을 다시 작동시키느라 **상당한 시간 낭비**
- compaction이 있어도 발생함 — compaction이 항상 완벽하게 명확한 지시를 다음 에이전트에 전달하지는 않음

### 실패 2: 조기 완료 선언

프로젝트 후반부에 자주 발생. 몇 가지 기능이 이미 만들어진 후, 이후 에이전트 인스턴스가 주변을 둘러보고, 진전이 있었음을 확인하고, **"일이 끝났다"고 선언**한다.

## 해결책: 2-에이전트 구조

문제를 두 부분으로 분해:
1. 주어진 프롬프트가 요구하는 **모든** 기능의 기반을 놓는 초기 환경 설정
2. 각 에이전트가 목표를 향해 **점진적 진전**을 하면서, 세션 끝에 환경을 **깨끗한 상태**로 남기는 것

### Initializer Agent (첫 세션에서 1회)

특수한 프롬프트로 모델에게 초기 환경 설정을 요청:

**1. Feature List 파일 (JSON 형식):**

에이전트의 one-shotting과 조기 완료 선언 문제를 해결하기 위해, 사용자의 초기 프롬프트를 확장한 **포괄적인 기능 요구사항 파일**을 작성하도록 프롬프트.

claude.ai 클론 예시에서는 **200개 이상의 기능**, 예: "사용자가 새 채팅을 열고, 쿼리를 입력하고, 엔터를 누르고, AI 응답을 볼 수 있다."

모든 기능이 처음에 `"passes": false`로 표시되어, 이후 코딩 에이전트가 **완전한 기능이 어떤 모습인지 명확한 윤곽**을 갖게 됨.

```json
{
  "category": "functional",
  "description": "New chat button creates a fresh conversation",
  "steps": [
    "Navigate to main interface",
    "Click the 'New Chat' button",
    "Verify a new conversation is created",
    "Check that chat area shows welcome state",
    "Verify conversation appears in sidebar"
  ],
  "passes": false
}
```

**왜 JSON인가:** 에이전트가 Markdown 파일에 비해 JSON 파일을 **부적절하게 변경하거나 덮어쓸 가능성이 적음**. 코딩 에이전트에게 `passes` 필드만 변경하도록 프롬프트하고, "테스트를 제거하거나 편집하는 것은 용납할 수 없다. 이는 기능 누락이나 버그로 이어질 수 있다"와 같은 강한 어조의 지시 사용.

**2. init.sh 스크립트:**

개발 서버를 실행하고 기본적인 end-to-end 테스트를 수행할 수 있는 초기화 스크립트.

**3. claude-progress.txt 파일:**

에이전트가 한 일의 로그를 기록하는 진행 상황 파일.

**4. 초기 git 커밋:**

어떤 파일이 추가되었는지 보여주는 초기 커밋.

### Coding Agent (매 세션)

매 후속 세션에서 에이전트에게 **점진적 진전**을 만들고 구조화된 업데이트를 남기도록 요청.

**세션 시작 시 표준 절차:**
1. `pwd` 실행하여 작업 디렉토리 확인
2. git 로그와 진행 파일을 읽어 최근 작업 파악
3. 기능 목록 파일을 읽고 **가장 우선순위가 높은 미완성 기능** 선택

**핵심: 한 번에 하나의 기능만 작업 (Incremental Progress)**

이 점진적 접근이 에이전트의 "한 번에 너무 많이 하려는" 경향을 해결하는 데 **결정적**이었다.

**세션 종료 시 깨끗한 상태 유지:**
- 설명적 커밋 메시지로 git에 진행 상황 커밋
- 진행 파일에 작업 요약 작성
- 코드가 **메인 브랜치에 머지해도 될 수준**: 주요 버그 없음, 코드가 정돈되고 문서화됨

**git의 이중 역할:** 진행 기록 + 나쁜 코드 변경을 되돌리고 작동 상태를 복구하는 수단

### 자기 검증(Self-Verification)의 중요성

또 하나의 주요 실패 모드: Claude가 적절한 테스트 없이 기능을 완료로 표시하는 경향.

**명시적 프롬프팅 없이:** Claude가 코드를 변경하고, 유닛 테스트나 `curl` 명령으로 테스트하지만, 기능이 **end-to-end로 작동하는지 인식하지 못함**.

**해결:** 브라우저 자동화 도구(Puppeteer MCP)를 제공하고 **인간 사용자처럼 모든 테스트를 수행**하도록 명시적으로 프롬프트.

> "Claude에게 이러한 종류의 테스트 도구를 제공하는 것이 성능을 극적으로 개선했다. 에이전트가 코드만으로는 명확하지 않은 버그를 식별하고 수정할 수 있었기 때문이다."

**남은 한계:** Claude의 시각 능력과 브라우저 자동화 도구의 제한. 예: Claude가 Puppeteer MCP를 통해 브라우저 네이티브 alert 모달을 볼 수 없음 → 이러한 모달에 의존하는 기능이 더 버그가 많은 경향.

### 세션 시작의 실제 모습

```
[Assistant] 프로젝트의 현재 상태를 파악하겠습니다.
[Tool Use: pwd, git log, read progress file]
[Assistant] init.sh 스크립트가 있는지 확인하여 서버를 재시작하겠습니다.
[Tool Use: run init.sh, start dev server]
[Assistant] 애플리케이션으로 이동하여 기본 기능이 여전히 작동하는지 확인하겠습니다.
[Tool Use: Puppeteer - navigate, send message, check response]
[Assistant] 기본 기능이 잘 작동하고 있음을 확인했습니다.
채팅, 테마 전환, 대화 로딩, 에러 처리가 정상 동작합니다.
이제 tests.json 파일을 검토하여 다음에 구현할 것을 파악하겠습니다.
```

이 접근이 중요한 이유: 에이전트가 새 기능 구현을 시작하기 전에 **앱이 깨진 상태인지 먼저 확인**. 깨진 상태에서 새 기능 구현을 시작하면 문제를 악화시킬 가능성이 높음.

## 실패 모드와 해결책 요약표

| 문제 | Initializer 행동 | Coding Agent 행동 |
|------|-----------------|-------------------|
| 프로젝트 조기 완료 선언 | feature list 파일 설정 (JSON, 모든 기능 `passes: false`) | 세션 시작 시 feature list 읽기. 단일 기능 선택하여 작업 |
| 환경을 버그/미문서화 상태로 방치 | 초기 git repo + progress notes 파일 작성 | 세션 시작 시 progress 파일 + git log 읽기 + 기본 테스트 실행. 세션 종료 시 git commit + progress 업데이트 |
| 기능을 조기 완료 표시 | feature list 파일 설정 | 모든 기능 자기 검증. 신중한 테스트 후에만 `passes: true` 표시 |
| 앱 실행 방법 파악에 시간 소비 | `init.sh` 스크립트 작성 | 세션 시작 시 `init.sh` 읽기 |

## 미래 작업

이 연구는 장기 실행 에이전트 harness의 가능한 해결책 중 하나를 보여주지만, 열린 질문이 남아있다:

1. **단일 범용 코딩 에이전트 vs 멀티 에이전트 아키텍처:** 테스트 에이전트, QA 에이전트, 코드 정리 에이전트 같은 특화 에이전트가 소프트웨어 개발 생명주기의 하위 작업을 더 잘 수행할 수 있을까?
2. **다른 분야로의 일반화:** 이 데모는 풀스택 웹앱 개발에 최적화됨. 과학 연구나 금융 모델링 같은 다른 장기 에이전트 작업에도 적용 가능한가?

→ 이 질문들은 다음 글(harness-design-long-running-apps)에서 **Planner-Generator-Evaluator 3-에이전트 구조**로 답변됨.

## Soo에게 의미 있는 이유

이 글은 **장기 에이전트 harness 설계의 원점**이다. 이후 모든 harness 논의의 기초가 되는 개념들 — feature list, incremental progress, 핸드오프 아티팩트, 자기 검증 — 이 여기서 시작됐다.

**우리 워크플로우와의 직접적 연관:**
- R2가 Claude Code로 Holocron을 구현할 때 **정확히 이 패턴**을 따르고 있다
- Feature List = 우리의 SPEC.md (F1~F10)
- Incremental Progress = 한 번에 하나의 Feature spec만 구현
- Progress File = git commit + PR
- Self-verification = `go test ./...` + `go build`

AInD 컨설팅에서 "에이전트가 장기 프로젝트를 어떻게 수행하는가"의 **가장 기본적이면서 가장 중요한 레퍼런스**.
