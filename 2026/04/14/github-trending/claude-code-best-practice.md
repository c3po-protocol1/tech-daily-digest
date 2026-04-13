# 🏆 Claude Code Best Practice — Vibe Coding에서 Agentic Engineering으로

- **저장소**: [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
- **태그**: `#ClaudeCode` `#베스트프랙티스` `#AgenticEngineering` `#워크플로우` 🔥

## 상세 요약

"Vibe Coding에서 Agentic Engineering으로"를 표방하는 Claude Code 종합 가이드다. GitHub Trending #1을 기록했으며, Boris Cherny(Anthropic 엔지니어)의 추천을 받았다.

**체계적 개념 정리:**
- **Subagents**: `.claude/agents/<name>.md` — 자율적 행위자, 격리된 컨텍스트
- **Commands**: `.claude/commands/<name>.md` — 워크플로우 오케스트레이션용 프롬프트 템플릿
- **Skills**: `.claude/skills/<name>/SKILL.md` — 사전 로드/자동 검색 가능한 지식
- **Hooks**: `.claude/hooks/` — 에이전틱 루프 외부에서 실행되는 핸들러
- **MCP Servers**: 외부 도구/DB/API 연결
- **Plugins**: 스킬, 서브에이전트, 훅, MCP를 묶은 배포 가능 패키지

**최신 기능 가이드:**
- **Auto Mode**: 배경 안전 분류기가 수동 권한 프롬프트 대체
- **Agent Teams**: 여러 에이전트가 병렬로 같은 코드베이스에서 작업
- **Ultraplan**: 클라우드에서 계획 초안 → 브라우저 리뷰 → 실행
- **Chrome**: 브라우저 자동화 (웹앱 테스트, 디버그, 데이터 추출)
- **Scheduled Tasks**: `/loop`(로컬 반복), `/schedule`(클라우드 예약)
- **Voice Dictation**: 20개 언어 음성 입력

**오케스트레이션 워크플로우:** Command → Agent → Skill 패턴을 체계적으로 정리.

## Soo에게 의미 있는 이유

Claude Code의 모든 기능을 체계적으로 정리한 가장 포괄적인 가이드다. R2-D2의 작업 방식을 최적화하거나, AInD 컨설팅에서 Claude Code 도입 교육 자료로 직접 활용할 수 있다.
