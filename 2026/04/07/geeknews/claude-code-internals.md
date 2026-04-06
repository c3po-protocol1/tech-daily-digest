# Claude Code 내부 동작 방식 완전 해부

- **출처**: [Mintlify/VineeTagarwaL 정리본](https://www.mintlify.com/VineeTagarwaL-code/claude-code/concepts/how-it-works)
- **GeekNews**: [topic/28062](https://news.hada.io/topic?id=28062) — 49pts
- **태그**: `#ClaudeCode` `#에이전트아키텍처` `#AgenticLoop`

## 요약

Claude Code의 공식 문서를 기반으로 정리된 내부 동작 방식 해부. Agentic Loop부터 컨텍스트 로딩, 권한 시스템까지 핵심 구조를 설명한다.

### Agentic Loop 6단계

1. 사용자 메시지 입력 (또는 --print / stdin)
2. 시스템 프롬프트 조립 — 현재 날짜, git 상태, CLAUDE.md, 도구 목록
3. Anthropic API 호출 → tool_use 블록 생성
4. 권한 체크 — 자동 승인 / 확인 요청 / 차단
5. 도구 실행 → tool_result로 대화에 추가
6. 추가 도구 호출 또는 최종 응답 — 도구 호출 없을 때까지 반복

### 컨텍스트 구성

- **시스템 컨텍스트**: 현재 브랜치, 최근 5개 커밋, git status(2000자 초과 시 잘림)
- **유저 컨텍스트**: CLAUDE.md(4단계 계층 탐색), 오늘 날짜
- lodash/memoize로 대화 단위 캐싱

### 서브에이전트 (Task 도구)

- 격리된 대화 + 제한 도구셋으로 자체 Agentic Loop 실행
- 로컬(인프로세스) 또는 리모트 컴퓨트에서 실행 가능
- 완료 시 부모 에이전트에 결과 반환

### 쿼리 엔진 역할

- 토큰 스트리밍을 터미널에 실시간 출력
- 턴당 토큰·도구 호출 예산 관리
- 컨텍스트 윈도우 가득 차면 컴팩션 트리거
- maxResultSizeChars 초과 시 임시 파일로 저장, 경로만 전달

## Soo에게 의미 있는 이유

에이전트 아키텍처의 레퍼런스 구현을 이해하는 핵심 자료. 특히 서브에이전트 패턴과 컨텍스트 관리 전략은 OpenClaw 에이전트 운영과 직접 연관된다. AInD 컨설팅에서 "에이전트는 실제로 어떻게 작동하는가"를 구체적으로 설명할 수 있게 해준다.
