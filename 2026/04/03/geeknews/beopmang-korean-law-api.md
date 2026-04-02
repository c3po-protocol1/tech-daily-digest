# Show GN: 법망 — PostgreSQL 기반 한국 법령 전체를 JSON으로 제공하는 에이전트용 API

- **출처:** https://api.beopmang.org
- **GeekNews:** https://news.hada.io/topic?id=28050
- **점수:** 81 points
- **태그:** #korean-law #api #agent #postgresql #pgvector

## 상세 요약

로스쿨 학생이 개발한 에이전트 친화적 법령 정보 API로, 국가법령정보센터의 거의 모든 법령(99.9%+)을 JSON으로 제공한다.

**핵심 기능:**
- XML, HWP, PDF 사전 파싱 — 표 데이터 포함 모든 출력이 JSON
- PostgreSQL + pgvector 기반, 주요 조문 20만건 임베딩(768d)으로 시맨틱 검색 지원
- 인증키 불필요한 REST API, rate limit 100회/분
- 매주 토요일 최신 법령 동기화
- 로깅 없음 (IP, 쿼리 등 미수집), 익명 엔드포인트 호출 빈도만 집계
- 4가지 기본 Action(law.search, law.get, law.diff, law.history)만으로 에이전트가 빠르게 탐색 가능
- 법제처 공식 API 대비 원하는 정보 도달 시간과 토큰 모두 1/10 수준으로 축소
- Claude/Codex의 경우 MCP 설정 없이 프롬프트 한 줄로 바로 사용 가능

공개 24시간 만에 누적 2만 건 이상의 API 호출을 기록했으며, 커뮤니티 피드백으로 버그 수정도 진행 중. 변호사시험 이후에도 계속 유지보수 예정.

## Soo에게 의미 있는 이유

AI 에이전트가 법률 정보에 접근하는 실용적 사례로, 도메인 특화 API + pgvector 시맨틱 검색의 조합이 인상적이다. 한국에서 AI 에이전트를 활용한 전문 분야 서비스의 좋은 레퍼런스이며, AInD 컨설팅에서 "AI 에이전트 + 도메인 지식" 활용 사례로 소개할 수 있다.
