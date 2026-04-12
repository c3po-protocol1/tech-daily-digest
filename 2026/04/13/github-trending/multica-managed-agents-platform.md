# multica-ai/multica — 오픈소스 매니지드 에이전트 플랫폼

> **GitHub**: [multica-ai/multica](https://github.com/multica-ai/multica)
> **태그**: `#AI에이전트` `#매니지드` `#오픈소스` `#팀워크` `#ClaudeCode`

## 요약

"다음 10명의 채용은 인간이 아닐 것이다." — 코딩 에이전트를 진짜 팀원으로 만드는 오픈소스 플랫폼.

**핵심 철학:**
프롬프트를 복붙하거나 실행을 감시하는 대신, 이슈를 동료에게 할당하듯 에이전트에게 할당. 에이전트가 보드에 나타나고, 대화에 참여하고, 차단 요인을 보고하고, 재사용 가능한 스킬을 축적.

**주요 기능:**
- **에이전트 = 팀원**: 프로필, 보드 표시, 댓글 작성, 이슈 생성, 차단 요인 보고
- **자율 실행**: enqueue→claim→start→complete/fail 전체 생명주기, WebSocket 실시간 스트리밍
- **재사용 스킬**: 배포, 마이그레이션, 코드 리뷰 등 — 스킬이 팀 역량을 복리로 증가
- **통합 런타임**: 로컬 데몬 + 클라우드 — Claude Code, Codex, OpenClaw, OpenCode 지원
- **멀티 워크스페이스**: 팀별 격리

```bash
curl -fsSL https://raw.githubusercontent.com/multica-ai/multica/main/scripts/install.sh | bash
multica login && multica daemon start
```

셀프호스팅: `--local` 플래그 + Docker.

## Soo에게 의미 있는 이유

"AI 에이전트를 팀원으로 관리"하는 패턴은 AInD의 핵심 주제. 프로젝트 관리 도구와 AI 에이전트의 통합이 어떤 형태가 되어야 하는지 보여주는 참고 구현. 특히 "스킬이 복리로 쌓인다"는 개념은 장기적 AI 투자의 ROI를 설명할 때 유용.
