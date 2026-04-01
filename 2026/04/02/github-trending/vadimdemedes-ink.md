# vadimdemedes/ink — CLI를 위한 React 렌더러

- **GitHub**: [vadimdemedes/ink](https://github.com/vadimdemedes/ink)
- **언어**: TypeScript
- **태그**: `#React` `#CLI` `#터미널UI` `#개발도구` `#프레임워크`

## 상세 요약

Ink는 React를 사용해 CLI 출력을 구축하고 테스트할 수 있게 해주는 프레임워크다. 브라우저의 React와 동일한 컴포넌트 기반 UI 구축 경험을 터미널 앱에 제공한다. Yoga를 사용해 Flexbox 레이아웃을 터미널에서 구현한다.

**사용하는 주요 프로젝트:**
- **Claude Code** — Anthropic의 AI 코딩 도구
- **Gemini CLI** — Google의 AI 코딩 도구
- GitHub Copilot CLI, Canva CLI, Cloudflare Wrangler, Prisma, Gatsby 등

Claude Code와 Gemini CLI 모두 Ink를 사용한다는 점은 현재 AI 코딩 도구의 터미널 UI 표준이 React + Ink임을 보여준다.

## Soo에게 의미 있는 이유

Claude Code 소스 유출에서도 Ink의 최적화 기법(Int32Array 기반 ASCII char pool, 비트마스크 인코딩 스타일 등)이 발견되었다. CLI 도구를 만들 때의 UI 프레임워크 표준으로 자리잡은 기술이며, AI 에이전트 CLI를 직접 만들 때 활용할 수 있다.
