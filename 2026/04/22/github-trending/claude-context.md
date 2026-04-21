# Claude Context - 코드베이스 전체를 Claude의 컨텍스트로

- **GitHub**: [zilliztech/claude-context](https://github.com/zilliztech/claude-context)
- **언어**: TypeScript
- **오늘의 스타**: ⭐ 259/day
- **태그**: `#MCP` `#ClaudeCode` `#시맨틱검색` `#벡터DB`

## 요약

Zilliz(Milvus 개발사)가 만든 MCP 플러그인으로, Claude Code 및 기타 AI 코딩 에이전트에 시맨틱 코드 검색 기능을 추가한다.

**핵심 가치:**
- **전체 코드베이스를 컨텍스트로**: 수백만 줄의 코드에서 시맨틱 검색으로 관련 코드를 찾아 Claude 컨텍스트에 바로 제공. 다중 라운드 탐색 불필요
- **비용 효율적**: 전체 디렉토리를 Claude에 로드하는 대신, 벡터 데이터베이스에 코드를 저장하고 관련 코드만 컨텍스트에 포함하여 비용 절감

**설정 방법:**
```bash
claude mcp add claude-context \
  -e OPENAI_API_KEY=sk-your-key \
  -e MILVUS_TOKEN=your-token \
  -- npx @zilliz/claude-context-mcp@latest
```

Zilliz Cloud의 벡터 DB + OpenAI 임베딩 모델을 사용하며, VS Code 확장도 지원한다.

## Soo에게 의미 있는 이유

MCP(Model Context Protocol) 생태계가 빠르게 성장하고 있음을 보여주는 도구다. 대규모 코드베이스에서 AI 코딩 에이전트의 효율성을 높이는 핵심 인프라로, AInD 프로젝트에서 활용 가능성이 높다.
