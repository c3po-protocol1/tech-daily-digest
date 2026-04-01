# Claude Code 내부 동작 방식 완전 해부 — Agentic Loop부터 컨텍스트 로딩까지

- **출처**: [Mintlify 문서](https://www.mintlify.com/VineeTagarwaL-code/claude-code/concepts/how-it-works)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28062)
- **태그**: `#ClaudeCode` `#아키텍처` `#에이전트루프` `#컨텍스트` `#MCP`

## 상세 요약

Claude Code의 내부 아키텍처를 체계적으로 정리한 기술 문서다. 유출된 소스를 기반으로 핵심 동작 메커니즘을 문서화했다.

**Agentic Loop:**
Claude가 추론하여 도구를 선택 → 도구 실행 → 결과 반환의 반복 루프로 동작한다. 각 턴에서 토큰 예산과 도구 호출 횟수 제한을 적용하며, 컨텍스트 윈도우가 가득 차면 자동 compaction을 트리거한다.

**컨텍스트 로딩 (세션 시작 시):**
1) Git 상태 — 현재 브랜치, 기본 브랜치, git status, 최근 5개 커밋
2) CLAUDE.md 메모리 — 4단계 계층(managed → user → project → local) 탐색
3) 현재 날짜 주입
4) 캐시 무효화 문자열 (디버깅용)

**도구 실행 모델:**
- Interactive(REPL) 모드와 Non-interactive(task/print) 모드 구분
- Sub-agents는 Task 도구를 통해 독립 컨텍스트에서 실행
- 대화 기록은 디스크에 저장되며 세션 재개 시 전체 메시지 히스토리를 로드

**쿼리 엔진:**
스트리밍 토큰 출력, tool_use 블록 디스패치, 턴당 토큰/도구 호출 예산 적용, 도구 결과 수집 및 다음 모델 호출 전 추가, 컨텍스트 윈도우 가득 차면 compaction 실행.

## Soo에게 의미 있는 이유

AI 코딩 에이전트를 설계할 때 참고할 수 있는 구체적인 아키텍처 문서다. Agentic loop, 컨텍스트 관리, 세션 영속성 등의 설계 패턴은 자체 AI 에이전트 시스템 구축 시 직접 적용 가능한 지식이다.
