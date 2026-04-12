# 스페인 축구 중계로 인해 Docker Pull이 실패하다

> **출처**: [Hacker News (Tell HN)](https://news.ycombinator.com/item?id=47738883)
> **점수**: 604점 | **댓글**: 233개
> **태그**: `#인프라` `#Cloudflare` `#DNS` `#규제`

## 요약

스페인에서 한 개발자가 로컬 GitLab runner의 CI 파이프라인이 갑자기 실패하는 문제를 1시간 넘게 디버깅했다. `docker pull`을 실행하면 TLS 인증서 오류가 발생했는데, 원인은 놀랍게도 **스페인 프로축구 리그(LaLiga)의 불법 스트리밍 차단 조치**였다.

스페인 바르셀로나 상업법원의 2024년 12월 판결에 따라, LaLiga와 Telefónica는 축구 경기 중계 시간에 불법 스트리밍과 관련된 Cloudflare IP를 차단할 수 있는 권한을 받았다. 문제는 Docker 이미지가 저장된 Cloudflare R2 스토리지(`docker-images-prod.*.r2.cloudflarestorage.com`)가 **같은 IP 대역에 위치**한다는 것이다.

결과적으로 축구 경기가 진행되는 동안 스페인 전역에서:
- Docker 이미지 Pull 실패
- CI/CD 파이프라인 중단
- Cloudflare R2 기반 서비스 접근 불가

개발자가 브라우저에서 해당 URL에 접속하니 스페인어로 "법원 판결에 의해 차단됨"이라는 메시지가 나타났다. Tailscale, DNS 설정 등을 의심하며 시간을 낭비한 끝에야 원인을 발견했다.

HN 댓글에서는 유럽 전역에서 비슷한 과잉 차단 사례가 보고되었으며, IP 기반 차단의 부작용(collateral damage)에 대한 비판이 쏟아졌다. 스페인 ISP들이 Cloudflare IP 전체를 차단하는 방식이 근본적으로 문제가 있다는 지적이 주를 이뤘다.

## Soo에게 의미 있는 이유

인프라/DevOps 관점에서 매우 중요한 사례다. CI/CD 파이프라인이 **국가 규제 + CDN 차단의 예상치 못한 조합**으로 실패할 수 있다는 것을 보여준다. AInD 컨설팅 시 글로벌 배포 환경에서 이런 지역별 네트워크 규제 이슈를 사전에 파악해야 한다. 또한 Cloudflare 의존도가 높은 현대 인프라의 SPOF(단일 장애점) 리스크를 상기시킨다.
