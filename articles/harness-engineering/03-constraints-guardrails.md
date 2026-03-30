# 3. Constraints, Guardrails & Safe Autonomy — 제약과 안전한 자율성

> 에이전트에게 자유를 주되 통제력을 잃지 않는 방법.

---

## 3.1 Anthropic — Beyond Permission Prompts: Making Claude Code More Secure and Autonomous

**출처:** [anthropic.com](https://www.anthropic.com/engineering/claude-code-sandboxing)

### 핵심 내용

매번 "이 명령을 실행해도 됩니까?" 묻는 것은 생산성을 죽인다. **더 나은 샌드박싱과 정책 설계**로 승인 마찰을 줄이면서 통제력을 유지하는 방법.

**접근법:**
- **화이트리스트 기반 허용** — 안전하다고 알려진 명령은 자동 허용
- **샌드박스 격리** — 파일시스템, 네트워크 접근을 제한된 환경에서 실행
- **정책 기반 자동화** — "읽기는 허용, 쓰기는 특정 디렉토리만, 삭제는 금지" 같은 선언적 정책
- 목표: **"안전할 때 자동으로, 위험할 때만 물어보기"**

### 핵심 교훈
> "보안과 자율성은 트레이드오프가 아니다. 정책이 잘 설계되면 둘 다 높일 수 있다."

---

## 3.2 Anthropic — Code Execution with MCP: Building More Efficient Agents

**출처:** [anthropic.com](https://www.anthropic.com/engineering/code-execution-with-mcp)

### 핵심 내용

에이전트에게 코드 실행 능력을 부여하되, **명시적이고 검사 가능한 도구 경계**를 통해 통제하는 방법.

**MCP(Model Context Protocol)를 통한 실행:**
- 에이전트가 직접 `eval()`하지 않고, MCP 서버를 통해 격리된 환경에서 실행
- 실행 요청과 결과가 모두 **감사 가능(auditable)**
- 도구 호출 로그로 에이전트가 무엇을 실행했는지 추적 가능

**설계 원칙:**
- 실행 환경은 에이전트의 메인 환경과 **격리**
- 타임아웃, 메모리 제한, 네트워크 차단 등 리소스 제한
- 결과를 에이전트에 반환하기 전 **위생 처리(sanitization)**

### 핵심 교훈
> "에이전트에게 실행 능력을 줄 때, '할 수 있게'만이 아니라 '어떻게 관찰하고 제한할 것인가'를 함께 설계하라."

---

## 3.3 Anthropic — Writing Effective Tools for Agents

**출처:** [anthropic.com](https://www.anthropic.com/engineering/writing-tools-for-agents)

### 핵심 내용

에이전트가 **올바르게, 안전하게** 호출할 수 있는 도구 인터페이스 설계 가이드.

**좋은 도구의 특징:**
- **명확한 설명** — 도구가 무엇을 하는지, 언제 사용해야 하는지, 어떤 입력이 필요한지
- **예측 가능한 출력** — 같은 입력에 같은 형식의 출력
- **유용한 에러** — 모델이 에러를 읽고 다음 행동을 결정할 수 있어야 함
- **적절한 범위** — 하나의 도구가 너무 많은 일을 하면 안 됨 (SRP)

**나쁜 도구의 징후:**
- 에이전트가 같은 도구를 잘못된 파라미터로 반복 호출
- 도구 설명이 모호하여 에이전트가 사용 시점을 판단하지 못함
- 에러 메시지가 "실패했습니다"만 반환 → 에이전트가 대응 불가

### 핵심 교훈
> "도구 설계는 API 설계와 같다. 사용자가 모델이라는 점만 다를 뿐, 명확성과 예측 가능성의 원칙은 동일하다."

---

## 3.4 Thoughtworks — Assessing Internal Quality While Coding with an Agent

**출처:** [martinfowler.com](https://martinfowler.com/articles/exploring-gen-ai/ccmenu-quality.html)

### 핵심 내용

품질 검사를 사후(after-the-fact)가 아닌 **루프 안(in-the-loop)**으로 이동시키는 방법.

**기존 방식의 문제:**
- 에이전트가 코드 생성 → 인간이 나중에 리뷰 → 이미 많이 잘못됨
- 피드백 지연이 클수록 수정 비용 증가

**루프 내 품질 검사:**
- 코드 생성 직후 **자동 린트, 테스트, 타입 체크** 실행
- 결과를 에이전트에 즉시 피드백 → 에이전트가 자체 수정
- 인간 리뷰는 **자동 검사를 통과한 코드만** 대상

### 핵심 교훈
> "에이전트가 생성하는 코드의 품질을 높이는 가장 효과적인 방법은 빠른 피드백 루프다."

---

## 3.5 Thoughtworks — Anchoring AI to a Reference Application

**출처:** [martinfowler.com](https://martinfowler.com/articles/exploring-gen-ai/anchoring-to-reference.html)

### 핵심 내용

에이전트를 **구체적인 참조 구현(reference application)**에 앵커링하여 일관된 출력을 보장하는 방법.

**참조 앱의 역할:**
- "이렇게 만들어라"가 아닌 **"이 앱처럼 만들어라"**
- 추상적 규칙보다 **구체적 예시**가 에이전트에게 더 효과적
- 아키텍처 패턴, 코딩 스타일, 파일 구조를 실물로 보여줌

**실용 방법:**
- 프로젝트 내 **"골든 모듈"**을 지정 — 다른 모듈의 참조가 되는 잘 만든 예시
- CLAUDE.md에 "src/modules/auth를 참조하여 같은 패턴으로 구현하라"고 명시
- 새 기능 추가 시 에이전트가 참조 모듈의 구조를 자동으로 따름

### 핵심 교훈
> "규칙 100줄보다 잘 만든 예시 1개가 에이전트를 더 효과적으로 제약한다."

---

## 3.6 Thoughtworks — Humans and Agents in Software Engineering Loops

**출처:** [martinfowler.com](https://martinfowler.com/articles/exploring-gen-ai/humans-and-agents.html)

### 핵심 내용

인간이 **harness를 강화**해야 할 지점과 에이전트에게 위임해야 할 지점의 멘탈 모델.

**인간의 역할:**
- **아키텍처 결정** — 전체 구조, 기술 선택, 트레이드오프 판단
- **품질 기준 설정** — 무엇이 "좋은 코드"인지 정의
- **예외 처리** — 에이전트가 막힌 상황에서 방향 제시
- **Harness 개선** — 에이전트가 실패하는 패턴을 관찰하고 harness 수정

**에이전트의 역할:**
- **구현** — 정의된 패턴에 따른 코드 생성
- **반복 작업** — 보일러플레이트, 테스트 작성, 리팩토링
- **검증** — 빌드, 테스트, 린트 실행
- **탐색** — 관련 코드 검색, 문서 참조

### 핵심 교훈
> "인간은 harness를 설계하고, 에이전트는 harness 안에서 실행한다. 매 아티팩트를 마이크로매니징하는 것이 아니다."

---

## 3.7 Anthropic — Claude Code: Best Practices for Agentic Coding

**출처:** [anthropic.com](https://www.anthropic.com/engineering/claude-code-best-practices)

### 핵심 내용

Anthropic의 Claude Code 실전 베스트 프랙티스.

**리포 구조:**
- CLAUDE.md를 프로젝트 루트에 배치
- 디렉토리별 추가 지시서 가능 (e.g., `src/api/CLAUDE.md`)

**체크포인트:**
- 주기적으로 git commit → 문제 발생 시 롤백 가능
- 에이전트에게 "의미 있는 단위로 커밋하라"고 지시

**검증:**
- 코드 작성 후 반드시 빌드 + 테스트 실행
- 에이전트가 "완료했습니다" 선언 전 검증 강제

**위임:**
- 큰 작업을 작은 단위로 분해하여 지시
- "auth 모듈을 구현하라"보다 "로그인 엔드포인트를 구현하라. auth/login.ts에 작성하라"

### 핵심 교훈
> "에이전트에게 명확한 범위, 구체적 위치, 검증 수단을 함께 제공하라."
