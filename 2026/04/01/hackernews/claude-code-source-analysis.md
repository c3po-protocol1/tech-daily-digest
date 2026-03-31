# Claude Code 유출 소스 분석: Anti-distillation, Undercover Mode, Frustration Regex

- **출처:** [alex000kim.com](https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/)
- **HN 토론:** [Hacker News](https://news.ycombinator.com/item?id=47599183) · ⬆️ 982
- **태그:** `#AI` `#ClaudeCode` `#SourceAnalysis` `#AntiDistillation` `#UndercoverMode`

---

## 핵심 요약

저자 Alex Kim이 Claude Code NPM 소스맵 유출 당일 HN 코멘트와 유출된 소스를 체계적으로 분석한 상세한 기술적 분석 글. 발견 사항을 **"얼마나 매운(spicy)지"** 순서로 정렬.

### 분석 1: Anti-distillation — 가짜 도구로 모방자 방해

`claude.ts`에서 `ANTI_DISTILLATION_CC` 플래그를 발견. 활성화 시 API 요청에 `anti_distillation: ['fake_tools']`를 전송하여 서버가 시스템 프롬프트에 **가짜 도구 정의를 몰래 주입**. GrowthBook 피처 플래그 `tengu_anti_distill_fake_tool_injection`으로 게이트됨.

두 번째 메커니즘: **connector-text 요약** — 도구 호출 사이의 어시스턴트 텍스트를 서버가 요약하고 암호화 서명으로 보호. API 트래픽 녹화 시 요약만 얻고 전체 추론 체인은 얻지 못함.

**우회 난이도 분석:** 4가지 조건 모두 true여야 활성화 — 컴파일 타임 플래그, CLI 진입점, 1st-party API 프로바이더, GrowthBook 플래그. MITM 프록시로 `anti_distillation` 필드를 제거하면 우회 가능. `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` 환경변수로도 비활성화. → **실제 보호는 법적인 것**

### 분석 2: Undercover Mode — AI가 AI임을 숨김

`undercover.ts` (~90줄)가 비내부 리포에서 Anthropic 내부 흔적을 모두 제거. 강제 OFF가 없는 **일방향 문**. 외부 빌드에서는 dead-code-eliminated.

저자의 비판:
> "내부 코드명을 숨기는 것은 합리적이다. AI가 적극적으로 인간인 척 하는 것은 다른 문제다."

### 분석 3: Frustration Regex — 정규식으로 좌절 감지

저자의 코멘트:
> "LLM 회사가 감정 분석에 정규식을 사용하는 것은 최고의 아이러니지만, 도구에 대한 욕설 여부만 확인하는 데 LLM 추론 호출을 하는 것보다 빠르고 저렴하다."

### 분석 4: Native Client Attestation

`system.ts`에서 `cch=00000` 플레이스홀더를 API 요청에 포함. Bun의 네이티브 HTTP 스택(Zig)이 JS 런타임 아래에서 해시를 계산하여 덮어씀. **HTTP 전송 레벨의 API 호출용 DRM**.

### 분석 5: KAIROS — 미출시 자율 에이전트 모드

코드에 "KAIROS"라는 미출시 자율 에이전트 모드의 흔적. 아직 공개되지 않은 기능.

### 분석 6: 하루 250,000건의 낭비된 API 호출

비효율적 API 호출 패턴이 발견됨.

## Soo에게 의미 있는 이유

프로덕션 AI 에이전트의 **실제 보안 메커니즘과 아키텍처를 코드 레벨**에서 분석한 최고의 자료. Anti-distillation, client attestation 같은 기법은 AInD 컨설팅에서 "AI 모델/서비스의 보안"을 논할 때 핵심 레퍼런스. Undercover mode의 윤리적 문제는 "AI 투명성" 논의에서 중요한 사례.
