# Vercel 2026년 4월 보안 사고 — 해커 데이터 판매 주장

- **출처**: [BleepingComputer](https://www.bleepingcomputer.com/news/security/vercel-confirms-breach-as-hackers-claim-to-be-selling-stolen-data/)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47824463)
- **HN 점수**: ⭐ 426점
- **태그**: `#보안` `#데이터유출` `#클라우드` `#Vercel`

## 요약

클라우드 개발 플랫폼 Vercel이 내부 시스템에 대한 무단 접근이 발생한 보안 사고를 공식 공개했다. Vercel은 Next.js를 만든 회사로, 서버리스 함수, 엣지 컴퓨팅, CI/CD 파이프라인을 제공하는 플랫폼이다.

**사고 경위:**
- "ShinyHunters"를 자칭하는 해커가 해킹 포럼에 Vercel 데이터 판매 게시글을 올림
- 접근 키, 소스 코드, 데이터베이스 데이터, 내부 배포 및 API 키(NPM, GitHub 토큰 포함) 판매 주장
- 580건의 직원 데이터(이름, Vercel 이메일, 계정 상태, 활동 타임스탬프) 유출
- 내부 Enterprise 대시보드 스크린샷도 공개

**핵심 발견:**
- 보안 침해의 원인은 **제3자 AI 도구의 Google Workspace OAuth 애플리케이션** 침해에서 비롯
- Vercel은 Google Workspace 관리자에게 특정 OAuth 앱 ID 확인을 권고
- 해커는 Vercel과 **200만 달러 몸값** 협상을 진행했다고 주장

**Vercel의 대응:**
- 사고 대응 전문가 투입 및 수사기관 통보
- 고객에게 환경 변수 점검, 민감 환경 변수 기능 사용, 시크릿 교체를 권고
- 서비스 자체는 영향받지 않았다고 발표

## Soo에게 의미 있는 이유

AI 도구의 OAuth 연동이 공격 벡터가 된 사례로, AI 네이티브 개발 환경에서 서드파티 도구 연동 시 보안 검토의 중요성을 보여준다. AInD 컨설팅에서 보안 거버넌스 관련 중요 사례 연구가 될 수 있다.
