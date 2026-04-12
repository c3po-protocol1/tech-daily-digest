# Claude Code Pro Max 5x 쿼터, 1.5시간 만에 소진 문제

- **출처**: [GitHub Issue #45756](https://github.com/anthropics/claude-code/issues/45756)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47739260)
- **점수**: 284 points | 208 comments
- **태그**: `#claude-code` `#anthropic` `#quota` `#api-pricing`

## 상세 요약

Anthropic의 Claude Code Pro Max 5x (Opus) 플랜 사용자가 1.5시간 만에 쿼터가 완전히 소진되는 심각한 문제를 보고했다. 이 사용자는 WSL2 환경에서 claude-opus-4-6 (1M 컨텍스트)를 사용 중이었으며, 119,866건의 API 호출 데이터를 분석하여 근본 원인을 밝혀냈다.

### 핵심 발견:
- **Window 1** (5시간, 헤비 개발): 2,715건 API 호출, cache read 1,044M 토큰, output 1.15M 토큰 — 이것은 예상된 소비량
- **Window 2** (1.5시간, 보통 사용): 691건 API 호출, cache read 103.9M 토큰 — 그런데 쿼터 소진

### 근본 원인 추정:
`cache_read` 토큰이 1/10 가격으로 과금되지만, **rate limit(쿼터) 계산에서는 풀 레이트로 카운트**되는 것으로 보인다. 즉, 비용은 할인되지만 쿼터 소비량은 할인되지 않아, 캐시의 쿼터 절감 효과가 무효화되는 상황이다.

사용자는 두 대의 독립적인 머신에서 동일한 현상을 확인했으며, 세션 JSONL 파일의 `usage` 객체를 직접 분석한 상세한 데이터를 제시했다. 이 이슈는 관련 이슈 #46829 (Cache TTL 변경)와 직접 연관된다.

## Soo에게 의미 있는 이유

AInD 컨설팅에서 Claude Code를 핵심 도구로 사용하는 팀에게, 쿼터 관리와 비용 예측은 매우 중요하다. cache_read 토큰이 쿼터에 풀 레이트로 카운트된다면, 대규모 프로젝트에서의 비용 모델링을 재검토해야 한다. 특히 multi-agent 워크플로우에서 여러 세션이 동시에 돌아갈 때 쿼터 소진 속도가 급격히 빨라질 수 있다.
