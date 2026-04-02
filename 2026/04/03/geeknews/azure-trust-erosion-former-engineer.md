# Azure 신뢰를 무너뜨린 결정들 — 전직 Azure Core 엔지니어의 폭로

- **출처:** https://isolveproblems.substack.com/p/how-microsoft-vaporized-a-trillion
- **HN 토론:** https://news.ycombinator.com/item?id=47616242
- **점수:** 145 points (HN) 
- **태그:** #microsoft #azure #engineering #management #insider

## 상세 요약

전직 Azure Core 엔지니어 Axel Rietschin이 "Microsoft가 어떻게 1조 달러를 증발시켰는가"라는 시리즈의 첫 글을 공개했다. Windows 커널 엔지니어이자 Docker/Container 플랫폼 발명 기여자였던 저자가 2023년 Azure Core Overlake R&D 팀에 합류한 첫날부터 목격한 조직적 문제를 상세히 서술한다.

**핵심 폭로:**
- 합류 첫날 월간 계획 회의에서, 팀이 손톱만한 ARM SoC에 Windows의 절반을 포팅하려는 비현실적 계획을 세우고 있었다
- Overlake 카드의 FPGA에 확보할 수 있는 듀얼포트 메모리가 4KB에 불과한데, 122명 규모의 조직이 Windows를 Linux로 포팅하는 계획을 진지하게 논의
- Azure 노드를 관리하는 에이전트가 **173개**에 달하며, Microsoft 내부의 누구도 왜 173개가 필요한지, 각각이 무엇을 하는지, 어떻게 상호작용하는지 설명할 수 없었다
- 이 스택은 400W Xeon에서 수십 개 VM 수준에서 스케일링 한계에 도달 — 하이퍼바이저의 1,024 VM 한도에 한참 못 미치는 수준
- 이 깨지기 쉬운 스택이 Anthropic의 Claude, OpenAI API, SharePoint Online, 정부 클라우드 등 미션 크리티컬 인프라를 운영

시리즈 예고: CEO에게 보낸 서한, Microsoft 이사회에 보낸 서한, OpenAI 거의 상실, 국방장관의 신뢰 위반 공개 발언, Rust 명령, OpenAI 베어메탈 팀 경험, 중국 등으로부터의 에스코트 세션 등.

## Soo에게 의미 있는 이유

클라우드 인프라의 내부 실태를 이해하는 것은 AInD 컨설팅에서 "어떤 클라우드를 선택할 것인가"에 대한 조언에 직결된다. 대규모 기술 조직의 기술 부채와 관리 실패가 어떻게 1조 달러 규모의 영향을 미치는지를 보여주는 교과서적 사례다.
