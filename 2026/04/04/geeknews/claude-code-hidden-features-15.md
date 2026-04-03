# Claude Code의 숨겨진 강력한 기능 15가지

- **출처**: [https://x.com/bcherny/status/2038454336355999749](https://x.com/bcherny/status/2038454336355999749)
- **GeekNews**: [https://news.hada.io/topic?id=28021](https://news.hada.io/topic?id=28021)
- **점수**: 70 points
- **태그**: `claude-code` `tips` `developer-tools` `productivity`

## 상세 요약

Claude Code 제작자 Boris Cherny가 잘 알려지지 않은 Claude Code의 강력한 기능 15가지를 정리하여 공개했다.

### 핵심 기능 요약

1. **모바일 앱**: iOS에서 Claude Code 사용 가능
2. **자동 스케줄링**: Claude가 작업을 자동으로 예약
3. **세션 포크(/branch)**: `/branch` 명령 또는 `claude --resume --fork-session`으로 기존 세션 분기
4. **/btw — 사이드 쿼리**: 에이전트 작업 중 빠른 질문을 던지는 기능
5. **Git Worktrees**: `claude -w`로 워크트리 세션 시작, 병렬 작업 시 필수
6. **/batch — 대규모 병렬 팬아웃**: 수십~수천 개 워크트리 에이전트에 작업 분산 (대규모 코드 마이그레이션에 유용)
7. **--bare 플래그**: SDK 시작 속도 최대 10배 향상 (CLAUDE.md, 설정, MCP 자동 탐색 스킵)
8. **--add-dir — 다중 저장소 접근**: 추가 폴더에 대한 접근 권한 부여
9. **--agent — 커스텀 에이전트**: `.claude/agents` 디렉토리에 에이전트 정의
10. **/voice — 음성 입력**: CLI에서 스페이스바 홀드로 음성 코딩
11. **Chrome/Edge 확장 프로그램**: 웹 코드 작업 시 MCP 대비 안정적
12. **Claude Desktop 앱**: 웹 서버 자동 실행 및 내장 브라우저 테스트
13. **프롬프트 반복 작성**: 결과가 좋아질 때까지 반복
14. **Compute-use MCP**: `/mcp`로 들어가면 사용 가능
15. **Teleport**: 세션 관련 기능

### 커뮤니티 반응
- `/voice` 모드는 한국어에서 기본 음성 키보드보다 못함
- `/btw`를 키보드에 맵핑하고 싶다는 요청
- PC간 세션 이어받기(teleport) 기능에 대한 관심

## Soo에게 의미 있는 이유

Claude Code를 실제로 활용하고 있다면 워크플로를 크게 개선할 수 있는 팁 모음. 특히 /batch(대규모 병렬 처리), --bare(속도 최적화), Git Worktrees(병렬 작업) 등은 에이전트 기반 개발의 생산성을 크게 높일 수 있는 기능이다.
