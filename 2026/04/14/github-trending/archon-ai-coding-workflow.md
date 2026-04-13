# ⚙️ Archon — AI 코딩을 위한 워크플로우 엔진

- **저장소**: [coleam00/Archon](https://github.com/coleam00/Archon)
- **태그**: `#AI코딩` `#워크플로우` `#자동화` `#YAML`

## 상세 요약

Archon은 AI 코딩 에이전트를 위한 **워크플로우 엔진**이다. "Dockerfile이 인프라에, GitHub Actions가 CI/CD에 한 것을 Archon이 AI 코딩 워크플로우에 한다"는 포지셔닝이다.

**핵심 문제:** AI에게 "이 버그 고쳐줘"라고 하면 결과가 모델의 "기분"에 따라 달라진다. 계획을 건너뛰기도 하고, 테스트를 잊기도 하고, PR 설명을 임의로 작성한다.

**Archon의 해결:** YAML로 개발 프로세스를 정의하면, AI는 각 단계에서 지능을 발휘하되 구조는 결정론적이다.

```yaml
nodes:
  - id: plan
    prompt: "코드베이스를 탐색하고 구현 계획을 작성해"
  - id: implement
    depends_on: [plan]
    loop:
      prompt: "계획을 읽고 다음 작업을 구현해"
      until: ALL_TASKS_COMPLETE
  - id: run-tests
    depends_on: [implement]
    bash: "bun run validate"  # AI 없이 결정론적 실행
  - id: approve
    depends_on: [review]
    loop:
      until: APPROVED
      interactive: true  # 인간 승인 게이트
```

**특징:**
- **반복 가능** — 같은 워크플로우, 같은 순서, 매번
- **격리** — 각 실행마다 자체 git worktree → 5개 수정을 병렬 실행 가능
- **조합 가능** — 결정론적 노드(bash, git)와 AI 노드 혼합
- **이식 가능** — CLI, Web UI, Slack, Telegram, GitHub 어디서든 동일 작동

## Soo에게 의미 있는 이유

AI 코딩에서 "재현성"은 기업 도입의 핵심 장벽이다. Archon은 AI의 창의성과 프로세스의 결정론성을 결합한 좋은 아키텍처 패턴을 보여준다. AInD 컨설팅에서 "AI 코딩 도입 시 품질 보증을 어떻게 하느냐"는 질문에 대한 좋은 답변 사례.
