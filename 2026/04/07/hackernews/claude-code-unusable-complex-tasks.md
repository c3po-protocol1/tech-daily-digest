# Claude Code, 2월 업데이트 이후 복잡한 엔지니어링 작업에서 사용 불가

- **출처**: [GitHub Issue #42796](https://github.com/anthropics/claude-code/issues/42796)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47660925)
- **점수**: 667 points
- **태그**: `#ClaudeCode` `#AI에이전트` `#품질저하` `#ExtendedThinking`

## 요약

Claude Code GitHub에 올라온 가장 많은 공감을 받은 이슈(667점)로, stellaraccident(MLIR/IREE 핵심 기여자)가 제출했다. 17,871개의 thinking 블록과 234,760개의 tool call을 분석한 정량적 보고서를 포함한다.

### 정량적 분석 결과

- **분석 대상**: 6,852개 세션 파일, 1~3월 전체 로그
- **핵심 발견**: `redact-thinking-2026-02-12` 롤아웃과 품질 저하가 정확히 일치
  - 3월 5일: 사고(thinking) 편집 1.5% → 3월 8일: 58.4% → 3월 12일+: 99%+ 편집됨
- **행동 변화**: 사고 깊이 감소 시 "연구 우선" → "편집 우선" 패턴으로 이동

### 보고된 증상

1. 지시사항 무시
2. 잘못된 "가장 간단한 수정" 주장
3. 요청의 반대 행동 수행
4. 지시에 반하는 완료 주장

### Extended Thinking이 핵심인 이유

- 시니어 엔지니어링 워크플로에서 extended thinking 토큰은 "있으면 좋은 것"이 아닌 **구조적 필수 요소**
- 다단계 연구, 코딩 컨벤션 준수, 신중한 코드 수정에 thinking 깊이가 직접적으로 필요
- Thinking 제한 → 도구 사용 패턴이 측정 가능하게 변화 → 보고된 품질 문제 발생

## Soo에게 의미 있는 이유

AI 코딩 에이전트의 "보이지 않는 품질 저하" 문제를 정량적으로 증명한 최초의 대규모 분석. AInD 컨설팅에서 "AI 도구의 품질을 어떻게 측정하고 모니터링할 것인가"라는 질문에 대한 구체적 사례로 활용 가능. 또한 thinking 토큰 할당이 비용 최적화 vs 품질의 트레이드오프임을 보여준다.
