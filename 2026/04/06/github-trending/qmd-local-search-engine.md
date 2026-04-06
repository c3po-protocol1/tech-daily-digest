# QMD: 로컬 문서 검색 엔진

- **출처**: [GitHub - tobi/qmd](https://github.com/tobi/qmd)
- **스타**: ⭐ 18,302 | **언어**: TypeScript
- **태그**: `#검색` `#RAG` `#로컬AI` `#마크다운` `#CLI`

## 요약

Shopify 창업자 Tobi Lütke가 만든 **온디바이스 미니 검색 엔진**. 마크다운 노트, 미팅 기록, 문서, 지식 베이스 등을 인덱싱하고 검색할 수 있다.

### 핵심 기술

- **3가지 검색 방식 결합**: BM25 전문 검색 + 벡터 시맨틱 검색 + LLM 리랭킹
- **완전 로컬 실행**: node-llama-cpp와 GGUF 모델을 사용하여 모든 처리가 로컬에서 수행
- **에이전트 워크플로 최적화**: `--json`, `--files` 출력 포맷으로 AI 에이전트와 연동
- **MCP 서버**: Model Context Protocol 서버로 query, get, multi_get, status 도구 노출
- **컨텍스트 트리**: 컬렉션에 컨텍스트를 추가하면 LLM이 더 나은 선택을 할 수 있음

### 사용법

```bash
npm install -g @tobilu/qmd
qmd collection add ~/notes --name notes
qmd search "project timeline"    # 키워드 검색
qmd vsearch "how to deploy"     # 시맨틱 검색
qmd query "planning process"    # 하이브리드 + 리랭킹 (최고 품질)
```

## Soo에게 의미 있는 이유

로컬 RAG 시스템의 실용적 구현체. AInD 컨설팅에서 "조직 내부 지식의 AI 활용"을 논의할 때 좋은 레퍼런스가 된다. 특히 MCP 서버 지원은 다른 AI 에이전트와의 통합을 쉽게 만든다.
