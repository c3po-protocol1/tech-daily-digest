# Anthropic, 캐시 TTL을 조용히 1시간→5분으로 변경 (비용 20-32% 증가)

> **출처**: [GitHub Issue #46829](https://github.com/anthropics/claude-code/issues/46829) | [HN 토론](https://news.ycombinator.com/item?id=47736476)
> **점수**: 452점
> **태그**: `#AI` `#Anthropic` `#Claude` `#비용최적화` `#API`

## 요약

한 사용자가 2026년 1월~4월 간 119,866개의 Claude Code API 호출을 분석하여, Anthropic이 **3월 6일경 프롬프트 캐시 TTL을 1시간에서 5분으로 조용히 변경**했음을 밝혀냈다. 두 대의 독립 머신(Linux 워크스테이션 + Windows 노트북, 서로 다른 계정)에서 동일한 패턴이 확인되었다.

**Phase별 분석:**
- **Phase 1** (1/11~1/31): 5분 TTL만 존재 (1시간 TTL 미출시 시기)
- **Phase 2** (2/1~3/5): **1시간 TTL**만 사용됨. 33일 연속 양쪽 머신에서 일관됨
- **Phase 3** (3/6~현재): 다시 5분 TTL로 회귀. 1시간 토큰이 사라짐

이 변경으로 인해:
- 캐시 생성 비용 **20~32% 증가**
- 구독 사용자의 쿼터 소비량 급증 (이전에 한 번도 한도에 도달하지 않았던 사용자까지 영향)
- `ephemeral_5m_input_tokens`와 `ephemeral_1h_input_tokens` 필드를 통해 API 응답에서 직접 관찰 가능

Issue는 "not planned"으로 닫혔지만, 커뮤니티에서는 API 비용 투명성과 캐시 정책 변경의 사전 고지 필요성에 대한 논의가 활발하다.

## Soo에게 의미 있는 이유

AInD 컨설팅에서 LLM API 비용 관리는 핵심 과제다. **캐시 TTL 변경만으로 비용이 20-32% 급증**할 수 있다는 것은 API 의존 서비스의 비용 예측 불확실성을 보여준다. JSONL 파일을 직접 분석해 비용 변동을 추적하는 방법론도 참고할 만하다. Claude Code를 사용하는 팀이라면 반드시 알아야 할 이슈.
