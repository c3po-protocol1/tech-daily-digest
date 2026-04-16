# OpenAI Agents SDK (Python) — 멀티 에이전트 워크플로우 프레임워크

- **리포**: [openai/openai-agents-python](https://github.com/openai/openai-agents-python)
- **언어**: Python
- **⭐ Today**: 110 stars
- **��그**: `#OpenAI` `#에이전트` `#Python` `#SDK`

## 상세 ��약

OpenAI의 공식 **멀티 에이전트 워크플로우 프레임워크**. 경량이지만 강력한 에이전트 시스템을 구축할 수 있다. 100+ LLM 프로바이더를 지원하는 프로바이더 독립적 설계.

### 핵심 개념
- **Agents**: 지시사항, 도구, 가드레일, 핸드오프가 설정된 LLM
- **Sandbox Agents**: 컨테이너에서 실제 작업을 수행하는 에이전트 (v0.14.0 신규)
- **Agents as Tools / Handoffs**: 특정 작업을 다른 에이전트에 위임
- **Tools**: 함수, MCP, 호스팅 도구 등 다양한 도구
- **Guardrails**: 입출력 검증을 위한 안전 검사
- **Human in the Loop**: 인간 개입 메커니즘
- **Sessions**: 자동 대화 이력 관리
- **Tracing**: 에이전트 실행 추적/디버그/최적화
- **Realtime Agents**: gpt-realtime-1.5 기반 음성 에이전트

### Sandbox Agent 예시
```python
agent = SandboxAgent(
    name="Workspace Assistant",
    default_manifest=Manifest(
        entries={"repo": GitRepo(repo="openai/openai-agents-python", ref="main")}
    ),
)
result = Runner.run_sync(agent, "Inspect the repo README and summarize.")
```

## Soo에게 의미 있는 이유
OpenAI의 에이전트 SDK가 빠르게 진화하며 "에이전트 오케스트레이션의 표준"을 형성하고 있다. AInD 컨설팅에서 에이전트 프레임워크 선택과 아키텍처 설계의 핵심 참조점이다.
