# qmd — 마크다운 문서를 위한 로컬 검색 엔진

- **GitHub**: [tobi/qmd](https://github.com/tobi/qmd)
- **태그**: `#검색` `#마크다운` `#로컬AI` `#에이전트도구`

## 요약

Shopify 창업자 Tobi Lütke가 만든 온디바이스 마크다운 검색 엔진. BM25 전문 검색 + 벡터 시맨틱 검색 + LLM 리랭킹을 결합. Karpathy의 LLM-Wiki에서 권장하는 도구.

### 핵심 기능

- **3단계 검색**: 키워드(BM25) → 시맨틱(벡터) → 하이브리드+리랭킹
- **100% 로컬**: node-llama-cpp + GGUF 모델로 온디바이스 실행
- **컬렉션 관리**: 노트, 미팅 기록, 문서를 별도 컬렉션으로 관리
- **컨텍스트 트리**: 하위 문서 매칭 시 상위 컨텍스트도 함께 반환 — LLM의 맥락 판단 향상
- **에이전트 친화**: `--json`, `--files` 출력, CLI/MCP 서버 지원

### 사용 예

```bash
qmd collection add ~/notes --name notes
qmd embed  # 임베딩 생성
qmd search "project timeline"    # 키워드 검색
qmd vsearch "how to deploy"     # 시맨틱 검색
qmd query "quarterly planning"  # 하이브리드 + 리랭킹
```

## Soo에게 의미 있는 이유

LLM-Wiki, Obsidian 기반 지식 관리 시스템의 핵심 인프라. OpenClaw 에이전트에 통합하면 워크스페이스 내 문서 검색 능력이 대폭 향상. "컨텍스트 트리" 개념은 에이전트의 맥락 이해에 특히 유용.
