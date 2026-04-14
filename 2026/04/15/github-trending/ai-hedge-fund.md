# 🔥 virattt/ai-hedge-fund — AI 기반 헤지펀드 PoC

- **레포**: [github.com/virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)
- **태그**: #AI #금융 #멀티에이전트 #투자
- 🔥 2일 이상 연속 트렌딩

## 상세 요약

AI 에이전트가 투자 결정을 내리는 헤지펀드의 개념 증명(PoC) 프로젝트다. 교육/연구 목적이며 실제 거래는 수행하지 않는다.

**19개 에이전트 시스템:**
- 유명 투자자 에이전트: Buffett, Munger, Damodaran, Graham, Ackman, Cathie Wood, Burry, Pabrai, Taleb, Lynch, Fisher, Jhunjhunwala, Druckenmiller
- 분석 에이전트: Valuation(내재가치 계산), Sentiment(시장 심리), Fundamentals(기본 분석), Technicals(기술 분석)
- Risk Manager(리스크 지표 + 포지션 한도)
- Portfolio Manager(최종 트레이딩 결정 + 주문 생성)

각 에이전트가 자신만의 투자 철학에 따라 분석하고, Portfolio Manager가 최종 판단을 내리는 멀티에이전트 아키텍처.

## Soo에게 의미 있는 이유

멀티에이전트 시스템의 실용적 구현 사례다. 특히 서로 다른 페르소나/전략을 가진 에이전트들이 협력하는 구조는 AInD에서 멀티에이전트 아키텍처를 설계할 때 참고할 만하다.
