# 법망 — PostgreSQL 기반 한국 법령 전체를 JSON으로 제공하는 에이전트용 API

- **출처**: [api.beopmang.org](https://api.beopmang.org)
- **GeekNews**: [topic/28050](https://news.hada.io/topic?id=28050) — 91pts
- **태그**: `#법률AI` `#API` `#PostgreSQL` `#한국`

## 요약

법학전문대학원 재학생이 실무수습 중 느낀 필요성으로 만든, 한국 법령 전체를 AI 에이전트 친화적으로 제공하는 REST API.

### 핵심 스펙

- **법령 수록**: 국가법령정보센터 제공 법령 99.9%+ (XML, HWP, PDF 사전 파싱)
- **출력**: 표 데이터 포함 모든 출력 JSON
- **검색**: PostgreSQL + pgvector, 주요 조문 20만건 임베딩(768d) — semantic search 지원
- **성능**: rate limit 100회/분, 4분 내 500 동시접속 20K+ 요청 처리
- **프라이버시**: 로깅 없음 (IP, 쿼리 등), 익명 엔드포인트 호출 빈도만 집계
- **갱신**: 매주 토요일 최신 동기화

### 4개 핵심 Action

- `law.search`: 법령 검색
- `law.get`: 법령 조회
- `law.diff`: 법령 변경사항 비교
- `law.history`: 법령 개정 이력

### 사용 편의성

- **인증키 불필요**
- Claude/Codex: MCP 설정 없이 프롬프트 한 줄로 사용 가능
- 법제처 공식 API 대비 정보 도달 시간/토큰 **1/10 수준**

### 반응

- 공개 24시간 내 누적 2만건 이상 API 호출
- 변호사시험 후에도 계속 사용할 목적으로 제작 — 유지보수 지속 예정

## Soo에게 의미 있는 이유

도메인 특화 AI API의 모범 사례. AInD 컨설팅에서 "특정 산업의 데이터를 에이전트 친화적으로 만드는 것"이 핵심 가치라는 것을 보여준다. pgvector를 활용한 semantic search + 전통 DB의 조합도 참고할 아키텍처.
