# FFF.nvim — AI 에이전트와 Neovim을 위한 초고속 파일 검색

- **GitHub**: [https://github.com/dmtrKovalenko/fff.nvim](https://github.com/dmtrKovalenko/fff.nvim)
- **태그**: `neovim` `mcp` `file-search` `ai-agents` `developer-tools`

## 상세 요약

FFF(Freakin Fast Fuzzy File Finder)는 AI 에이전트와 Neovim을 위한 퍼지 파일 검색 도구로, 파일 검색에 특화된 성능 중심 도구이다.

### 핵심 가치
- **AI 에이전트용 MCP**: AI 에이전트의 파일 검색 시간과 토큰 소비를 대폭 절감
- **빌트인 메모리**: frecency(빈도+최근성), git status, 파일 크기, 정의 매칭 등 다양한 요인에 기반한 스마트 검색 결과 제공
- **성능**: Linux 커널 리포지토리(10만 파일, 8GB)에서도 빠른 검색

### MCP 연동
```bash
curl -L https://dmtrkovalenko.dev/install-fff-mcp.sh | bash
```
Claude Code, Codex, OpenCode 등에 연결하여 사용. CLAUDE.md에 "use fff" 한 줄만 추가하면 동작.

### Neovim 통합
- grepping, 퍼지 파일 매칭, globbing, multigrepping 지원
- 탁월한 오타 내성(typo-resistant) 경험
- lazy.nvim으로 설치 가능
- Neovim 0.10.0 이상 필요

### Claude Code 내장 도구 대비 성능
빌트인 도구 대비 라운드트립 횟수와 불필요한 파일 읽기를 크게 줄여 토큰 효율성이 훨씬 높음 (차트로 비교 제공).

## Soo에게 의미 있는 이유

AI 코딩 에이전트의 효율성을 높이는 인프라 도구. 에이전트가 파일을 찾는 데 드는 토큰과 시간을 줄이면 전체 코딩 작업의 비용 효율이 크게 향상된다. MCP 기반 도구 생태계의 좋은 사례이기도 하다.
