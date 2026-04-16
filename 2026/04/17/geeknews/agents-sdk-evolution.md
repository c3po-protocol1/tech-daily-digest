# Agents SDK의 차세대 진화

- **출처**: [OpenAI](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28578) (6 points)
- **태그**: `#OpenAI` `#에이전트` `#SDK` `#Python`

## 상세 요약

OpenAI가 Agents SDK를 대폭 업데이트하여, 에이전트가 파일 검사·명령 실행·코드 편집·장기 작업을 **제어된 샌드박스 환경**에서 수행할 수 있는 표준 인프라를 제공한다.

### 핵심 신기능
- **Sandbox Agents**: 에이전트가 파일시스템이 있는 컴퓨터 환경에서 실제 작업 수행. 파일 검사, 명령 실행, 패치 적용, 워크스페이스 상태 유지
- **Sessions**: 에이전트 실행 간 자동 대화 이력 관리
- **Human in the Loop**: 에이전트 실행 중 인간 개입을 위한 내장 메커니즘
- **Realtime Agents**: gpt-realtime-1.5와 전체 에이전트 기능을 결합한 음성 에이전트 구축
- **100+ LLM 지원**: 프로바이더 독립적 설계
- **Guardrails**: 입출력 검증을 위한 구성 가능한 안전 검사

### 코드 예시
```python
agent = SandboxAgent(
    name="Workspace Assistant",
    instructions="Inspect the sandbox workspace before answering.",
    default_manifest=Manifest(
        entries={"repo": GitRepo(repo="openai/openai-agents-python", ref="main")}
    ),
)
```

## Soo에게 의미 있는 이유
에이전트 SDK가 "샌드박스 내 실제 작업 수행"이라는 패러다임으로 진화하고 있다. 이는 AInD 컨설팅에서 에이전트 아키텍처 설계의 핵심 참조 구현이 된다.
