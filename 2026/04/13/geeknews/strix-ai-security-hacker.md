# strix — 앱의 취약점을 찾아 수정하는 오픈소스 AI 해커

> **출처**: [GitHub (usestrix)](https://github.com/usestrix/strix) | [GeekNews 토론](https://news.hada.io/topic?id=28364)
> **점수**: 28점
> **태그**: `#보안` `#AI에이전트` `#펜테스팅` `#오픈소스`

## 요약

자율 AI 에이전트 방식으로 실제 해커처럼 코드를 실행하고, 취약점을 발견한 뒤 **실제 PoC(개념 증명)로 검증**하는 오픈소스 보안 테스트 도구.

**핵심 차별점:**
- 정적 분석이 아닌 **동적 실행** — 실제로 코드를 돌려서 취약점 확인
- False positive 최소화 — PoC로 검증된 결과만 보고
- 자동 수정(Auto-fix) 기능 포함

**에이전트 툴킷:**
- Full HTTP Proxy (요청/응답 조작)
- 브라우저 자동화 (XSS, CSRF, 인증 플로우 테스트)
- 터미널 환경 (인터랙티브 셸)
- Python 런타임 (커스텀 익스플로잇 개발)
- 코드 분석 (정적 + 동적)

**탐지 범위:**
- 접근 제어 (IDOR, 권한 상승, 인증 우회)
- 인젝션 (SQL, NoSQL, 커맨드 인젝션)
- 서버사이드 (SSRF, XXE, 역직렬화)
- 클라이언트사이드 (XSS, 프로토타입 오염)
- 비즈니스 로직 (레이스 컨디션, 워크플로우 조작)

**Graph of Agents** — 다중 에이전트가 협업하고 발견을 공유하는 분산 워크플로우 지원. GitHub Actions/CI/CD 통합으로 PR마다 자동 스캔 가능.

```bash
curl -sSL https://strix.ai/install | bash
strix --target ./app-directory
```

## Soo에게 의미 있는 이유

AI 에이전트의 보안 분야 적용 사례. "AI가 AI가 만든 코드의 보안을 검증한다"는 패턴이 중요해지고 있다. 바이브 코딩으로 빠르게 코드를 생성할 때 보안 검증을 자동화하는 필수 도구가 될 수 있다.
