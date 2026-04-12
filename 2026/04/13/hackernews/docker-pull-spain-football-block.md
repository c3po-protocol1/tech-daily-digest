# 스페인, 축구 중계 차단으로 Docker Pull까지 먹통

- **출처**: [Tell HN (자체 게시물)](https://news.ycombinator.com/item?id=47738883)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47738883)
- **점수**: 106 points | 41 comments
- **태그**: `#docker` `#cloudflare` `#spain` `#censorship` `#infrastructure`

## 상세 요약

스페인의 한 개발자가 로컬 GitLab 러너에서 CI/CD 파이프라인이 실패하는 원인을 1시간 넘게 디버깅한 끝에, **축구 경기 중계 불법 스트리밍 차단 때문에 Docker 이미지 풀이 불가능**해진 것을 발견했다.

### 사건 경위:
1. GitLab 러너가 Docker 이미지 풀 시 TLS 에러 발생: `docker-images-prod.*.r2.cloudflarestorage.com` 인증서 검증 실패
2. Tailscale, DNS 등을 의심하며 디버깅했으나, 해당 URL을 브라우저에서 접속하니 스페인어 차단 메시지 표시
3. **원인**: LaLiga(스페인 프로축구 리그)의 법원 명령에 따라, 축구 경기 중에 Cloudflare의 특정 IP 범위가 통째로 차단
4. Cloudflare R2(오브젝트 스토리지)에 호스팅된 Docker Hub 이미지도 같은 IP 범위에 있어 부수적 피해(collateral damage) 발생

### 핵심 문제:
- **IP 기반 광역 차단의 위험성**: Cloudflare 뒤의 수십만 개 서비스가 하나의 IP 차단으로 모두 영향
- **인프라의 취약성**: CI/CD, API 엔드포인트, Docker 레지스트리가 스포츠 중계 저작권 보호 조치의 부수적 피해자
- 일부 ISP는 차단 메시지조차 없이 트래픽을 그냥 드롭하여 더 디버깅이 어려움
- 축구 경기 중인지 확인하는 웹사이트까지 등장

HN 댓글에서는 VPN 사용, 대체 DNS, 스페인 외부 시스템 운영 등의 우회 방법과 함께, 기술 전문가들의 지역 정치 참여 필요성이 논의되었다.

## Soo에게 의미 있는 이유

클라우드 인프라 의존도가 높은 현대 개발 환경에서, 예상치 못한 외부 요인(법적 IP 차단)이 개발 워크플로우를 완전히 중단시킬 수 있다는 교훈이다. 글로벌 서비스를 설계할 때 CDN 단일 의존 리스크와 지역별 인터넷 규제를 고려한 fallback 전략이 필요하다.
