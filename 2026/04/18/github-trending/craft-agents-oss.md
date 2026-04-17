# Craft Agents — Agent Native 소프트웨어 원칙의 비CLI 코딩 에이전트

- **GitHub**: [lukilabs/craft-agents-oss](https://github.com/lukilabs/craft-agents-oss)
- **스타**: ⭐ 4,285 | **언어**: TypeScript
- **태그**: `#AI에이전트` `#코딩도구` `#AgentNative` `#오픈소스`

## 요약

Craft.do 팀이 만든 **비CLI 코딩 에이전트 도구**. Claude Agent SDK와 Pi SDK를 함께 사용하며, Agent Native 소프트웨어 원칙에 기반한 문서 중심 워크플로우를 제공한다.

### 핵심 특징

- **자동 API/서비스 연결**: "add Linear as a source"라고 말하면 에이전트가 공개 API/MCP 서버를 찾아 문서 읽고, 자격증명 설정하고, 구성까지 자동 완료
- **MCP 지원**: JSON 설정 붙여넣기 또는 로컬 MCP 서버(stdio) 지원
- **커스텀 API**: OpenAPI 스펙, URL, 스크린샷 등으로 연결
- **Skills 가져오기**: Claude Code 기존 스킬 원클릭 마이그레이션
- **재시작 불필요**: 모든 변경 즉시 적용
- **자기 자신으로 빌드**: Craft Agents로 Craft Agents를 개발 (코드 에디터 미사용)

### 설치

```bash
curl -fsSL https://agents.craft.do/install-app.sh | bash
```

Apache 2.0 라이선스.

## Soo에게 의미 있는 이유

CLI 기반 코딩 에이전트(Claude Code, Codex)와 다른 접근법을 보여준다. **비개발자도 접근 가능한 UI 중심 에이전트 도구**가 성장하고 있으며, "Agent Native 소프트웨어"라는 개념이 구체화되고 있다.
