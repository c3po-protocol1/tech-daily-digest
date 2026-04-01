# 🔥 anthropics/claude-code — Anthropic의 공식 AI 코딩 에이전트

- **GitHub**: [anthropics/claude-code](https://github.com/anthropics/claude-code)
- **언어**: TypeScript
- **태그**: `#AI` `#코딩에이전트` `#CLI` `#Anthropic` `#개발도구`

## 상세 요약

Claude Code는 Anthropic이 만든 터미널 기반 에이전트 코딩 도구다. 코드베이스를 이해하고, 자연어 명령으로 루틴 작업 실행, 복잡한 코드 설명, Git 워크플로우 관리를 처리한다. 터미널, IDE, GitHub에서 @claude 태그로 사용 가능.

**설치 방식 (npm 설치는 deprecated):**
- macOS/Linux: `curl -fsSL https://claude.ai/install.sh | bash` 또는 `brew install --cask claude-code`
- Windows: `irm https://claude.ai/install.ps1 | iex` 또는 `winget install Anthropic.ClaudeCode`

**플러그인 아키텍처:**
공식 레포지토리에 여러 확장 플러그인이 포함되어 있어 커스텀 커맨드와 에이전트 추가 가능.

**소스 유출 사건으로 인해 금주 트렌딩 급상승.** Bun 기반 빌드에서 source map이 NPM에 포함되어 전체 소스가 노출되면서 커뮤니티의 폭발적 관심을 받았다.

## Soo에게 의미 있는 이유

현재 AI 코딩 도구의 사실상 표준 중 하나. 플러그인 아키텍처, CLAUDE.md 메모리 시스템, MCP 통합 등의 설계 패턴은 AInD 실무에서 직접 활용하는 도구이자, 에이전트 아키텍처의 참고 모델이다.
