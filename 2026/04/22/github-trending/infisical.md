# Infisical - 오픈소스 시크릿 관리 플랫폼

- **GitHub**: [Infisical/infisical](https://github.com/Infisical/infisical)
- **언어**: TypeScript
- **오늘의 스타**: ⭐ 62/day
- **태그**: `#보안` `#시크릿관리` `#PKI` `#DevOps`

## 요약

팀/인프라 전체에서 시크릿과 설정을 동기화하고 시크릿 유출을 방지하는 오픈소스 시크릿 관리 플랫폼이다.

**주요 기능:**
- **시크릿 관리**: 대시보드, GitHub/Vercel/AWS 등 동기화, 버전 관리, 특정 시점 복구, 자동 시크릿 로테이션, 동적 시크릿 생성(PostgreSQL, MySQL, RabbitMQ 등)
- **인증서 관리(PKI)**: 내부/외부 CA 통합, Let's Encrypt/DigiCert 등 지원, 인증서 수명주기 관리
- **KMS**: 암호화 키 중앙 관리, 대칭키 기반 데이터 암호화/복호화
- **SSH**: 임시 SSH 인증서 발급으로 안전한 단기 접근

다양한 인증 방식(Kubernetes, GCP, Azure, AWS, OIDC, Universal) 지원.

## Soo에게 의미 있는 이유

Vercel 보안 침해 사건이 보여주듯, 시크릿 관리는 개발 인프라의 핵심이다. AI 에이전트가 외부 API와 상호작용할 때의 시크릿 관리는 AInD 프로젝트에서 반드시 고려해야 할 보안 요소다.
