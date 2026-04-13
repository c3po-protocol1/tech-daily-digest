# 🔥 프롬프트에서 하네스까지 — AI 에이전틱 패턴 4년의 기록

> **출처**: [bits-bytes-nn.github.io](https://bits-bytes-nn.github.io/insights/agentic-ai/2026/04/05/evolution-of-ai-agentic-patterns.html) | [GeekNews 토론](https://news.hada.io/topic?id=28301)
> **점수**: 67점 | **댓글**: 7개
> **태그**: `#AI` `#에이전트` `#프롬프트엔지니어링` `#컨텍스트엔지니어링` `#하네스엔지니어링`
> 🔥 **2일 이상 연속 트렌딩**
> 📝 **상세 요약**: [articles/ai-engineering/2026-04-13-agentic-patterns-4-years-history.md](../../../articles/ai-engineering/2026-04-13-agentic-patterns-4-years-history.md)

## 요약

2022~2026년 AI 개발 패러다임의 세 번의 전환을 추적하는 심층 분석 글. "서베이가 아니라 부검 보고서"라고 자칭한다.

**세 번의 패러다임 전환:**

1. **Prompt Engineering (2022-2024)** — "어떤 말을 해야 하나?"
   - GitHub Copilot (2022.06): 최초의 상업용 AI 코딩 어시스턴트, 개발자 88% 생산성 향상 체감
   - ChatGPT (2022.11): 5일 만에 100만 사용자, "영어가 프로그래밍 언어"
   - Chain-of-Thought (Wei et al., 2022): "단계별로 생각하라" → PaLM 540B 수학 정확도 17.9%→58.1%
   - ReAct (Yao et al., 2022): 생각(Thought)+행동(Action) 루프 — 모든 현대 에이전트의 원형

2. **Context Engineering (2025)** — "어떤 정보를 넣어야 하나?"
   - 프롬프트보다 컨텍스트 윈도우에 무엇을 채울지가 더 중요
   - Shopify CEO Tobi Lütke가 2025.06 점화, Karpathy·Andrew Ng 합류

3. **Harness Engineering (2026)** — "어떤 시스템을 만들어야 하나?"
   - 컨텍스트를 소비하는 전체 시스템의 설계가 진짜 문제
   - KV-cache hit rate가 핵심 메트릭이 됨

**핵심 논지:**
Chad Fowler의 "Relocating Rigor" 인용 — 엔지니어링의 엄밀함은 사라지지 않는다, **이동할 뿐이다**. 설계 문서→테스트 코드, 컴파일러 검사→런타임 테스트처럼, 코드 작성의 엄밀함이 컨텍스트 설계→시스템 아키텍처로 이동 중.

**Copilot 진화가 축소판:**
- 2022: 자동완성 (프롬프트 시대)
- 2023: Chat + GPT-4 (컨텍스트 전환 시작)
- 2025: Agent Mode (하네스 시대)
- 2025: Coding Agent (완전 자율 워크플로우)

## Soo에게 의미 있는 이유

AInD 컨설팅의 **필독 자료**. AI 개발 패러다임 4년의 변화를 하나의 맥락으로 정리한 최고의 글 중 하나. "프롬프트 엔지니어링은 죽었다"가 아니라 "엄밀함이 이동했다"는 프레이밍이 클라이언트에게 설명하기 좋다. TF 발표 자료에 직접 활용 가능.
