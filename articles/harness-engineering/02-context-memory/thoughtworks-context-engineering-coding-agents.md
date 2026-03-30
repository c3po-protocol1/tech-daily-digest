# Context Engineering for Coding Agents

- **출처:** [Thoughtworks / Martin Fowler](https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html)
- **태그:** `#Thoughtworks` `#Grounding` `#CodingAgents`

---

## 핵심: "기반 유지(Grounding)"

코딩 에이전트의 품질은 모델 능력보다 **에이전트가 프로젝트의 실제 상태를 얼마나 정확히 파악하고 있느냐**에 더 많이 좌우된다. 이것이 "grounding"이다.

**Grounded 에이전트:** 파일 구조, 기존 패턴, 의존성, 테스트 상태를 정확히 이해하고 코딩
**Ungrounded 에이전트:** 프로젝트 맥락 없이 일반적인 "좋은 코드"를 생성 → 기존 코드와 충돌

## 실용적 접근

1. **리포 구조 문서화** — AGENTS.md, ARCHITECTURE.md로 프로젝트 맥락 제공
2. **관련 파일 자동 발견** — 작업 전 관련 코드를 자동 탐색
3. **테스트 피드백 루프** — 코드 작성 → 테스트 → 결과를 컨텍스트에 포함 → 수정
4. **점진적 컨텍스트 구축** — 한 번에 모든 것을 넣지 않고, 작업 진행에 따라 확장

## Soo에게 의미 있는 이유

"AI 코딩 도구의 결과가 왜 일관적이지 않은가"에 대한 답. Grounding의 수준이 결과 품질을 결정한다.
