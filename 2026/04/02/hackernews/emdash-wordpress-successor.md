# EmDash — Cloudflare가 만든 WordPress의 정신적 후속작

- **출처**: [Cloudflare Blog](https://blog.cloudflare.com/emdash-wordpress/)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47602832)
- **점수**: 420 points
- **태그**: `#CMS` `#WordPress` `#Cloudflare` `#TypeScript` `#오픈소스`

## 상세 요약

Cloudflare가 WordPress의 "정신적 후속작"으로 EmDash라는 완전히 새로운 CMS를 공개했다. TypeScript로 작성되었으며 MIT 라이선스로 완전 오픈소스다. WordPress 코드를 일절 사용하지 않고 AI 코딩 에이전트를 활용해 2개월 만에 재구축했다.

**핵심 혁신 — 플러그인 보안 문제 해결:**
WordPress 보안 이슈의 96%가 플러그인에서 발생한다. WordPress 플러그인은 DB와 파일시스템에 직접 접근하는 PHP 스크립트인 반면, EmDash 플러그인은 각각 독립된 Dynamic Worker 샌드박스에서 실행된다. 플러그인은 manifest에 명시적으로 선언한 capabilities(예: `read:content`, `email:send`)만 사용 가능하며, 외부 네트워크 접근도 불가능하다.

**x402 내장 결제 시스템:**
모든 EmDash 사이트에 HTTP 402 Payment Required 기반 결제가 내장되어 있다. AI 에이전트 시대에 콘텐츠 제작자가 구독 없이도 콘텐츠에 과금할 수 있는 비즈니스 모델을 기본 제공한다.

**서버리스 아키텍처:**
Cloudflare Workers의 v8 isolate 위에서 완전한 scale-to-zero를 지원한다. 요청이 없으면 비용 제로, 필요 시 즉시 스케일업. Astro 프레임워크 기반으로 프론트엔드 테마를 구성하며, Passkey 인증이 기본이다.

**AI 네이티브 CMS:**
MCP 서버가 내장되어 AI 에이전트가 직접 콘텐츠를 관리할 수 있고, Agent Skills와 CLI를 통해 프로그래밍적으로 사이트를 커스터마이징할 수 있다.

## Soo에게 의미 있는 이유

AInD 컨설팅 관점에서 주목할 세 가지: (1) AI 에이전트로 2개월 만에 WordPress급 CMS를 구축한 사례는 AI 코딩의 생산성을 보여주는 강력한 레퍼런스, (2) MCP/Agent Skills 내장은 "AI-native 소프트웨어"의 구체적 설계 패턴, (3) x402 결제 시스템은 에이전트 경제의 인프라가 되는 새로운 비즈니스 모델이다.
