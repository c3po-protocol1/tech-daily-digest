# 🔥 Google Agents CLI — 코딩 에이전트를 에이전트 빌더로 만드는 메타 도구

- **출처**: [GitHub - google/agents-cli](https://github.com/google/agents-cli)
- **GeekNews**: [토론](https://news.hada.io/topic?id=28817) (11P)
- **태그**: `#Google` `#에이전트` `#CLI` `#GeminiCLI` `#ClaudeCode`
- 🔥 2일 이상 연속 트렌딩

## 상세 요약

Google이 Cloud Next에서 공개한 agents-cli는 Gemini CLI, Claude Code, Codex 같은 코딩 에이전트에게 Google Cloud 기반 AI 에이전트를 설계하고 배포하게 해주는 메타 도구(meta-tool)다.

**핵심 개념**: 코딩 에이전트 → 에이전트 빌더. 즉, AI 코딩 도구가 또 다른 AI 에이전트를 만드는 "에이전트의 에이전트" 패턴이다.

**기능**:
- Gemini CLI나 Claude Code 안에서 `agents-cli`를 호출하여 Google Cloud 에이전트를 설계
- Agent Development Kit(ADK) 기반 에이전트 생성
- Vertex AI Agent Engine으로 배포
- 프로젝트 스캐폴딩부터 테스트, 배포까지 전체 워크플로 지원

이는 Google이 AI 에이전트 생태계에서 플랫폼 포지션을 강화하려는 전략의 일환이다. 코딩 에이전트가 어떤 것이든(Gemini, Claude, Codex) Google Cloud 위에서 에이전트를 만들도록 유도하는 구조다.

## Soo에게 의미 있는 이유

"에이전트가 에이전트를 만드는" 메타 도구 패턴은 AInD의 미래 방향을 보여준다. 컨설팅에서 "AI가 개발 프로세스만 바꾸는 것이 아니라, AI 시스템 자체의 구축 방식도 바꾸고 있다"는 메시지를 전달할 때 좋은 사례다.
