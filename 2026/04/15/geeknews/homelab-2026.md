# 홈랩 2026 현황 — 셀프호스팅 취미의 진화

- **출처**: [mrlokans.work](https://mrlokans.work/posts/state-of-homelab-2026/)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28509) (29P, 댓글 9개)
- **태그**: #홈랩 #셀프호스팅 #Docker #인프라

## 상세 요약

소규모 하드웨어와 무료 클라우드 터널링을 결합해 미디어·AI·사진·모니터링 등 다양한 서비스를 자체 운영하는 홈랩 구축 사례다. **월 약 7유로**의 운영 비용으로 벤더 종속 없이 데이터 소유권을 유지한다.

**하드웨어:** OrangePI 5에서 GMKTec NUC(AMD Ryzen 7 5700U, 32GB RAM, 1TB NVMe)로 업그레이드. Hetzner VM 병행 운영.

**네트워크:** Cloudflare Tunnel로 인바운드 포트 개방 없이 외부 접근. Traefik + Authentik으로 리버스 프록시와 SSO 인증.

**운영 도구:** Ansible 역할(role) 기반 IaC + SOPS(age 암호화)로 재현성과 보안 확보. Docker 컨테이너로 모든 서비스 실행.

**주요 서비스:** *arr 스택(미디어 자동화), Jellyfin(미디어 서버), Navidrome(음악 스트리밍), Calibre Web(전자책), 그리고 AI 관련 서비스들.

**운영 원칙:** Infrastructure-as-Code, 재현성(장애 시 빠른 재배포), 사용 편의성(표준적 접근 선호). 완벽보다 학습과 즐거움에 가치를 둔다.

## Soo에게 의미 있는 이유

AI 개발 환경을 로컬에서 구축하는 트렌드와 연결된다. 특히 Cloudflare Tunnel + Traefik + Authentik 조합은 사내 AI 서비스 배포 시 참고할 만한 패턴이다.
