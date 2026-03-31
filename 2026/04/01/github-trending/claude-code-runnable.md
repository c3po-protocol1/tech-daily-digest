# claude-code-best/claude-code — Claude Code 실행 가능 버전

- **출처:** [GitHub](https://github.com/claude-code-best/claude-code)
- **스타:** ★ 1,059
- **언어:** TypeScript
- **태그:** `#ClaudeCode` `#Runnable` `#TypeScript` `#Bun`

---

## 핵심 요약

유출된 Claude Code 소스를 **실제로 실행 가능하도록** 수정한 프로젝트. 1,059★. TypeScript 타입 에러를 전체 수정하고, lock 파일 보존으로 의존성 무결성을 보장하며, `bun i && bun run dev`로 즉시 실행 가능.

원본 소스맵에서 복원된 코드는 타입 에러와 누락된 의존성으로 인해 바로 실행이 불가능했다. 이 프로젝트는 그 간극을 메워 **연구와 학습 목적으로 실제 동작하는 Claude Code를 로컬에서 실행**할 수 있게 한다.

"기업급 신뢰성"과 "안전 무독"을 강조 — 악성 코드 주입 없이 원본에 충실한 실행 가능 버전을 목표.

## Soo에게 의미 있는 이유

실제 동작하는 에이전트를 로컬에서 분석할 수 있다는 것은 harness 엔지니어링 학습에 최고의 환경. 디버거를 붙여서 에이전틱 루프의 각 단계를 추적할 수 있음.
