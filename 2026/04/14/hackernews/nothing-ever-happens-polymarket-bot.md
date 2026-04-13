# 🤖 Nothing Ever Happens — Polymarket에서 항상 "No"에 베팅하는 봇

- **출처**: [github.com/sterlingcrispin/nothing-ever-happens](https://github.com/sterlingcrispin/nothing-ever-happens)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47753472) (329 points, 152 comments)
- **태그**: `#예측시장` `#트레이딩봇` `#Python` `#Polymarket`

## 상세 요약

"Nothing Ever Happens"는 Polymarket 예측 시장에서 비스포츠 예/아니오 마켓의 "No"(아니오)에 자동으로 베팅하는 비동기 Python 봇이다. "대부분의 극적인 예측은 실현되지 않는다"는 기본 가정에 기반한다.

**기술적 구조:**
- `bot/`: 런타임, 거래소 클라이언트, 대시보드, 복구 시스템, `nothing_happens` 전략
- **3중 안전장치**: `BOT_MODE=live` + `LIVE_TRADING_ENABLED=true` + `DRY_RUN=false` 모두 설정해야 실거래
- 미설정 시 자동으로 `PaperExchangeClient`(모의 거래) 사용
- 라이브 모드에서는 `PRIVATE_KEY`, `DATABASE_URL`, `POLYGON_RPC_URL` 등 추가 필요
- Polygon 블록체인 기반 프록시 월렛 승인 및 리뎀션 지원

**전략 로직:** 독립형 마켓을 스캔하여 설정된 가격 상한선 이하의 "No" 항목을 찾아 매수하고, 오픈 포지션을 추적하며, 대시보드를 통해 상태를 노출한다.

이 프로젝트는 CC0 라이선스(퍼블릭 도메인)로 공개되어 있으며, "오직 엔터테인먼트 목적"이라는 면책 조항이 있다.

## Soo에게 의미 있는 이유

예측 시장 자동화는 AI 에이전트의 실제 금융 응용 사례다. 간단한 규칙 기반 전략이지만, LLM 기반 판단을 결합하면 더 정교한 에이전트 트레이딩이 가능하다. 안전장치 설계(3중 확인)도 AI 에이전트 아키텍처에서 참고할 만한 패턴이다.
