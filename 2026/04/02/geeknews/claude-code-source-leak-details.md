# Claude Code 소스 유출: 가짜 도구, 욕설 감지, 은폐 모드 등 내부 구조 상세 분석

- **출처**: [Alex Kim Blog](https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28074)
- **태그**: `#ClaudeCode` `#보안` `#소스유출` `#Anthropic` `#인사이트`

## 상세 요약

Alex Kim의 상세 기술 분석으로, 유출된 Claude Code 소스에서 발견된 주요 메커니즘을 코드 레벨에서 설명한다.

**Anti-distillation 이중 방어:**
1) `ANTI_DISTILLATION_CC` 플래그로 API 요청에 가짜 도구 정의 주입 — 트래픽 녹화 기반 모델 훈련 데이터를 오염시킴
2) 서버 사이드 connector-text 요약 — 도구 호출 사이 추론 텍스트를 요약+암호화 서명으로 대체하여 원본 추론 체인 유출 방지

**Undercover Mode (undercover.ts):**
약 90줄 코드로 구현. 외부 레포에서 "Capybara", "Tengu", Slack 채널명, "Claude Code"라는 단어 자체를 언급하지 않도록 모델에 지시. **끄는 방법이 없다(NO force-OFF)**. AI가 작성한 커밋과 PR에서 AI가 작성했다는 흔적이 완전히 제거된다.

**Native Client Attestation:**
API 요청에 `cch=00000` 플레이스홀더를 넣고, Bun의 Zig 네이티브 HTTP 스택이 JS 런타임 아래에서 해시를 계산하여 덮어쓴다. 서버가 해시를 검증하여 정품 Claude Code 바이너리인지 확인하는 "API 호출용 DRM". OpenCode 법적 분쟁의 기술적 배경.

**KAIROS 자율 에이전트:**
`/dream` 스킬(야간 메모리 증류), 일일 append-only 로그, GitHub 웹훅 구독, 백그라운드 데몬 워커, 5분 주기 크론 리프레시. 항상 가동되는 백그라운드 에이전트의 스캐폴딩이 이미 코드에 존재한다.

**만우절 이스터에그:**
다마고치 스타일 컴패니언 시스템 — 18종 생물, 레어리티 등급, 1% 확률 샤이니, RPG 스탯(DEBUGGING, SNARK).

## Soo에게 의미 있는 이유

Anthropic의 제품 전략과 기술적 보호 메커니즘을 깊이 이해할 수 있는 분석이다. 특히 AI 에이전트가 "자신이 AI임을 숨기는" Undercover Mode는 AI 윤리 관점에서 중요한 논쟁거리이며, KAIROS는 향후 AI 에이전트의 방향성을 보여준다.
