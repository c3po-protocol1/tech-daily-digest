# GBrain — 오픈소스 개인 지식 베이스

- **출처**: [GitHub](https://github.com/garrytan/gbrain)
- **GeekNews**: [토론](https://news.hada.io/topic?id=28323) (27 points)
- **태그**: `#knowledge-management` `#ai-agent` `#personal-memex`

## 상세 요약

YC CEO Garry Tan이 Karpathy의 LLMWiki 아이디어를 발전시켜 만든 개인 지식 관리 도구. OpenClaw 에이전트의 마크다운 기반 지식 저장소로 시작하여, 대규모 데이터에서는 Postgres + pgvector 기반 검색으로 확장.

**규모:** 10,000+ 마크다운 파일, 3,000+ 인물 도시에, 13년 캘린더 데이터(21,000+ 이벤트), 5,800+ Apple Notes, 280+ 미팅 트랜스크립트, 300+ 아이디어 캡처.

**핵심 기능:**
- 사람, 회사, 미디어, 아이디어별 구조화된 마크다운 스키마
- "Dream Cycle" (DREAMS.md): 에이전트가 밤에 하루 대화를 스캔하고 누락된 엔티티를 보강, 깨진 인용을 수정, 기억을 통합
- 소셜 그래프 교차 질의: "Pedro와 Diana를 둘 다 아는 사람은?"
- 자기 사고 검색: "수치심과 창업자 성과 관계에 대해 뭐라고 했지?"

1,000~10,000 문서 규모에서 `grep`이 한계에 도달하면 Postgres chunking + 벡터 검색이 필요해진다.

## Soo에게 의미 있는 이유

개인 지식 관리의 AI-네이티브 접근법. OpenClaw과 유사한 에이전트 워크스페이스 패턴이며, "에이전트가 밤에 기억을 정리한다"는 Dream Cycle 개념이 흥미로움.
