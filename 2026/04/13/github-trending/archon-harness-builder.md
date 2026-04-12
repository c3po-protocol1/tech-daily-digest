# 🔥 coleam00/Archon — 오픈소스 하네스 빌더

> **GitHub**: [coleam00/Archon](https://github.com/coleam00/Archon)
> **태그**: `#AI코딩` `#워크플로우` `#하네스` `#YAML` `#결정론적`
> 🔥 **2일 이상 연속 트렌딩**

## 요약

**AI 코딩을 결정론적이고 반복 가능하게** 만드는 워크플로우 엔진. Dockerfile이 인프라에, GitHub Actions가 CI/CD에 한 것을 — Archon은 AI 코딩 워크플로우에 한다.

**문제:** AI에게 "이 버그 고쳐"라고 하면, 결과가 모델의 기분에 따라 달라진다. 계획을 건너뛰거나, 테스트를 잊거나, PR 설명을 무시.

**해결:** 개발 프로세스를 YAML 워크플로우로 인코딩. AI는 각 단계에서 지능을 채우되, **구조는 결정론적이고 소유자가 통제**.

```yaml
nodes:
  - id: plan
    prompt: "코드베이스 탐색 후 구현 계획 작성"
  - id: implement
    depends_on: [plan]
    loop:
      prompt: "계획 읽기. 다음 태스크 구현. 검증 실행."
      until: ALL_TASKS_COMPLETE
      fresh_context: true
  - id: run-tests
    depends_on: [implement]
    bash: "bun run validate"    # 결정론적, AI 없음
  - id: approve
    depends_on: [review]
    loop:
      until: APPROVED
      interactive: true         # 인간 승인 게이트
  - id: create-pr
    depends_on: [approve]
    prompt: "변경사항 푸시 후 PR 생성"
```

**핵심 특성:**
- **반복 가능**: 같은 워크플로우, 같은 시퀀스, 매번
- **격리**: 모든 실행이 자체 git worktree — 5개 수정을 병렬 실행 가능
- **Fire & forget**: 워크플로우 시작 후 다른 일 하기. 완성된 PR로 돌아오기
- **조합 가능**: 결정론적 노드(bash, git)와 AI 노드(계획, 코드 생성) 혼합

## Soo에게 의미 있는 이유

하네스 엔지니어링의 실전 도구. "AI 코딩의 불확실성을 YAML로 구조화"하는 접근법은 AInD 컨설팅에서 기업에 AI 코딩 도입을 제안할 때 핵심 도구가 될 수 있다. n8n의 AI 코딩 버전이라는 포지셔닝이 직관적.
