# openai/codex-plugin-cc — Codex를 Claude Code에서 사용

- **출처:** [GitHub](https://github.com/openai/codex-plugin-cc)
- **스타:** ★ 699
- **언어:** JavaScript (TypeScript)
- **라이선스:** Apache-2.0
- **태그:** `#OpenAI` `#Codex` `#ClaudeCode` `#CodeReview` `#Plugin` `#MultiModel`

---

## 핵심 요약

OpenAI가 공식 출시한 **Claude Code 플러그인** — Claude Code 안에서 Codex를 사용하여 코드 리뷰나 작업 위임이 가능. 하루 만에 699★으로 가장 많은 관심.

### 제공 기능

| 명령 | 기능 |
|------|------|
| `/codex:review` | 일반 Codex 코드 리뷰 (Codex에서 `/review`와 동일 품질) |
| `/codex:adversarial-review` | 조향 가능한 "챌린지 리뷰" — 의도적으로 까다롭게 검토 |
| `/codex:rescue` | 작업을 Codex에 위임 (백그라운드 실행) |
| `/codex:status` | 위임된 작업 상태 확인 |
| `/codex:result` | 위임된 작업 결과 확인 |
| `/codex:cancel` | 위임된 작업 취소 |

### 설치

```bash
# Claude Code에서 마켓플레이스 추가
/plugin marketplace add openai/codex-plugin-cc
# 플러그인 설치
/plugin install codex
```

### 요구 사항

- ChatGPT 구독 (Free 포함) 또는 OpenAI API 키
- Node.js 18.18 이상
- 사용량은 Codex 사용 한도에 포함

### 왜 이것이 중요한가

**경쟁사(OpenAI) 모델을 경쟁사(Anthropic) 제품 안에서 공식 플러그인으로 사용할 수 있게** 한 것. 업계의 도구 상호운용성 트렌드를 가장 명확하게 보여주는 사례. Harness 엔지니어링의 "최적의 harness가 모델이 훈련된 harness가 아닐 수 있다"는 원칙과 정확히 일치.

`adversarial-review`가 특히 흥미 — Anthropic의 "Evaluator 분리" 패턴을 Codex로 구현한 것. Generator(Claude)와 Evaluator(Codex)를 다른 모델로 분리하여 자기 평가의 관대함 문제를 해결.

## Soo에게 의미 있는 이유

멀티 모델 에이전트 오케스트레이션의 **공식 구현 사례**. 하나의 harness에서 여러 모델을 사용하는 패턴이 업계 표준으로 자리잡고 있다. Holocron이 "source-agnostic" 모니터링을 추구하는 것과 같은 방향. AInD 컨설팅에서 "모델 벤더 록인 없는 에이전트 아키텍처"를 논할 때 핵심 레퍼런스.
