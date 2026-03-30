# Harness Design for Long-Running Application Development

- **출처:** [Anthropic](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- **태그:** `#Anthropic` `#GAN` `#MultiAgent` `#Evaluator` `#SprintContract`

---

> 이 글의 전체 상세 요약은 별도 파일에 있습니다:
> **[../ai-engineering/2026-03-30-harness-design-long-running-apps.md](../ai-engineering/2026-03-30-harness-design-long-running-apps.md)**

## 핵심 요약

Anthropic의 harness 시리즈 두 번째 글. GAN에서 영감을 받은 **Planner → Generator → Evaluator** 3-에이전트 아키텍처.

### 두 가지 핵심 문제 해결
1. **Context Anxiety** — 컨텍스트 한계 접근 시 조기 마무리 → Context Reset으로 해결
2. **Self-Evaluation 실패** — 자기 코드를 항상 긍정 평가 → Evaluator 분리로 해결

### 핵심 패턴
- **Sprint Contract** — Generator와 Evaluator가 작업 전 완료 조건을 협상
- **Evaluator가 Playwright MCP로 실제 앱을 테스트** — 스크린샷이 아닌 실제 클릭
- **파일 기반 통신** — 에이전트 간 결과를 파일로 전달

### 모델 진화에 따른 Harness 단순화
- Opus 4.5 → 4.6: Sprint 구조 제거, Context Reset 불필요, Evaluator를 최종 1회로
- **원칙: "harness의 모든 컴포넌트는 모델이 못한다는 가정. 그 가정을 재검증하라."**
