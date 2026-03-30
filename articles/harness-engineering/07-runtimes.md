# 7. Runtimes, Harnesses & Reference Implementations — 런타임과 참조 구현

> 실제로 harness를 구축하거나 참고할 수 있는 프로젝트와 가이드.

---

## 7.1 LangChain — Agent Frameworks, Runtimes, and Harnesses, Oh My!

**출처:** [blog.langchain.com](https://blog.langchain.com/agent-frameworks-runtimes-and-harnesses-oh-my/)

### 핵심 내용

프레임워크, 런타임, harness의 **명확한 구분**. 혼동하기 쉬운 세 개념을 정리.

| 구분 | 역할 | 예시 |
|------|------|------|
| **프레임워크** | 에이전트를 구축하는 라이브러리/도구 | LangChain, CrewAI, AutoGen |
| **런타임** | 에이전트를 실행하는 인프라 | Inngest, Temporal, Celery |
| **Harness** | 특정 작업에 맞춘 프롬프트+도구+검증 조합 | SWE-agent, Claude Code 설정 |

**핵심 통찰:**
- 프레임워크는 범용, harness는 특수 목적
- 좋은 harness는 프레임워크 없이도 존재 가능 (단순한 스크립트 + 프롬프트)
- 런타임은 harness의 **실행 안정성**을 보장 (재시도, 상태 관리, 내구성)

### 핵심 교훈
> "프레임워크를 선택하기 전에 harness를 설계하라. Harness가 명확하면 프레임워크 선택은 쉬워진다."

---

## 7.2 Anthropic — Building Agents with the Claude Agent SDK

**출처:** [claude.com/blog](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

### 핵심 내용

Anthropic의 **프로덕션 지향 에이전트 SDK**. 세션, 도구, 오케스트레이션을 1급 시민으로 지원.

**주요 기능:**
- **세션 관리** — 컨텍스트 윈도우 전환, compaction, 핸드오프 자동화
- **도구 등록** — 에이전트가 사용할 도구를 선언적으로 정의
- **오케스트레이션** — 멀티 에이전트 패턴 (플래너-실행자-평가자) 지원
- **Hooks** — 에이전트 생명주기의 각 단계에 커스텀 로직 주입

**우리가 사용하는 것:** OpenClaw가 Claude Agent SDK 위에서 에이전트를 실행하며, Holocron이 이를 모니터링.

---

## 7.3 Anthropic — How We Built Our Multi-Agent Research System

**출처:** [anthropic.com](https://www.anthropic.com/engineering/multi-agent-research-system)

### 핵심 내용

Anthropic 내부의 **멀티 에이전트 리서치 시스템** 아키텍처.

**핵심 설계:**
- 역할 분리 — 검색 에이전트, 분석 에이전트, 요약 에이전트
- 구조화된 조정 — 에이전트 간 결과를 파일/아티팩트로 전달
- 각 에이전트는 **독립적으로 실행 가능** (느슨한 결합)

**Holocron과의 연관:** 이 시스템은 여러 에이전트가 독립적으로 동작하는 패턴을 보여줌. Holocron이 모니터링하려는 것이 바로 이런 구조.

---

## 7.4 LangChain — deepagents

**출처:** [github.com/langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)

LangChain의 **장기 실행 에이전트** 오픈소스 프로젝트. 미들웨어와 harness 패턴을 활용하여 더 깊고 오래 실행되는 에이전트를 구축. 컨텍스트 관리, 체크포인팅, 검증 루프 등의 패턴을 코드로 제공.

---

## 7.5 SWE-agent

**출처:** [github.com/SWE-agent/SWE-agent](https://github.com/SWE-agent/SWE-agent)

**가장 성숙한 연구용 코딩 에이전트.** harness, 프롬프트, 도구, 환경 설계를 **모두 직접 검사**할 수 있어 harness 엔지니어링 학습에 최적.

**왜 중요한가:**
- 오픈소스로 harness의 모든 구성 요소를 볼 수 있음
- SWE-bench에서 상위 성적 → harness 설계가 검증됨
- 프롬프트, 도구 설계, 환경 구성의 **실제 동작 예시**

---

## 7.6 SWE-ReX

**출처:** [github.com/SWE-agent/SWE-ReX](https://github.com/SWE-agent/SWE-ReX)

AI 에이전트를 위한 **샌드박스 코드 실행 인프라**. harness 작업이 실행 런타임 설계와 합류하는 지점. Docker 기반 격리 실행, 리소스 제한, 상태 리셋 등을 제공.

---

## 7.7 Inngest — AgentKit

**출처:** [github.com/inngest/agent-kit](https://github.com/inngest/agent-kit)

이벤트 드리븐 인프라 위에 **내구성 있는, 워크플로우 인식 에이전트**를 구축하는 TypeScript 도구. 상태 관리, 재시도, 동시성 제어를 인프라 레벨에서 해결.

---

## 7.8 Harbor

**출처:** [github.com/harbor-framework/harbor](https://github.com/harbor-framework/harbor)

대규모 에이전트 평가와 개선을 위한 **범용 harness 프레임워크**. Terminal-Bench 2.0과 함께 출시. 다양한 에이전트를 플러그인 방식으로 연결하여 벤치마킹 가능.

---

## 7.9 Terminal-Bench (Implementation)

**출처:** [github.com/harbor-framework/terminal-bench](https://github.com/harbor-framework/terminal-bench)

셸 네이티브 에이전트 벤치마크의 **오픈소스 구현체**. 실제 eval 파이프라인과 채점 로직을 코드로 확인 가능.

---

### 참조 구현 선택 가이드

| 목적 | 추천 |
|------|------|
| Harness 설계 학습 | SWE-agent (가장 투명) |
| 프로덕션 에이전트 SDK | Claude Agent SDK |
| 장기 실행 패턴 | deepagents (LangChain) |
| 샌드박스 실행 | SWE-ReX |
| 내구성 인프라 | AgentKit (Inngest) |
| 벤치마킹 프레임워크 | Harbor + Terminal-Bench |
