# iroh — 공개키 기반 초고속 P2P 네트워크 연결 라이브러리

- **출처**: [GitHub/n0-computer/iroh](https://github.com/n0-computer/iroh)
- **GeekNews**: [topic?id=28702](https://news.hada.io/topic?id=28702) (10점)
- **태그**: `#P2P` `#Rust` `#네트워킹` `#오픈소스`

## 요약

"IP 주소 대신 키로 연결하라"는 모토의 Rust 기반 모듈형 P2P 네트워킹 스택.

**핵심 특징:**
- 네트워크 주소나 IP가 아닌 **공개키(Ed25519) 기반 연결**
- "저 전화기로 연결해줘"라고 하면 위치 무관하게 가장 빠른 네트워크 경로를 자동 탐색·유지
- NAT traversal, relay fallback 자동 처리
- 모듈형 구조: `iroh-base`, `iroh-dns`, `iroh-relay` 등 필요한 것만 사용
- 8.3K 스타, 395포크, 2,401 커밋 — 활발한 프로젝트

**기술적 구성:**
- DNS 기반 노드 발견 (iroh-dns)
- 릴레이 서버 (iroh-relay) — 직접 연결 불가 시 폴백
- Apache 2.0 + MIT 듀얼 라이선스

## Soo에게 의미 있는 이유

AI 에이전트 간 P2P 통신, 분산 AI 워크로드, 엣지 디바이스 연결 등에 활용 가능한 인프라 라이브러리. 클라우드 의존 없는 분산 시스템 구축 시 참고할 만한 프로젝트.
