# Harness — Claude Code 에이전트 팀 & 스킬 아키텍트 플러그인

- **출처:** [GitHub - revfactory/harness](https://github.com/revfactory/harness)
- **GeekNews:** [토론](https://news.hada.io/topic?id=27970) · ⬆️ 7 (지속 트렌딩 🔥)
- **태그:** `#ClaudeCode` `#Harness` `#AgentTeams` `#Skills` `#MetaSkill` `#Plugin`

---

## 핵심 요약

Claude Code를 위한 **메타 스킬(meta-skill)** 플러그인. "이 프로젝트에 대한 harness를 만들어줘"라고 말하면, 도메인에 맞춘 에이전트 정의(`.claude/agents/`)와 스킬(`.claude/skills/`)을 **자동으로 생성**.

### 6가지 아키텍처 패턴

| 패턴 | 설명 |
|------|------|
| **Pipeline** | 순차 처리 (A → B → C) |
| **Fan-out/Fan-in** | 병렬 분산 후 결과 수집 |
| **Expert Pool** | 전문가 에이전트 풀에서 적합한 에이전트 선택 |
| **Producer-Reviewer** | 생산자 + 검토자 루프 (GAN-inspired) |
| **Supervisor** | 감독 에이전트가 팀 조정 |
| **Hierarchical Delegation** | 계층적 위임 |

### 워크플로우 (6단계)

```
Phase 1: Domain Analysis (도메인 분석)
Phase 2: Team Architecture Design (팀 아키텍처 설계)
Phase 3: Agent Definition Generation (에이전트 정의 생성)
Phase 4: Skill Generation (스킬 생성)
Phase 5: Integration & Orchestration (통합 및 오케스트레이션)
Phase 6: Validation & Testing (검증 및 테스트)
```

### 관련 프로젝트

**harness-100:** 10개 도메인에 걸친 **100개의 프로덕션 준비 에이전트 팀 harness**. 영어/한국어 모두 지원 (200개 패키지). 각 harness에 4~5명의 전문가 에이전트, 오케스트레이터 스킬, 도메인별 스킬 포함. 1,808개 마크다운 파일.

**claude-code-harness (A/B 테스트):** 15개 소프트웨어 엔지니어링 작업에서 **harness 유무에 따른 효과를 통제 실험**으로 측정. 구조화된 사전 설정이 LLM 코드 에이전트 출력 품질에 미치는 영향을 정량적으로 보여줌.

### 핵심 기능

- **Progressive Disclosure 기반 스킬 생성** — 효율적 컨텍스트 관리
- **에이전트 간 데이터 전달, 에러 핸들링, 팀 조정 프로토콜**
- **트리거 검증, 드라이런 테스트, with-skill vs without-skill 비교 테스트**

## Soo에게 의미 있는 이유

awesome-harness-engineering에서 정리한 이론을 **Claude Code 플러그인으로 구현**한 가장 완성된 사례. 한국인 개발자(revfactory)가 만들어 한국어도 지원. A/B 테스트로 harness의 효과를 **정량적으로 증명**한 것이 특히 가치 있다. AInD 컨설팅에서 "harness가 정말 효과가 있는가"에 대한 데이터 기반 답변. 100개 도메인별 harness 템플릿은 "서비스 템플릿으로서의 harness" 비전의 구체적 구현.
