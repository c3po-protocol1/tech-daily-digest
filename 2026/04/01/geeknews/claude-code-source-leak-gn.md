# Claude Code 소스 코드가 npm 소스맵 파일을 통해 유출 (GeekNews)

- **출처:** [GeekNews](https://news.hada.io/topic?id=28059)
- **원문:** [HN 상세 분석 →](../hackernews/claude-code-source-leak.md)
- **태그:** `#Security` `#NPM` `#Claude` `#SourceLeak`

---

## 핵심 요약

HN에서 1,838점을 기록한 Claude Code 소스 유출 사건의 GeekNews 보도. Anthropic의 Claude Code CLI 소스코드가 npm 레지스트리의 `.map` 파일을 통해 통째로 복원 가능한 형태로 유출.

소스맵 파일은 번들링된 JavaScript를 원본 소스에 매핑하는 디버깅 용도인데, 빌드 파이프라인에서 제거하지 않고 npm에 배포한 것이 원인이다. 유출 후 npm에서 패키지가 pull되었으나 이미 광범위하게 미러링됨.

**발견된 핵심 내부 메커니즘:** anti-distillation(가짜 도구 주입), undercover mode(AI 정체 숨김), frustration regex(사용자 좌절 감지), native client attestation(HTTP 레벨 DRM), KAIROS(미출시 자율 에이전트 모드). 상세 분석은 [HN 기사](../hackernews/claude-code-source-leak.md) 참조.

## Soo에게 의미 있는 이유

npm 배포 시 `.npmignore`나 `files` 필드로 소스맵을 명시적으로 제외해야 하는 기본적 보안 관행의 중요성. AI 코딩 도구의 내부 아키텍처 학습 기회.
