# 📋 Karpathy-Inspired Claude Code Guidelines

- **저장소**: [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)
- **태그**: `#ClaudeCode` `#프롬프트` `#코드품질` `#Karpathy` 🔥

## 상세 요약

Andrej Karpathy가 지적한 LLM 코딩의 핵심 문제점을 해결하는 **CLAUDE.md 파일 하나**로 Claude Code의 행동을 개선하는 가이드라인이다.

**Karpathy의 문제 진단:**
- "모델이 당신을 대신해 잘못된 가정을 하고 그냥 달려간다"
- "코드와 API를 과도하게 복잡화하고, 추상화를 부풀리고, 죽은 코드를 정리하지 않는다"
- "자기가 충분히 이해하지 못한 주석과 코드를 부수적으로 변경/삭제한다"

**4가지 원칙:**

| 원칙 | 해결하는 문제 |
|------|-------------|
| **Think Before Coding** | 잘못된 가정, 숨긴 혼란, 누락된 트레이드오프 |
| **Simplicity First** | 과도한 복잡성, 부풀린 추상화 |
| **Surgical Changes** | 직교적 편집, 건드리면 안 되는 코드 수정 |
| **Goal-Driven Execution** | 테스트 우선, 검증 가능한 성공 기준 |

각 원칙에 대한 구체적 테스트 기준 포함: "시니어 엔지니어가 이게 과도하게 복잡하다고 말할까? 그렇다면 단순화하라."

## Soo에게 의미 있는 이유

AI 코딩 에이전트의 출력 품질을 체계적으로 관리하는 프레임워크다. R2-D2 같은 코딩 에이전트에 이 원칙을 CLAUDE.md에 적용하면 코드 품질이 크게 개선된다. AInD 컨설팅에서 "에이전트 품질 관리" 가이드의 기초 자료로 활용 가능.
