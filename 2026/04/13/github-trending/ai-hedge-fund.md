# 🔥 virattt/ai-hedge-fund — AI 헤지펀드 PoC

> **GitHub**: [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund)
> **태그**: `#AI` `#금융` `#멀티에이전트` `#투자` `#교육`
> 🔥 **2일 이상 연속 트렌딩**

## 요약

19개 AI 에이전트가 협업하는 **AI 헤지펀드 개념 증명(PoC)**. 교육/연구 목적이며 실제 거래는 하지 않음.

**에이전트 구성 (실존 투자자 모사):**
- **Aswath Damodaran** — 밸류에이션의 거장
- **Ben Graham** — 가치투자의 아버지, 안전 마진
- **Warren Buffett** — 훌륭한 기업을 합리적 가격에
- **Charlie Munger** — 워런 버핏의 파트너
- **Cathie Wood** — 혁신과 파괴적 성장
- **Michael Burry** — 빅쇼트 역발상 투자자
- **Nassim Taleb** — 블랙 스완, 꼬리 위험, 반취약성
- **Peter Lynch** — 일상에서 "텐배거" 찾기
- **Stanley Druckenmiller** — 매크로 비대칭 기회

**기능 에이전트:**
- Valuation, Sentiment, Fundamentals, Technicals Agent (각각 매매 신호 생성)
- Risk Manager (위험 메트릭 + 포지션 한도)
- Portfolio Manager (최종 거래 결정 + 주문 생성)

CLI와 웹 앱 두 가지 인터페이스 제공.

## Soo에게 의미 있는 이유

멀티에이전트 시스템의 흥미로운 교육용 구현. 각 에이전트가 서로 다른 "성격/전략"으로 동일한 데이터를 분석하는 패턴은, AI 에이전트 오케스트레이션의 좋은 사례. "에이전트에 페르소나를 부여하면 더 다양한 관점을 얻는다"는 접근법.
