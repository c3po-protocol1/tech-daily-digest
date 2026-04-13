# 🔧 GitButler — GitHub 공동창업자가 만든 AI 시대를 위한 Git 재설계

- **출처**: [GeekNews](https://news.hada.io/topic?id=28488) | [gitbutler.com](https://gitbutler.com)
- **태그**: `#Git` `#개발도구` `#AI에이전트` `#a16z` `#투자`

## 상세 요약

GitHub 공동창업자이자 『Pro Git』 저자 Scott Chacon이 이끄는 **GitButler**가 a16z 주도로 **$1,700만 Series A 투자**를 유치했다.

**Scott Chacon의 문제 인식:**
"개발 관행이 Git이 할 수 있는 것에 억지로 맞춰져 온 지 너무 오래됐다. 도구 사이, 사람 사이, 사람과 에이전트 사이에서 컨텍스트가 무너진다."

**핵심 기능:**
- **스택 브랜치**: 브랜치를 계층적으로 관리, 복잡한 작업 흐름을 직관적으로 표현
- **병렬 브랜치**: worktree 없이 여러 브랜치를 동시에 활성 상태로 유지
- **스테이징 제거**: `git add` 없이 바로 작업
- **에이전트 전용 커맨드**: AI 코딩 환경에 최적화된 명령어
- **Agent 탭**: 브랜치별 독립적 Claude Code 세션 실행 가능 (v0.16)

**기술 스택:** Tauri(Desktop) + Svelte+TypeScript(Frontend) + Rust(Backend) + `but` CLI

**통합 지원:** Cursor, Windsurf, Claude Code

**라이선스:** Fair Source License (코드 열람/기여 가능, 2년 후 MIT 전환)

## Soo에게 의미 있는 이유

AI 코딩 에이전트 시대에 Git 인터페이스의 재설계는 필연적이다. 에이전트가 동시에 여러 브랜치에서 작업하는 패턴은 기존 Git 워크플로우로는 불편하다. GitButler의 접근 방식은 AInD 환경에서 버전 관리를 어떻게 해야 하는지에 대한 좋은 참고 사례다.
