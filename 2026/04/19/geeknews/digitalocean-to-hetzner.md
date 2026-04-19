# DigitalOcean에서 Hetzner로 마이그레이션하기

- **출처**: [Hacker News 토론](https://news.ycombinator.com/item?id=47807583)
- **토론**: [GeekNews](https://news.hada.io/topic?id=28671)
- **태그**: `#cloud` `#infrastructure` `#migration` `#cost-optimization`

## 상세 요약

클라우드 서버를 DigitalOcean/Linode에서 Hetzner로 이전한 경험담과 관련 커뮤니티 토론이다.

**마이그레이션 경험:**
- 서버 2대를 Linode와 DO에서 Hetzner로 이전, 비용을 크게 절감
- 수십 개 사이트가 서로 다른 언어, 오래된 라이브러리, MySQL·Redis가 뒤엉킨 복잡한 스택
- **Claude Code가 전체 마이그레이션을 처리** — 없는 라이브러리는 코드를 다시 작성하며 해결
- 향후 클라우드 사업자 간 이동성이 더 커질 전망

**AWS 탈출 계획:**
- Amazon은 경쟁사보다 때로 20배 비싼 가격, 장기 약정 강요, 비싼 데이터 이전 비용
- egress 요금이 사실상 "한 부분만 옮겨도 전체를 다 옮기게 만드는 압박"으로 작동
- Amazon 전용 서비스 위에 플랫폼을 쌓지 않은 경우 이전이 비교적 수월

**반론 — 이중화/가용성 우려:**
- 서버 한 대로 모든 서비스를 운영하면 가용성 문제 발생 가능
- Kubernetes 기반 멀티 노드 구성으로 Hetzner에서도 HA 구현 가능
- 단일 노드라면 Kubernetes가 과도할 수 있으나, 여러 노드면 효과적

**Hetzner의 장점:**
- 유럽 기반 서버로 가격 대비 성능이 뛰어남
- 독일 데이터센터의 안정성
- AWS/DO 대비 월 비용 50-80% 절감 사례 다수

## Soo에게 의미 있는 이유

AI 에이전트(Claude Code)가 복잡한 인프라 마이그레이션을 처리했다는 사례는 AInD 컨설팅의 핵심 사례가 된다. "AI가 코드만 짜는 게 아니라 인프라 이전까지 돕는다"는 포인트는 기업 고객에게 AI 도입의 ROI를 설명할 때 강력한 근거다. 또한 클라우드 비용 최적화는 모든 기업의 관심사이며, vendor lock-in 탈피 전략은 실무적으로 중요하다.
