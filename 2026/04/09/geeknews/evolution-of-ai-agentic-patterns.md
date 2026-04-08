# 프롬프트에서 하네스까지 — AI 에이전틱 패턴 4년의 기록

- **출처:** [bits-bytes-nn.github.io](https://bits-bytes-nn.github.io/insights/agentic-ai/2026/04/05/evolution-of-ai-agentic-patterns.html)
- **GeekNews:** [topic?id=28301](https://news.hada.io/topic?id=28301) (40 points)
- **태그:** `#AI에이전트` `#프롬프트엔지니어링` `#컨텍스트엔지니어링` `#하네스엔지니어링`

## 상세 요약

2022-2026년 AI 개발 패러다임이 세 번 전환된 과정을 "부검 보고서" 형식으로 추적한 심층 분석.

### 3번의 패러다임 전환
1. **Prompt Engineering (2022-2024):** "어떤 말을 해야 하나?" — Chain-of-Thought, ReAct 등 프롬프트 기법이 핵심
2. **Context Engineering (2025):** "어떤 정보를 넣어야 하나?" — Shopify CEO Tobi Lütke가 점화, Karpathy·Andrew Ng 합류. 프롬프트보다 컨텍스트 윈도우에 무엇을 채울지가 더 중요
3. **Harness Engineering (2026):** "어떤 시스템을 만들어야 하나?" — 컨텍스트를 소비하는 전체 시스템 설계가 진짜 문제

### 핵심 논지: "Relocating Rigor" (Chad Fowler)
엔지니어링의 엄밀함은 사라지지 않았다 — 이동했을 뿐이다.
- XP 운동: 설계 문서 → 자동화 테스트
- 동적 언어: 컴파일러 검사 → 런타임 테스트
- AI 시대: 코드 작성 → 컨텍스트 설계 → 시스템 아키텍처

### 역사적 기점들
- 2022.06: GitHub Copilot 정식 출시 (프롬프트 시대 서막)
- 2022.11: ChatGPT → "영어가 곧 프로그래밍 언어"
- 2022: CoT (Chain-of-Thought), ReAct 논문 → 에이전트의 원형 탄생
- 2026 핵심 메트릭: KV-cache hit rate, 하네스 복잡도

### Copilot 진화가 보여주는 축소판
초기 자동완성(프롬프트) → Copilot Chat(컨텍스트) → Agent Mode(하네스) → Coding Agent(완전자율)

## Soo에게 의미 있는 이유
AInD 컨설팅 TF의 핵심 교육 자료로 활용 가능. 3가지 시대 구분과 "Relocating Rigor" 프레임워크는 클라이언트에게 AI 도입의 본질을 설명하는 강력한 도구.
