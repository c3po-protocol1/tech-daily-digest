# Opus 4.6 vs 4.7 익명 토큰 비용 비교 커뮤니티 리더보드

- **출처**: [Tokenomics](https://tokens.billchambers.me/leaderboard)
- **토론**: [Hacker News](https://news.ycombinator.com/item?id=47816960) (516 points, 509 comments)
- **태그**: `#AI` `#LLM` `#Anthropic` `#pricing`

## 상세 요약

Bill Chambers가 만든 Tokenomics 사이트가 HN에서 516점으로 대히트를 기록했다. 이 사이트는 커뮤니티 사용자들이 익명으로 Anthropic Opus 4.6과 4.7의 요청-토큰 데이터를 비교할 수 있게 해주는 도구다.

핵심 발견 사항:
- **Opus 4.7은 출력 토큰이 4.6보다 훨씬 적음** — 같은 작업에서 더 간결한 응답 생성
- **추론(reasoning) 비용은 4.6→4.7에서 거의 절반으로 하락**
- **입력 토큰 단가는 4.7이 더 높음** — 추론이 많은 작업은 저렴, 추론이 적은 작업은 오히려 비쌀 수 있음
- **Claude Code 같은 실제 워크로드**에서는 입력+추론 비중이 커서 상쇄 효과가 불분명
- **체감 한도 소모 속도**: 한 사용자는 4.6에서 대화당 1-2%이던 5시간 한도 소모가 4.7에서 5%로 증가했다고 보고
- **Artificial Analysis 비교 기준**: 4.7이 4.6보다 약간 저렴, 4.5는 거의 절반 수준

HN 토론에서는 Anthropic의 가격 정책이 "간헐적 보상(intermittent reinforcement)" 방식으로 느껴진다는 비판, effort 설정의 불투명성에 대한 불만, Max 5x 플랜에서도 빠르게 소진되는 한도에 대한 우려가 쏟아졌다.

## Soo에게 의미 있는 이유

AI 코딩 에이전트(Claude Code, Codex 등)를 실제 업무에 도입할 때 비용 관리는 핵심 과제다. Opus 4.7의 토큰 경제학 변화는 "같은 플랜이라도 실제 사용 패턴에 따라 비용이 크게 달라질 수 있음"을 보여주며, AInD 컨설팅에서 클라이언트에게 AI 도구 도입 시 TCO(총소유비용) 분석 방법론을 제시할 때 참고할 만하다.
