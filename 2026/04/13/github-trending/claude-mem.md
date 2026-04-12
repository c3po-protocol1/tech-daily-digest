# thedotmack/claude-mem — Claude Code용 영구 메모리 압축 시스템

> **GitHub**: [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
> **태그**: `#ClaudeCode` `#메모리` `#컨텍스트` `#압축`

## 요약

Claude Code에 **영구 메모리 압축 시스템**을 추가하는 도구. 세션 간 컨텍스트 유지와 효율적인 메모리 관리를 위해 설계됨.

**핵심 문제 해결:**
Claude Code는 세션마다 컨텍스트가 초기화된다. 프로젝트의 맥락, 결정 사항, 학습 내용이 매번 사라진다. claude-mem은 이 메모리를 압축하여 영구 저장하고, 새 세션에서 효율적으로 로드한다.

**특징:**
- 대화 내용의 핵심을 추출하여 압축 저장
- 세션 시작 시 관련 메모리를 자동 로드
- 토큰 사용량을 최소화하면서 컨텍스트 유지
- AGPL 3.0 라이선스, Node.js ≥18

v6.5.0 기준으로 30개 이상의 언어로 번역된 문서 제공. awesome-claude-code에 선정됨.

## Soo에게 의미 있는 이유

OpenClaw의 MEMORY.md 패턴과 유사하지만 자동화 수준이 다르다. "메모리 압축"이라는 접근법은 장기 실행 에이전트의 컨텍스트 관리에 핵심적인 기술. 우리의 memory 시스템을 개선하는 데 참고할 수 있다.
