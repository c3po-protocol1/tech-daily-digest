# oh-my-codex (OmX) — Codex를 에이전트 팀으로 확장하는 워크플로우 레이어

- **GitHub:** https://github.com/Yeachan-Heo/oh-my-codex
- **스타:** 11,500 ⭐ | **포크:** 1.1K
- **태그:** #codex #agent-team #hooks #workflow #dev-tools

## 상세 요약

OpenAI Codex 위에 구축된 워크플로우 레이어로, 단독 코딩 에이전트를 에이전트 팀으로 확장한다. 훅, HUD, 그리고 "Your codex is not alone"이라는 슬로건이 핵심.

**주요 기능:**
- `$team` 모드: 병렬 코드 리뷰 — 여러 에이전트가 동시에 코드를 검토
- `$ralph` 모드: 아키텍트 수준 검증이 포함된 영구 실행 루프
- 훅 시스템: 에이전트 행동에 대한 가로채기와 확장
- HUD: 에이전트 상태와 작업 진행 상황을 실시간 모니터링
- 미션/스킬/프롬프트 템플릿 시스템

claw-code 프로젝트가 이 도구를 사용해 전체 포팅 세션을 오케스트레이션한 것으로 유명해졌다. Rust crates 구조, 1,204 커밋의 활발한 개발 활동.

## Soo에게 의미 있는 이유

단일 에이전트의 한계를 멀티에이전트 오케스트레이션으로 극복하는 실전 사례다. 특히 $team과 $ralph 모드는 Soo의 에이전트 시스템(R2-D2, Yoda 등)의 협업 패턴에 영감을 줄 수 있다.
