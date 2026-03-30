# Harness — Claude Code 에이전트 팀 & 스킬 아키텍트 플러그인

- **출처:** [GitHub - revfactory/harness](https://github.com/revfactory/harness)
- **GeekNews:** [토론](https://news.hada.io/topic?id=27970) · ⬆️ 7 (지속 트렌딩 🔥)
- **태그:** `#ClaudeCode` `#Harness` `#AgentTeams` `#Skills` `#MetaSkill`

---

## 핵심 요약

Claude Code를 위한 **메타 스킬(meta-skill)** — 도메인별 에이전트 팀을 설계하고, 특화된 에이전트를 정의하고, 그들이 사용할 스킬을 생성하는 플러그인.

핵심 개념:
- **메타 스킬:** 다른 스킬을 만드는 스킬. 프로젝트를 분석하고 적절한 에이전트 팀 구성을 자동으로 설계
- **에이전트 팀:** 프론트엔드, 백엔드, 테스팅 등 역할별 에이전트를 정의
- **스킬 생성:** 각 에이전트가 사용할 프로젝트 특화 스킬을 자동 생성

Anthropic의 harness design 글에서 다룬 Planner-Generator-Evaluator 패턴을 **Claude Code 플러그인 형태로 구현**한 것. 지속적으로 GeekNews에서 관심을 받고 있다 🔥.

## Soo에게 의미 있는 이유

우리가 awesome-harness-engineering에서 정리한 이론을 **실제 도구로 구현**한 사례. 특히 "메타 스킬"이라는 개념 — 스킬을 만드는 스킬 — 은 AInD 컨설팅에서 "에이전트 설정의 자동화"를 논할 때 중요한 레퍼런스.
