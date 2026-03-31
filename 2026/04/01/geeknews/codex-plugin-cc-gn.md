# OpenAI의 Claude Code용 Codex 플러그인 (GeekNews)

- **출처:** [GeekNews](https://news.hada.io/topic?id=28023)
- **GitHub:** [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc) · ★ 699
- **태그:** `#AI` `#OpenAI` `#Codex` `#ClaudeCode` `#Plugin`

---

## 핵심 요약

OpenAI가 Claude Code 안에서 자사의 Codex를 직접 호출할 수 있는 공식 플러그인을 출시. `/codex:review` (일반 리뷰), `/codex:adversarial-review` (도전적 리뷰), `/codex:rescue` (작업 위임) 등 슬래시 커맨드 기반.

경쟁사(Anthropic) 도구에 자사 서비스를 플러그인으로 제공하는 **이례적 전략**. "플랫폼화"보다 **"유비쿼터스 접근"**을 택한 것. `adversarial-review`가 특히 흥미 — Anthropic의 "Evaluator 분리" 패턴을 Codex로 구현. Generator(Claude)와 Evaluator(Codex)를 다른 모델로 분리하여 자기 평가의 관대함 문제 해결.

ChatGPT 구독(Free 포함) 또는 OpenAI API 키 + Node.js 18.18 이상 필요.

## Soo에게 의미 있는 이유

멀티 모델 에이전트 오케스트레이션의 공식 구현 사례. 벤더 록인 없는 에이전트 아키텍처의 구체적 사례.
