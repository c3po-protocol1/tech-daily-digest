# 1. Foundations — 기초 이론과 멘탈 모델

> Harness 엔지니어링의 핵심 개념과 설계 원칙을 다루는 기초 자료들.

---

## 1.1 OpenAI — Harness Engineering: Leveraging Codex in an Agent-First World

**출처:** [openai.com](https://openai.com/index/harness-engineering/)

### 핵심 내용

OpenAI가 Codex를 사용해 빈 Git 리포에서 대규모 애플리케이션을 구축한 실전 보고서다.

**엔지니어의 역할 재정의:**
- 코드를 직접 작성하는 것에서 **에이전트가 효과적으로 작업할 수 있는 환경을 설계**하는 것으로 전환
- 엔지니어는 "코더"가 아닌 **"아키텍트 + QA + 환경 설계자"**

**리포지토리 지식을 시스템 오브 레코드로:**
- AGENTS.md, 아키텍처 문서, 코딩 규칙을 리포 안에 유지
- 에이전트가 참조할 수 있는 **리포 내 지식**이 핵심
- 외부 대화나 구두 합의가 아닌 **코드와 문서가 진실의 원천**

**에이전트 가독성(Agent Legibility):**
- 인간이 읽기 좋은 코드가 아니라, **에이전트가 이해하기 좋은 구조**를 설계
- 명확한 디렉토리 구조, 일관된 네이밍, 자기 설명적 파일

**아키텍처와 취향 강제:**
- 에이전트에게 자유를 주면 일관성이 깨짐
- **아키텍처 제약을 명시적으로 설정**하여 에이전트가 범위 내에서만 작업하도록 함

**자율성의 단계:**
- Level 1: 에이전트가 단일 함수/파일 수정
- Level 2: 에이전트가 기능 단위 구현
- Level 3: 에이전트가 설계 결정까지 포함한 자율 코딩
- 단계별로 harness의 제약 수준이 달라져야 함

### 핵심 교훈
> "에이전트 시대의 엔지니어는 코드를 쓰는 사람이 아니라, 에이전트가 좋은 코드를 쓸 수 있는 환경을 만드는 사람이다."

---

## 1.2 Anthropic — Effective Harnesses for Long-Running Agents

**출처:** [anthropic.com](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

### 핵심 내용

수 시간~수 일에 걸친 장기 에이전트 작업의 핵심 문제와 해결책을 다룬 Anthropic의 원조 harness 글.

**장기 에이전트의 근본 문제:**
- 각 세션은 이전 세션의 기억이 없음 — "교대 근무하는 엔지니어가 매번 기억을 잃는 것"과 같음
- Compaction만으로는 부족 — context anxiety, 중간에 끊긴 작업, "일이 끝난 것 같다"고 선언하는 문제

**2-에이전트 해결책:**

**Initializer Agent:**
- 고수준 프롬프트를 받아 전체 작업을 분해
- Feature list 생성 — 각 기능을 독립적으로 구현 가능한 단위로
- `init.sh` 생성 — 프로젝트 스캐폴딩, 의존성, 기본 구조 설정
- 이 결과물이 **모든 후속 세션의 기반**

**Coding Agent (매 세션):**
- Feature list에서 다음 미완성 기능을 선택
- 한 세션에 한 기능만 구현 (one-feature-at-a-time)
- 세션 끝에 **자기 검증** (빌드 + 테스트 + 수동 확인)
- **핸드오프 아티팩트** 남기기 — 다음 에이전트가 이어받을 수 있도록

**핸드오프 아티팩트:**
- 완료된 기능 체크리스트
- 현재 상태 요약
- 알려진 이슈
- 다음 세션에서 해야 할 일

### 핵심 교훈
> "장기 에이전트의 핵심은 각 세션이 깨끗하게 시작하고 깨끗하게 끝나는 것이다. 핸드오프 아티팩트가 세션 간의 다리 역할을 한다."

---

## 1.3 Anthropic — Harness Design for Long-Running Application Development

**출처:** [anthropic.com](https://www.anthropic.com/engineering/harness-design-long-running-apps)

> 별도 상세 요약: [2026-03-30-harness-design-long-running-apps.md](../ai-engineering/2026-03-30-harness-design-long-running-apps.md)

### 핵심 요약
- GAN에서 영감 — **Planner → Generator → Evaluator** 3-에이전트 구조
- Self-evaluation 실패 해결: Evaluator를 분리하면 비판적 튜닝이 가능
- Sprint Contract: 작업 전 완료 조건 합의
- 모델이 좋아질수록 harness는 단순해져야 하지만, 더 어려운 작업에서는 여전히 필요

---

## 1.4 LangChain — The Anatomy of an Agent Harness

**출처:** [blog.langchain.com](https://blog.langchain.com/the-anatomy-of-an-agent-harness/)

### 핵심 내용

에이전트 = 모델 + Harness. Harness의 구성 요소를 명확히 분해한 글.

**Harness의 5가지 레이어:**
1. **Prompts** — 시스템 프롬프트, 지시서, 컨텍스트 주입
2. **Tools** — 에이전트가 사용할 수 있는 도구 인터페이스
3. **Middleware** — 입출력 가공, 로깅, 검증, 재시도
4. **Orchestration** — 멀티 에이전트 조정, 작업 분배, 핸드오프
5. **Runtime Infrastructure** — 실행 환경, 상태 관리, 영속성

**프레임워크 vs 런타임 vs Harness:**
- **프레임워크:** 일반적인 에이전트 구축 도구 (LangChain, CrewAI)
- **런타임:** 실행, 상태, 내구성 인프라 (Inngest, Temporal)
- **Harness:** 특정 작업에 맞춘 프롬프트 + 도구 + 검증 조합

### 핵심 교훈
> "Harness는 프레임워크가 아니다. 특정 문제를 해결하기 위해 모델 주변에 구성한 맞춤형 환경이다."

---

## 1.5 Thoughtworks — Harness Engineering

**출처:** [martinfowler.com](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html)

### 핵심 내용

Thoughtworks(Martin Fowler 팀)의 harness 엔지니어링 프레이밍.

**Harness 작업의 3가지 축:**
1. **Context Engineering** — 에이전트에게 올바른 정보를 올바른 시점에 제공
2. **Architectural Constraints** — 에이전트가 만들 수 있는 구조적 결정의 범위를 제한
3. **Garbage Collection (엔트로피 대응)** — 에이전트가 만든 코드의 품질 저하를 지속적으로 정리

**"엔트로피 대응"이 핵심 개념:**
- 에이전트가 코드를 생성할수록 복잡도가 증가 (엔트로피)
- 이를 적극적으로 관리하지 않으면 시스템은 빠르게 부패
- Harness에 **자동 리팩토링, 품질 게이트, 구조 검증**을 포함해야 함

### 핵심 교훈
> "Harness 엔지니어링의 절반은 에이전트를 돕는 것이고, 나머지 절반은 에이전트가 만든 엔트로피를 청소하는 것이다."

---

## 1.6 Anthropic — Building Effective Agents

**출처:** [anthropic.com](https://www.anthropic.com/engineering/building-effective-agents)

### 핵심 내용

Anthropic의 에이전트 설계 총론. 가장 널리 인용되는 에이전트 가이드.

**핵심 원칙: "가장 단순한 솔루션부터 시작하라"**
- 에이전트가 필요하지 않을 수 있음 → 워크플로우로 충분한가 먼저 확인
- 워크플로우: 사전 정의된 코드 경로 (결정적)
- 에이전트: 모델이 자율적으로 도구를 선택하고 경로를 결정 (비결정적)

**워크플로우 패턴 (단순 → 복잡):**
1. Prompt chaining — 순차 처리, 게이트 포함
2. Routing — 입력 분류 후 적절한 경로로 분배
3. Parallelization — 독립 작업 동시 실행
4. Orchestrator-worker — 중앙 조정자가 작업 분배
5. Evaluator-optimizer — 생성 + 평가 루프

**도구 설계 원칙:**
- 도구 설명이 명확해야 함 — 모델이 언제, 어떻게 사용할지 이해
- 입출력이 예측 가능해야 함
- 에러 메시지가 모델에게 유용해야 함

### 핵심 교훈
> "에이전트를 만들기 전에, 워크플로우로 충분한지 확인하라. 복잡도를 정당화할 수 있을 때만 에이전트를 선택하라."

---

## 1.7 HumanLayer — Skill Issue: Harness Engineering for Coding Agents

**출처:** [humanlayer.dev](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents)

### 핵심 내용

코딩 에이전트의 약한 결과는 모델의 한계가 아니라 **harness의 문제(skill issue)**라는 주장.

**흔한 오해:**
- "AI가 만든 코드는 별로다" → 대부분 harness가 부실한 것
- 같은 모델이라도 harness에 따라 결과가 크게 달라짐
- **모델을 바꾸기 전에 harness를 개선하라**

**Harness가 해결하는 문제들:**
- 컨텍스트 부족 → 관련 파일을 자동으로 포함
- 구조 불일치 → 아키텍처 규칙을 프롬프트에 명시
- 검증 부재 → 자동 테스트, 빌드, 린트를 루프에 포함
- 핸드오프 실패 → 세션 간 상태 전달 구조화

### 핵심 교훈
> "에이전트가 나쁜 코드를 만들면 모델을 탓하기 전에 harness를 확인하라. 대부분의 경우 skill issue는 harness issue다."

---

## 1.8 Inngest — Your Agent Needs a Harness, Not a Framework

**출처:** [inngest.com](https://www.inngest.com/blog/your-agent-needs-a-harness-not-a-framework)

### 핵심 내용

에이전트에게 필요한 것은 범용 프레임워크가 아니라 **인프라 수준의 harness**라는 주장.

**프레임워크의 한계:**
- 대부분의 에이전트 프레임워크는 프롬프트 체이닝에 집중
- 상태 관리, 재시도, 트레이싱, 동시성은 후순위
- 프로덕션에서 가장 문제되는 것이 바로 이 인프라 레이어

**Harness가 제공해야 하는 인프라:**
- **State** — 에이전트의 현재 상태를 영속적으로 관리
- **Retries** — 실패 시 자동 재시도 (지수 백오프)
- **Traces** — 전체 실행 경로 추적 (디버깅)
- **Concurrency** — 여러 에이전트/작업의 동시 실행 관리
- **Durability** — 프로세스 재시작에도 작업이 유지

### 핵심 교훈
> "프레임워크는 에이전트를 만드는 방법을 알려주지만, harness는 에이전트를 안정적으로 운영하는 방법을 제공한다."
