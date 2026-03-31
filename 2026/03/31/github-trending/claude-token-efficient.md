# drona23/claude-token-efficient — Claude 출력 토큰 63% 절감

- **출처:** [GitHub](https://github.com/drona23/claude-token-efficient)
- **스타:** ★ 77
- **태그:** `#ClaudeCode` `#TokenEfficiency` `#CLAUDEmd` `#CostOptimization`

---

## 핵심 요약

Claude의 출력 토큰을 **63% 절감**하는 범용 CLAUDE.md. 코드 변경 없이 드롭인 적용 가능.

Claude가 기본적으로 장황하게 출력하는 경향이 있는데, 이 CLAUDE.md 설정 파일이 간결한 출력을 유도하는 지시를 포함. 토큰 비용 절감과 컨텍스트 윈도우 효율화를 동시에 달성.

HumanLayer의 "지시는 적을수록 좋다" 원칙과 다소 긴장 관계 — 토큰 절감을 위한 지시 자체가 컨텍스트를 소모하므로, 실제 효과는 프로젝트에 따라 다를 수 있음.

## Soo에게 의미 있는 이유

비용 최적화가 중요한 고객사에서 참고할 만한 기법. 다만 ETH Zurich 연구에서 보여준 것처럼, CLAUDE.md의 효과는 프로젝트와 작업에 따라 크게 다를 수 있으므로 검증 필요.
