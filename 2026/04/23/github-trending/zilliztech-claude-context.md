# 🔥 zilliztech/claude-context — 코드베이스 전체를 Claude의 컨텍스트로

- **GitHub**: [zilliztech/claude-context](https://github.com/zilliztech/claude-context)
- **태그**: `#MCP` `#ClaudeCode` `#시맨틱검색` `#벡터DB`

## 상세 요약

Claude Code와 다른 AI 코딩 에이전트에 **시맨틱 코드 검색**을 추가하는 MCP 플러그인. 전체 코드베이스를 벡터 데이터베이스에 인덱싱하여 관련 코드만 효율적으로 컨텍스트에 주입한다.

**핵심 기능:**
- 🧠 **전체 코드베이스를 컨텍스트로**: 수백만 줄의 코드에서 시맨틱 검색으로 관련 코드 발견. 다중 라운드 탐색 불필요
- 💰 **대규모 코드베이스에서 비용 효율적**: 매번 디렉토리 전체를 로드하는 대신, 벡터 DB에 저장 후 관련 코드만 사용
- Zilliz Cloud(무료 벡터 DB) + OpenAI 임베딩 모델 사용
- VS Code 확장 및 npm 패키지로도 제공
- Node.js >= 20 필요

**사용법:**
```bash
# Claude Code MCP 설정에 추가
claude mcp add claude-context \
  -e ZILLIZ_CLOUD_API_KEY=your-key \
  -e OPENAI_API_KEY=your-key \
  npx @zilliz/claude-context-mcp
```

대규모 모노리포에서 Claude Code를 사용할 때 컨텍스트 윈도우 한계를 극복하는 실용적 도구.

## Soo에게 의미 있는 이유

R2-D2가 대규모 프로젝트에서 코딩할 때 컨텍스트 부족 문제를 해결할 수 있는 도구. 특히 AInD 컨설팅에서 고객의 기존 코드베이스를 분석/이해하는 데 활용 가능.
