# awesome-harness-engineering — Harness 엔지니어링 리소스 총정리

- **출처:** [GitHub - walkinglabs/awesome-harness-engineering](https://github.com/walkinglabs/awesome-harness-engineering)
- **GitHub 스타:** ★ 215+
- **태그:** `#Harness` `#AINativeDev` `#AwesomeList` `#AgentEngineering`

---

## 이 리포지토리가 중요한 이유

AI 코딩 에이전트의 **harness 엔지니어링** — 모델을 감싸는 scaffold(프롬프트, 도구, 검증, 컨텍스트 관리)를 어떻게 설계하는가 — 에 대한 최고 수준의 리소스를 한 곳에 모은 awesome 리스트다. 하루 만에 200+★을 넘기며 이 분야에 대한 폭발적 관심을 보여준다.

## 카테고리별 핵심 리소스

### 1. Foundations & Mental Models (기초)
- **Anthropic "Building Effective Agents"** — 가장 단순한 솔루션부터 시작, 필요할 때만 복잡도 추가
- **Anthropic "Harness design for long-running apps"** — Planner-Generator-Evaluator 3-agent 구조
- **LangChain "Frameworks, Runtimes, Harnesses"** — 프레임워크/런타임/harness의 명확한 구분

### 2. Context Engineering (컨텍스트 엔지니어링)
- **Anthropic "Effective context engineering"** — 컨텍스트 윈도우를 작업 메모리 예산으로 관리
- **Manus "Context Engineering Lessons"** — KV-cache 지역성, 도구 마스킹, 파일시스템 메모리
- **Martin Fowler "Context Engineering for Coding Agents"** — 코딩 에이전트가 기반을 유지하도록 환경 설계
- **HumanLayer "Context-Efficient Backpressure"** — 에이전트가 노이즈에 컨텍스트를 낭비하지 않도록

### 3. Constraints & Safe Autonomy (제약과 안전)
- **Anthropic "Claude Code sandboxing"** — 통제력을 잃지 않으면서 승인 마찰 줄이기
- **Anthropic "Writing tools for agents"** — 모델이 올바르고 안전하게 호출할 수 있는 도구 인터페이스
- **Anthropic "Claude Code best practices"** — 리포 구조, 체크포인트, 검증, 위임
- **HumanLayer "12 Factor Agents"** — 프로덕션 에이전트의 운영 원칙

### 4. Specs & Workflow Design (스펙과 워크플로우)
- **AGENTS.md** — 리포 로컬 에이전트 지시서 오픈 포맷
- **GitHub Spec Kit** — 스펙 기반 개발 도구 (에이전트가 명확한 스펙에 맞춰 실행)
- **Martin Fowler "Understanding Spec-Driven-Development"** — 강한 스펙이 AI 개발을 더 신뢰할 수 있게 만드는 이유
- **12-Factor AgentOps** — 컨텍스트 규율, 검증, 재현 가능한 워크플로우

### 5. Evals & Observability (평가와 관측성)
- **OpenAI "Testing Agent Skills Systematically"** — 에이전트 trace → 반복 가능한 eval
- **Anthropic "Demystifying Evals"** — 성공/실패 경로가 다양한 에이전트를 어떻게 측정하는가
- **Anthropic "Infrastructure noise in evals"** — 런타임 구성이 벤치마크 점수를 리더보드 갭 이상으로 움직일 수 있음
- **LangChain "Evaluating Deep Agents"** — 단일 스텝, 전체 실행, 멀티턴 eval 설계

### 6. Benchmarks (벤치마크)
- **SWE-bench Verified** — 실제 GitHub 이슈와 테스트 기반, harness 선택이 가장 잘 드러남
- **Terminal-Bench** — 터미널 네이티브 에이전트 벤치마크
- **HAL (Princeton)** — 신뢰성, 비용, 범용성을 함께 측정

### 7. Runtimes & Reference Implementations
- **Claude Agent SDK** — Anthropic의 프로덕션 에이전트 SDK
- **SWE-agent** — harness, 프롬프트, 도구, 환경 설계를 직접 검사할 수 있는 연구용 에이전트
- **deepagents (LangChain)** — 더 깊고 오래 실행되는 에이전트를 위한 미들웨어 + harness 패턴

## Soo에게 의미 있는 이유

이 리포지토리는 **AInD 컨설팅의 교과서**와 같다. Harness 엔지니어링의 모든 측면 — 기초 이론부터 컨텍스트 관리, 안전성, 스펙 설계, 평가, 벤치마크, 구현 레퍼런스까지 — 을 최고 수준의 원문 링크로 정리해놓았다.

특히 **Foundations, Context Engineering, Specs 섹션**은 컨설팅 TF의 필독 자료다. "AI 에이전트를 어떻게 잘 운영하는가"에 대한 업계 최전선의 답변이 모두 여기에 있다.
