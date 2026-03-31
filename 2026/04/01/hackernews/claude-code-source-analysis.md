# Claude Code 유출 소스 분석: fake tools, frustration regexes, undercover mode

- **출처:** [alex000kim.com](https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/)
- **HN 토론:** [Hacker News](https://news.ycombinator.com/item?id=47599183) · ⬆️ 982
- **태그:** `#AI` `#ClaudeCode` `#SourceAnalysis` `#AgenticArchitecture`

---

## 핵심 요약

Claude Code NPM 소스맵 유출 사건의 후속 분석 글. 유출된 코드를 체계적으로 분석하여 Claude Code의 내부 아키텍처와 숨겨진 메커니즘을 상세히 해부.

발견된 주요 내부 메커니즘:
- **Agentic Loop 구조** — "읽고 → 생각하고 → 도구 쓰고 → 결과 보고"의 루프
- **컨텍스트 로딩 방식** — CLAUDE.md, 프로젝트 파일, 스킬 등의 로딩 순서와 우선순위
- **도구 호출 메커니즘** — 내부적으로 도구를 어떻게 정의하고 호출하는지
- **사용자 승인 흐름** — 위험한 작업에 대한 승인 프로세스

982점으로 세 번째로 높은 관심. AI 코딩 에이전트의 내부를 직접 볼 수 있는 드문 기회.

## Soo에게 의미 있는 이유

Harness 엔지니어링을 공부하면서 "실제로 프로덕션 에이전트는 어떻게 구현되어 있는가"를 알 수 있는 최고의 자료. Anthropic의 공식 문서보다 더 구체적인 구현 세부사항을 보여준다.
