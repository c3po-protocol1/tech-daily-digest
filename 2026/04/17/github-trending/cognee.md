# Cognee — AI 에이전트 메모리를 위한 지식 엔진

- **리포**: [topoteretes/cognee](https://github.com/topoteretes/cognee)
- **언어**: Python
- **⭐ Today**: 156 stars
- **태그**: `#AI` `#메모리` `#지식그래프` `#RAG` `#에이전트`

## 상세 요약

AI 에이전트를 위한 **개인화된 동적 메모리**를 구축하는 오픈소스 지식 엔진. 6줄의 코드로 에이전트에 메모리를 추가할 수 ���다.

### 핵심 기능
- 벡터 검색 + 그래프 데이터베이스 + 인지 과학 접근법 결합
- 어떤 형식/구조의 데이터든 수집 가능
- 의미 기반 검색 + 관계 기반 연결 동시 지원
- 데이터 변화와 진화에 따라 지속적 학습
- OpenClaw 플러그인, Claude Code 플러그인 제공

### 사용 예시
```python
import cognee
await cognee.add("data_directory")
await cognee.cognify()
results = await cognee.search("query")
```

## Soo에게 의미 있는 이유
에이전트 메모리는 AInD의 핵심 인프라. Cognee는 RAG를 넘어 "지식이 연결되고 진화하는" 메모리 시스템을 구현하며, 에이전트의 장기적 학습 능력을 실현하는 좋은 참조 구현이다.
