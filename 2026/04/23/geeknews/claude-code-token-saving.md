# Claude Code 및 Codex 설정 변경으로 토큰을 절약하는 방법

- **출처**: [Steady Study Blog](https://www.stdy.blog/increasing-token-efficiency-by-setting-adjustment-in-claude-and-codex/)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28697)
- **점수**: 50점 | 댓글 4개
- **태그**: `#ClaudeCode` `#Codex` `#토큰최적화` `#코딩에이전트`

## 상세 요약

Claude Opus 4.7 출시와 함께 토큰 사용량 증대가 화두가 된 상황에서, 코딩 에이전트의 토큰 효율을 설정 변경만으로 끌어올리는 방법을 체계적으로 정리한 글이다.

**Opus 4.7의 토큰 사용량 변화:**
- 업데이트된 토크나이저로 동일 입력이 **약 1.0~1.35배 더 많은 토큰**으로 매핑
- 높은 effort 레벨에서 더 많이 사고(think)하여 출력 토큰 증가
- 인터랙티브 모드에서 특히 토큰 사용량 증가 (대화 턴마다 추론량 증가)
- 캐싱 TTL이 1시간 → 5분으로 줄어 커뮤니티 불만 폭발

**토큰이 새는 3가지 경로:**
1. 매 세션/턴마다 자동 주입되는 추가 텍스트
2. 대화 히스토리에 남은 너무 긴 툴 호출 출력
3. 검색, 커넥터, IDE 연동 등 외부 연결로 인한 추가 호출

**Claude Code 핵심 설정들:**
1. `includeGitInstructions: false` — Git 관련 시스템 프롬프트 제거, 효과 큼
2. `autoConnectIde: false` — 외부 터미널 실행 시 IDE 자동 연결 비활성화
3. `CLAUDE_CODE_GLOB_NO_IGNORE=false` — .gitignore 파일 Glob 결과 제외
4. 출력 상한 설정:
   - `BASH_MAX_OUTPUT_LENGTH`: bash 출력 최대 문자 수 (기본 30,000)
   - `CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS`: 파일 읽기 최대 토큰 (기본 25,000)
   - `MAX_MCP_OUTPUT_TOKENS`: MCP 도구 출력 최대 토큰 (기본 25,000)
5. 비대화형 모드를 위한 환경변수:
   - `ENABLE_CLAUDEAI_MCP_SERVERS=false`: MCP 서버 비활성화
   - 다양한 플래그로 초기 컨텍스트 주입량 최소화

**트레이드오프 주의:** 출력 상한을 줄이면 에이전트가 잘린 출력을 복구하려 오히려 더 많은 호출을 만들 수 있음. 특히 테스트 요약, 에러 스택트레이스 등 "꼬리" 정보가 잘리면 오진율 증가.

## Soo에게 의미 있는 이유

R2-D2(코딩 에이전트)와 Yoda, C-3PO 모두 Claude 기반으로 동작하므로, 이 설정들은 **직접적인 비용 절감**으로 이어진다. 특히 `includeGitInstructions: false`와 출력 상한 설정은 즉시 적용 가능한 최적화다.
