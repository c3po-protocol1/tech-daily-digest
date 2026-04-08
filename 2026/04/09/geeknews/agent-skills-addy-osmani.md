# agent-skills — AI 코딩 에이전트를 위한 프로덕션급 엔지니어링 스킬 모음

- **출처:** [github.com/addyosmani](https://github.com/addyosmani/agent-skills)
- **GeekNews:** [topic?id=28294](https://news.hada.io/topic?id=28294) (51 points)
- **태그:** `#AI에이전트` `#코딩` `#개발워크플로우` `#Claude` `#Cursor`

## 상세 요약

Google Cloud AI 디렉터 Addy Osmani가 공개한, AI 코딩 에이전트가 시니어 엔지니어 수준의 워크플로우를 일관되게 따르도록 설계된 19개 스킬 + 7개 슬래시 명령어 시스템.

### 7개 슬래시 명령어 = 개발 생명주기
| 단계 | 명령어 | 원칙 |
|------|--------|------|
| 정의 | /spec | 코드 전에 스펙 |
| 계획 | /plan | 작고 원자적인 태스크 |
| 빌드 | /build | 한 번에 한 슬라이스 |
| 테스트 | /test | 테스트가 증거 |
| 리뷰 | /review | 코드 건강성 개선 |
| 단순화 | /code-simplify | 명확성 > 영리함 |
| 배포 | /ship | 빠를수록 안전 |

### 19개 스킬 체계
- **Define:** idea-refine, spec-driven-development
- **Plan:** planning-and-task-breakdown
- **Build:** incremental-implementation, TDD, context-engineering, frontend-ui-engineering, api-and-interface-design
- **Verify:** browser-testing-with-devtools, debugging-and-error-recovery
- **Review:** code-review-and-quality 등

### 지원 도구
Claude Code(공식 마켓플레이스), Cursor, Gemini CLI, Windsurf, OpenCode, GitHub Copilot, Codex 등 모든 주요 에이전트에서 사용 가능. 스킬이 순수 마크다운이라 시스템 프롬프트를 받는 모든 에이전트에 적용 가능.

### 핵심 설계 철학
각 스킬에 단계별 워크플로우, 검증 게이트, anti-rationalization 테이블(에이전트가 "충분히 좋다"고 합리화하는 것을 방지)이 포함.

## Soo에게 의미 있는 이유
AInD 컨설팅에서 에이전트 기반 개발 프로세스를 표준화할 때 바로 참고할 수 있는 레퍼런스. 특히 anti-rationalization 패턴은 에이전트 품질 보장의 핵심 설계 패턴.
