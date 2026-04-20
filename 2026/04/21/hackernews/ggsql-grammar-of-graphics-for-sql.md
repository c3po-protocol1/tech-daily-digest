# ggsql: SQL을 위한 Grammar of Graphics — Posit 알파 릴리스

- **출처**: [Posit Open Source Blog](https://opensource.posit.co/blog/2026-04-20_ggsql_alpha_release/)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47833558) (327점, 71댓글)
- **태그**: `#SQL` `#시각화` `#ggplot2` `#데이터분석` `#오픈소스`

## 요약

ggplot2 팀(Hadley Wickham, Thomas Lin Pedersen 등)이 SQL 구문 내에서 직접 시각화를 기술하는 새로운 도구 **ggsql**의 알파 버전을 공개했다.

**핵심 개념:**
- SQL 쿼리 끝에 `VISUALIZE` 절을 추가하여 데이터 시각화를 선언적으로 정의
- `DRAW`로 레이어 추가, `PLACE`로 어노테이션, `SCALE`로 스케일 제어, `LABEL`로 제목/라벨 설정
- R이나 Python 없이 **단독 실행 가능** — 별도 런타임 불필요
- DuckDB 백엔드 지원, 10억 행 데이터도 집계만 전송하여 처리

**예시 코드:**
```sql
VISUALIZE bill_len AS x, bill_dep AS y, species AS color FROM ggsql:penguins
DRAW point
DRAW smooth
```

**왜 중요한가:**
- ggplot2의 18년 경험을 백지 상태에서 재설계
- SQL 사용자에게 강력한 코드 기반 시각화 도구 제공
- **LLM과의 궁합 탁월** — LLM이 SQL을 매우 잘 생성하므로 자연어 → 시각화 파이프라인 구축 용이
- 경량 실행 파일로 AI 에이전트에 안전하게 통합 가능 (샌드박싱 용이)
- querychat에서 이미 자연어 → ggsql 시각화 데모 운영 중

**향후 계획:**
- Rust로 작성된 고성능 렌더러
- 테마 인프라, 인터랙티비티
- 공간 데이터 지원
- 전용 LSP(언어 서버) 및 코드 포매터

## Soo에게 의미 있는 이유

데이터 분석과 AI의 교차점에 있는 혁신적 도구. SQL만 아는 분석가도 ggplot2 수준의 시각화를 할 수 있고, LLM이 생성하기에 최적화된 구문 설계는 AI 에이전트 기반 데이터 분석 워크플로우의 핵심 컴포넌트가 될 수 있다. AInD 컨설팅에서 데이터 분석 자동화 솔루션 설계 시 참고할 만한 프로젝트.
