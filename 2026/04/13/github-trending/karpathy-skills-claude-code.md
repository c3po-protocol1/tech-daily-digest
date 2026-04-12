# 🔥 forrestchang/andrej-karpathy-skills — Karpathy 원칙 기반 Claude Code 가이드라인

> **GitHub**: [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)
> **태그**: `#ClaudeCode` `#CLAUDE.md` `#코드품질` `#베스트프랙티스`
> 🔥 **2일 이상 연속 트렌딩**

## 요약

Andrej Karpathy가 지적한 LLM 코딩의 문제점을 해결하는 단일 `CLAUDE.md` 파일.

**Karpathy가 지적한 문제:**
> "모델이 당신을 대신해 잘못된 가정을 하고 그냥 달려간다. 혼란을 관리하지 않고, 명확화를 구하지 않고, 불일치를 드러내지 않고, 트레이드오프를 제시하지 않고, 반론을 제기하지 않는다."
> "코드와 API를 과도하게 복잡하게 만들고, 추상화를 비대하게 하고, 데드 코드를 정리하지 않는다... 100줄이면 될 것을 1000줄로 구현한다."

**4가지 원칙:**
1. **Think Before Coding** — 가정을 명시하고, 혼란 시 멈추고, 트레이드오프 제시
2. **Simplicity First** — 요청받지 않은 기능/추상화/유연성 금지. 200줄이 50줄이 될 수 있으면 다시 쓰기
3. **Surgical Changes** — 직접 관련 없는 코드/주석/포맷 건드리지 않기. 모든 변경 라인이 사용자 요청으로 추적 가능해야 함
4. **Goal-Driven Execution** — "검증 추가" → "유효하지 않은 입력 테스트를 쓰고, 통과시키기"로 변환

각 원칙에 "시니어 엔지니어라면 이게 과하다고 할까?" 같은 **검증 테스트** 포함.

## Soo에게 의미 있는 이유

CLAUDE.md 작성의 베스트 프랙티스. R2-D2의 코드 품질을 높이기 위한 즉시 적용 가능한 가이드라인. 특히 "Surgical Changes" 원칙은 AI 에이전트가 관련 없는 코드를 건드리는 가장 흔한 문제를 해결한다.
