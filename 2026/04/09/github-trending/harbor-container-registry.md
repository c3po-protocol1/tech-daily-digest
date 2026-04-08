# goharbor/harbor — 오픈소스 클라우드 네이티브 컨테이너 레지스트리

- **GitHub:** [goharbor/harbor](https://github.com/goharbor/harbor)
- **태그:** `#CNCF` `#컨테이너` `#레지스트리` `#보안` `#DevOps`

## 상세 요약

CNCF가 호스팅하는 오픈소스 컨테이너 레지스트리. Docker Distribution을 확장하여 엔터프라이즈에 필요한 보안·관리 기능을 추가.

### 핵심 기능
- **RBAC:** 프로젝트 기반 역할별 접근 제어
- **정책 기반 복제:** 필터(저장소/태그/라벨)로 다중 레지스트리 간 이미지 동기화
- **취약점 스캔:** 정기적 이미지 스캔, 취약 이미지 배포 차단 정책
- **LDAP/AD, OIDC 지원:** 기존 엔터프라이즈 인증 통합, SSO
- **Notary:** Docker Content Trust로 이미지 서명·출처 보장
- **Cosign 서명 검증:** v2.15.0+에서 릴리스 아티팩트 서명 지원
- **GUI 포털, RESTful API, 감사 로그**

### 배포
Docker Compose, Helm Chart, Harbor Operator 지원. Linux 호스트 기본.

### 의의
Fortune 100 기업들이 사용하는 프로덕션급 컨테이너 레지스트리의 사실상 표준.

## Soo에게 의미 있는 이유
AI 에이전트를 컨테이너로 배포할 때 이미지 관리·보안 스캐닝의 표준 도구. Scion 같은 에이전트 오케스트레이터가 컨테이너 기반이므로 직접 관련.
