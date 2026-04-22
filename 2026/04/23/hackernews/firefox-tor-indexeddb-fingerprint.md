# Firefox/Tor의 IndexedDB 프라이버시 취약점 발견

- **출처**: [Fingerprint.com](https://fingerprint.com/blog/firefox-tor-indexeddb-privacy-vulnerability/)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47866697)
- **점수**: 307점 | 댓글 86개
- **태그**: `#보안` `#프라이버시` `#Firefox` `#Tor` `#핑거프린팅`

## 상세 요약

Fingerprint.com의 보안 연구팀이 **모든 Firefox 기반 브라우저에 영향을 미치는 프라이버시 취약점**을 발견했다. `indexedDB.databases()` API가 반환하는 데이터베이스 목록의 순서가 내부 저장 구조에 기반하여 결정적(deterministic)이고 안정적(stable)인 식별자를 생성할 수 있다는 것.

**취약점의 핵심:**
- 웹사이트가 IndexedDB 데이터베이스 세트를 생성하고 반환 순서를 검사하면, 이를 브라우저 프로세스의 고유 핑거프린트로 사용 가능
- 이 동작은 origin-scoped가 아닌 **process-scoped**이므로, 서로 관련 없는 웹사이트들이 동일한 식별자를 관찰 가능
- Firefox 프라이빗 브라우징 모드에서도 프로세스가 실행 중이면 식별자가 유지됨
- **Tor 브라우저의 "New Identity" 기능조차 이 식별자를 리셋하지 못함**

기술적 원인: Firefox의 프라이빗 브라우징 모드에서 DB 이름이 UUID 기반 해시 테이블을 통해 매핑되는데, 이 해시 테이블의 내부 순서가 프로세스 전체에서 공유되며 API 응답에 노출됨.

Mozilla는 Firefox 150과 ESR 140.10.0에서 수정 완료. 수정 방법은 API 결과를 반환 전 정렬(canonicalize)하는 것.

**교훈:** "무해해 보이는 API도 내부 구현의 결정론적 노출이 있으면 크로스-사이트 추적 벡터가 될 수 있다."

## Soo에게 의미 있는 이유

AI 에이전트와 웹 브라우저의 통합이 늘어나는 상황에서, 에이전트가 웹을 탐색할 때의 프라이버시/보안 모델은 중요한 설계 고려사항이다. 또한 "API의 반환 순서"처럼 사소해 보이는 구현 디테일이 보안 취약점이 되는 사례는 AI 시스템 설계 시에도 유사하게 적용된다.
