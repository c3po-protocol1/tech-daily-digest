# 🔥 Claude Code Unpacked — 비주얼 가이드

- **출처:** https://ccunpacked.dev/
- **GeekNews:** https://news.hada.io/topic?id=28094
- **점수:** 18 points (2일 연속 트렌딩)
- **태그:** #claude-code #visualization #architecture #tools

## 상세 요약

Claude Code의 전체 구조와 내부 동작을 시각적으로 분석한 비공식 프로젝트로, 2026년 3월 31일 소스 유출 코드를 기반으로 한다.

**주요 섹션:**

1. **에이전트 루프 (11단계):** 입력 → 메시지 → 히스토리 → 시스템 → API → 토큰 → 도구? → 루프 → 렌더 → 훅 → 대기. 키 입력부터 응답 렌더링까지의 전체 흐름을 단계별로 시각화.

2. **도구 시스템 (47개 도구):**
   - 파일 작업 (6개): FileRead, FileEdit, FileWrite, Glob, Grep, NotebookEdit
   - 실행 (3개): Bash, PowerShell, REPL
   - 검색/가져오기 (4개): WebBrowser, WebFetch, WebSearch, ToolSearch
   - 에이전트/태스크 (11개): AgentSendMessage, TaskCreate/Get/List/Update/Stop/Output, TeamCreate/Delete, ListPeers 등
   - 계획 (5개): EnterPlanMode, ExitPlanMode, EnterWorktree, ExitWorktree, VerifyPlanExecution
   - MCP (4개): mcpList, McpResources, ReadMcpResource, McpAuth
   - 시스템 (11개): AskUserQuestion, TodoWrite, SkillConfig, RemoteTrigger, CronCreate/Delete/List 등
   - 실험적 (8개): Sleep, SendUserMessage, StructuredOutput, LSP, PushNotification, Monitor 등

3. **커맨드 카탈로그 (72개 슬래시 명령어):** 설정/구성(12), 일일 워크플로우(24), 코드 리뷰/Git(13), 디버깅/진단(23), 고급/실험(23)

4. **숨겨진 기능:** Buddy(가상 반려동물), Kairos(세션간 메모리 통합), UltraPlan(30분 실행 윈도우의 Opus급 계획), Coordinator Mode(병렬 워크트리), Bridge(폰/브라우저 원격 세션), Daemon Mode(tmux 백그라운드 실행), UDS Inbox(유닉스 소켓 세션간 통신), Auto-Dream(세션간 학습 정리)

## Soo에게 의미 있는 이유

Claude Code의 내부 구조를 한눈에 파악할 수 있는 최고의 비주얼 레퍼런스다. 특히 숨겨진 기능(Kairos, UltraPlan, Coordinator Mode, Auto-Dream 등)은 아직 출시되지 않은 미래 기능의 방향성을 보여주며, 에이전트 아키텍처 설계에 직접적인 영감을 준다.
