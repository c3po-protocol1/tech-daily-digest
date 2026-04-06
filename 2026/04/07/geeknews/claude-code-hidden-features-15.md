# Claude Code의 숨겨진 강력한 기능 15가지

- **출처**: [Boris Cherny (제작자) X 스레드](https://x.com/bcherny/status/2038454336355999749)
- **GeekNews**: [topic/28021](https://news.hada.io/topic?id=28021) — 72pts
- **태그**: `#ClaudeCode` `#생산성` `#자동화` `#팁`

## 요약

Claude Code 제작자 Boris Cherny가 직접 정리한 잘 알려지지 않은 강력한 기능들.

### 주요 기능 하이라이트

1. **모바일 앱**: iOS/Android Code 탭에서 노트북 없이 코드 작성
2. **`--teleport`**: 모바일·웹·데스크탑·터미널 간 세션 이동
3. **`/loop` & `/schedule`**: 최대 1주일 자동 반복 작업. PR 관리, Slack 피드백, 코드 리뷰 완전 자동화
4. **Hooks**: 에이전트 라이프사이클에 결정론적 로직 삽입. 권한 요청을 WhatsApp으로 라우팅 가능
5. **Cowork Dispatch**: Desktop 앱의 보안 원격 제어. MCP, 브라우저, 컴퓨터 자원 활용
6. **Chrome 확장**: 프론트엔드 작업 시 브라우저 기반 검증. MCP 대비 더 안정적
7. **세션 포크**: `/branch` 또는 `--resume --fork-session`
8. **`/btw`**: 에이전트 작업 중 사이드 쿼리
9. **Git Worktrees**: `claude -w`로 병렬 작업. `WorktreeCreate` 훅으로 커스텀 가능
10. **`/batch`**: 수십~수천 워크트리 에이전트 병렬 팬아웃. 대규모 코드 마이그레이션
11. **`--bare`**: SDK 시작 속도 최대 10배 향상 (향후 기본값 전환 예정)
12. **`--add-dir`**: 다중 저장소 접근
13. **`--agent`**: `.claude/agents`에 커스텀 에이전트 정의
14. **`/voice`**: 음성 코딩

### 핵심 원칙

> "Claude에게 결과물을 직접 검증할 수단을 제공해야 반복 개선이 가능"

## Soo에게 의미 있는 이유

Claude Code를 활용한 AI 네이티브 개발 워크플로의 실전 가이드. 특히 `/loop`, `/batch`, Hooks는 AInD 컨설팅에서 "AI 에이전트로 무엇이 가능한가"를 데모할 때 강력한 사례가 된다.
