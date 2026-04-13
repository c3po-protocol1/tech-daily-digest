# 🗄️ pgmicro — SQLite 기반으로 만든 인-프로세스 PostgreSQL

- **출처**: [GeekNews](https://news.hada.io/topic?id=28464) | [GitHub](https://github.com/glommer/pgmicro)
- **태그**: `#데이터베이스` `#PostgreSQL` `#SQLite` `#Rust` `#AI에이전트`

## 상세 요약

PostgreSQL SQL을 SQLite 바이트코드로 직접 컴파일하는 인메모리 임베디드 데이터베이스다. AI 에이전트 환경에서 급증하는 일시적·소규모 데이터베이스 수요를 겨냥해 설계되었다.

**핵심 기술적 특징:**
- Rust로 처음부터 재작성한 SQLite 재구현체인 **Turso**를 엔진으로 사용
- PostgreSQL의 실제 파서(`libpg_query`)를 그대로 채택해 **100% 구문 호환성** 확보
- 생성된 데이터 파일은 **표준 SQLite 3.x .db 형식** → 기존 SQLite 도구로 열람 가능
- 커넥션 레벨에서 PostgreSQL과 SQLite 문법을 **동적 전환** 가능
- PostgreSQL을 WebAssembly로 변환하거나 내장하는 기존 방식과 근본적으로 다른 아키텍처
- MIT 라이선스

**기존 방식과의 차이:** PGLite 같은 프로젝트는 Postgres 전체를 Wasm으로 포팅하는 반면, pgmicro는 Postgres의 SQL 파서만 가져와 SQLite 바이트코드로 컴파일한다. 훨씬 경량이면서도 Postgres 구문 호환성을 유지한다.

## Soo에게 의미 있는 이유

AI 에이전트가 작업 중 임시 데이터를 구조화하여 저장/쿼리하는 패턴이 늘고 있다. pgmicro는 에이전트가 Postgres SQL을 알면 별도 서버 없이 인-프로세스로 데이터를 관리할 수 있게 한다. AInD 프로젝트에서 에이전트 데이터 관리 패턴으로 주목할 만하다.
