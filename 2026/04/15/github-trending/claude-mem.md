# thedotmack/claude-mem — Claude Code 영속 메모리 압축 시스템

- **레포**: [github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
- **태그**: #ClaudeCode #메모리 #플러그인 #컨텍스트관리
- 🔥 2일 이상 연속 트렌딩

## 상세 요약

Claude Code 플러그인으로, 코딩 세션 중 Claude가 수행한 모든 작업을 자동으로 캡처하고, AI(Claude Agent SDK 사용)로 압축한 뒤, 미래 세션에 관련 컨텍스트를 자동 주입하는 영속 메모리 시스템이다.

**핵심 기능:**
- 세션 간 컨텍스트 연속성 자동 유지
- AI 기반 메모리 압축으로 토큰 효율 최적화
- 새 세션 시작 시 과거 관련 작업 자동 참조

AGPL 3.0 라이선스, Node.js 18+ 필요, v6.5.0. 30개 이상 언어로 README 번역되어 있어 글로벌 관심이 높다.

## Soo에게 의미 있는 이유

OpenClaw/Yoda가 이미 파일 기반 메모리(MEMORY.md, daily notes)를 사용하고 있지만, claude-mem의 "AI 기반 자동 압축" 접근은 메모리 관리를 한 단계 자동화하는 아이디어를 제공한다.
