# 🔒 누군가 WordPress 플러그인 30개를 사들여 백도어를 심었다

- **출처**: [anchor.host](https://anchor.host/someone-bought-30-wordpress-plugins-and-planted-a-backdoor-in-all-of-them/)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47755629) (545 points, 151 comments)
- **태그**: `#보안` `#WordPress` `#공급망공격` `#백도어`

## 상세 요약

Anchor Hosting의 Austin Ginder가 발견한 대규모 WordPress 공급망 공격 사례다. 인도 기반 "Essential Plugin" 팀이 2015년부터 8년간 구축한 30개 이상의 WordPress 플러그인 포트폴리오가 Flippa 마켓플레이스에서 6자릿수(수십만 달러)에 매각되었고, 구매자 "Kris"는 SEO, 암호화폐, 온라인 도박 마케팅 배경을 가진 인물이었다.

**공격 기법이 매우 정교하다:**
- 2025년 8월 첫 SVN 커밋에 `wpos-analytics` 모듈로 위장한 PHP 역직렬화 백도어 삽입
- `file_get_contents()` + `@unserialize()` + `__return_true` 권한 콜백으로 원격 코드 실행(RCE) 가능
- **8개월간 휴면** 상태 유지 후 2026년 4월에 활성화
- C2 도메인을 **이더리움 스마트 컨트랙트**로 리졸브하여 전통적 도메인 차단 무력화
- Googlebot에게만 스팸 링크와 리다이렉트를 보여주는 클로킹 기법

**피해 규모:**
- 31개 플러그인이 WordPress.org에 의해 영구 폐쇄됨
- `wp-config.php`에 약 6KB 악성 코드 주입 (강제 업데이트로도 제거 안 됨)
- 수십만 개 활성 설치 사이트에 영향

**핵심 문제:** WordPress.org에는 플러그인 소유권 이전 시 검토 메커니즘이 전혀 없다. 사용자 통지도, 추가 코드 리뷰도 없다. 2017년 Display Widgets 사건(200,000 설치)과 동일한 패턴이 훨씬 큰 규모로 반복된 것이다.

## Soo에게 의미 있는 이유

공급망 보안은 AI 시대에도 여전히 핵심 이슈다. 오픈소스 생태계의 "신뢰"를 이용한 공격 패턴은 npm, PyPI 등 모든 패키지 매니저에 적용 가능하며, AInD 컨설팅에서 보안 검토 프레임워크를 설계할 때 이런 사례를 참고해야 한다. 특히 이더리움 스마트 컨트랙트를 C2로 활용하는 기법은 새로운 위협 벡터다.
