# 🔥 shanraisshan/claude-code-best-practice — Vibe Coding에서 에이전틱 엔지니어링으로

> **GitHub**: [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice)
> **태그**: `#ClaudeCode` `#베스트프랙티스` `#에이전트` `#오케스트레이션`
> 🔥 **2일 이상 연속 트렌딩**

## 요약

Claude Code의 모든 기능을 체계적으로 정리한 **최고의 레퍼런스 가이드**. Boris Cherny(Claude Code 팀)의 팁을 중심으로, Subagents/Commands/Skills/Hooks/MCP/Plugins 등 전체 기능을 다룬다.

**핵심 개념 매핑:**
- **Subagents** (`.claude/agents/<name>.md`): 격리된 컨텍스트의 자율 행위자 — 커스텀 도구, 권한, 모델, 메모리
- **Commands** (`.claude/commands/<name>.md`): 기존 컨텍스트에 주입되는 프롬프트 템플릿
- **Skills** (`.claude/skills/<name>/SKILL.md`): 설정 가능, 자동 검색, 컨텍스트 포킹, 점진적 공개

**오케스트레이션 패턴**: Command → Agent → Skill 체인

**최신 핫 기능:**
- **Ultraplan**: 클라우드에서 계획 초안, 브라우저 리뷰, 인라인 댓글
- **Agent SDK**: Python/TypeScript SDK로 프로덕션 에이전트 구축
- **Auto Mode**: 배경 안전 분류기가 수동 권한 프롬프트 대체
- **Channels**: Telegram, Discord, 웹훅 이벤트를 실행 중 세션에 푸시
- **Voice Dictation**: 20개 언어 Push-to-talk
- **Agent Teams**: 여러 에이전트가 같은 코드베이스에서 병렬 작업

## Soo에게 의미 있는 이유

Claude Code를 100% 활용하기 위한 **바이블**. R2-D2의 능력을 극대화하려면 이 가이드의 패턴들(특히 오케스트레이션 워크플로우, 서브에이전트 구성)을 적용해야 한다.
