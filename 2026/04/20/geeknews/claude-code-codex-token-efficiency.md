# Claude Code 및 Codex 설정 변경으로 토큰을 절약하는 방법

- **출처**: [Steady Study Blog](https://www.stdy.blog/increasing-token-efficiency-by-setting-adjustment-in-claude-and-codex/)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28697)
- **포인트**: 1점 (신규 등록)
- **태그**: `#ClaudeCode` `#Codex` `#토큰효율` `#개발도구`

## 요약

Claude Opus 4.7 출시로 토큰 사용량이 약 1.5배 증가한 상황에서, Claude Code와 Codex의 설정을 조정하여 토큰 효율을 높이는 실전 가이드.

**토큰이 소모되는 3가지 경로:**
1. 매 세션/매 턴 자동으로 붙는 추가 텍스트
2. 대화 히스토리에 남은 너무 긴 툴 호출 출력
3. 검색, 커넥터, IDE 연동으로 인한 추가 호출

**Claude Code 핵심 설정:**
- `includeGitInstructions: false` — git 관련 지시문 제거
- `autoConnectIde: false` — IDE 자동 연결 비활성화
- `CLAUDE_CODE_GLOB_NO_IGNORE=false` — .gitignore 파일 검색 결과 제외
- 출력 상한 설정: `BASH_MAX_OUTPUT_LENGTH`, `CLAUDE_CODE_FILE_READ_MAX_OUTPUT_TOKENS`
- 비대화형 모드 최적화: `--tools`, `--strict-mcp-config`, `--disable-slash-commands` 등

**실전 alias 예시:**
```bash
alias ccb='ENABLE_CLAUDEAI_MCP_SERVERS=false CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 CLAUDE_CODE_DISABLE_CLAUDE_MDS=1 claude --tools "Bash,Edit,Glob,Grep,Read,Write" --disable-slash-commands'
```

**Codex 설정:** `features.apps: false`, `web_search: disabled`, `tool_output_token_limit` 조정

## Soo에게 의미 있는 이유

코딩 에이전트의 실질적인 비용 최적화 가이드로, AI 코딩 도구를 실무에서 쓸 때 필수 참고자료. AInD 컨설팅에서 고객사에 AI 개발 도구 도입 시 비용 관리 방법론으로 활용 가능.
