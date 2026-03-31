# Claude Code 소스코드가 NPM 소스맵 파일을 통해 유출

- **출처:** [Twitter - @Fried_rice/Chaofan Shou](https://twitter.com/Fried_rice/status/2038894956459290963)
- **HN 토론:** [Hacker News](https://news.ycombinator.com/item?id=47597531) · ⬆️ 1,838 · 💬 898
- **태그:** `#Security` `#AI` `#Claude` `#NPM` `#SourceLeak`

---

## 핵심 요약

Anthropic의 Claude Code CLI 도구의 전체 소스코드가 NPM 패키지에 포함된 `.map`(소스맵) 파일을 통해 유출되었다. 이것은 Anthropic의 **1주일 내 두 번째 유출 사고** — 불과 며칠 전 모델 스펙 유출이 있었다. 소스맵은 번들링된 JavaScript를 원본 소스에 매핑하는 디버깅 파일인데, 빌드 파이프라인에서 제거하지 않고 npm에 배포한 것이 원인이다.

1,838점이라는 극도로 높은 점수와 898개의 댓글은 이 사건이 AI 코딩 도구 커뮤니티에 미친 충격을 반영한다. 유출 후 패키지가 npm에서 pull되었지만, 이미 코드가 광범위하게 미러링되고 분석되었다.

### 배경: 유출의 맥락

10일 전 Anthropic이 OpenCode에 법적 위협을 보내, 제3자 도구가 Claude Code의 내부 API를 사용하여 구독 요금으로 Opus에 접근하는 것을 차단한 바 있다. 이 맥락에서 소스코드 유출은 더 큰 아이러니를 자아낸다.

### 유출 소스에서 발견된 주요 내부 메커니즘

**1. Anti-distillation: 가짜 도구 주입으로 모방자 방해**

`claude.ts` (301-313줄)에 `ANTI_DISTILLATION_CC` 플래그가 존재. 활성화되면 API 요청에 `anti_distillation: ['fake_tools']`를 전송하여, 서버가 시스템 프롬프트에 **가짜 도구 정의를 몰래 주입**. 목적: 누군가 Claude Code의 API 트래픽을 녹화하여 경쟁 모델을 훈련할 경우, 가짜 도구가 훈련 데이터를 오염시킴.

두 번째 anti-distillation 메커니즘: `betas.ts` (279-298줄)에서 서버 측 connector-text 요약. 활성화 시 API가 도구 호출 사이의 어시스턴트 텍스트를 요약하고, 원본 텍스트를 암호화 서명으로 복원 가능하게 저장. 트래픽을 녹화하는 사람은 요약만 얻고 전체 추론 체인은 얻지 못함.

**우회 난이도:** 높지 않음. MITM 프록시가 요청 본문에서 `anti_distillation` 필드를 제거하면 우회 가능. 환경변수 `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS`를 truthy로 설정해도 비활성화. 실제 보호는 기술적이라기보다 **법적**인 것으로 추정.

**2. Undercover Mode: AI가 AI임을 숨기는 모드**

`undercover.ts` (~90줄)는 Claude Code가 비내부 리포에서 사용될 때 **Anthropic 내부의 모든 흔적을 제거**하는 모드. 모델에게 "Capybara", "Tengu" 같은 내부 코드명, 내부 Slack 채널, 리포 이름, "Claude Code"라는 문구 자체를 언급하지 말라고 지시.

> "강제 OFF가 없다. 모델 코드명 유출을 방지하기 위한 것."

`CLAUDE_CODE_UNDERCOVER=1`로 강제 ON은 가능하지만, 강제 OFF하는 방법은 없다. 외부 빌드에서는 전체 함수가 dead-code-eliminated됨. **일방향 문(one-way door).**

→ Anthropic 직원의 오픈소스 프로젝트 커밋/PR에서 AI가 작성했다는 표시가 없다. 내부 코드명 숨기기는 합리적이지만, **AI가 적극적으로 인간인 척 하는 것은 다른 문제.**

**3. Frustration Detection via Regex (정규식으로 사용자 좌절 감지)**

`userPromptKeywords.ts`에 사용자 좌절을 감지하는 정규식 패턴:

```
/\b(wtf|wth|ffs|omfg|shit(ty|tiest)?|dumbass|horrible|awful|
piss(ed|ing)? off|piece of (shit|crap|junk)|what the (fuck|hell)|
fucking? (broken|useless|terrible|awful|horrible)|fuck you|
screw (this|you)|so frustrating|this sucks|damn it)\b/
```

> "LLM 회사가 감정 분석에 정규식을 사용하는 것은 최고의 아이러니지만, 감정 확인만을 위해 LLM 추론 호출을 하는 것보다 더 빠르고 저렴하다."

**4. Native Client Attestation (네이티브 클라이언트 인증)**

`system.ts` (59-95줄)에서 API 요청에 `cch=00000` 플레이스홀더를 포함. 요청이 프로세스를 떠나기 전, Bun의 네이티브 HTTP 스택(Zig로 작성)이 5개의 0을 계산된 해시로 덮어씀. 서버가 해시를 검증하여 요청이 **실제 Claude Code 바이너리에서 온 것**인지 확인.

같은 길이의 플레이스홀더를 사용하여 Content-Length 헤더 변경이나 버퍼 재할당 불필요. 계산이 JavaScript 런타임 아래에서 이루어지므로 JS 레이어에서 실행되는 어떤 것에도 **보이지 않음**. 사실상 HTTP 전송 레벨에서 구현된 **API 호출용 DRM**.

**5. 하루 250,000건의 낭비된 API 호출**

소스코드에서 비효율적 API 호출 패턴이 발견됨 — 하루 약 250,000건의 불필요한 호출.

**6. KAIROS: 미출시 자율 에이전트 모드**

아직 출시되지 않은 "KAIROS"라는 자율 에이전트 모드의 코드가 존재.

## Soo에게 의미 있는 이유

이것은 단순한 보안 사고가 아니라, **프로덕션 AI 에이전트의 내부 아키텍처를 직접 볼 수 있는 전례 없는 기회**다.

1. **Anti-distillation** — 모델 보호를 위한 기술적 방어 메커니즘. AInD에서 "AI 모델 보호 전략"을 논할 때 핵심 사례
2. **Undercover Mode** — AI의 정체성 투명성에 대한 윤리적 논쟁. "AI가 작성했는지 공개해야 하는가"
3. **Frustration Regex** — 사용자 경험 관리를 위한 실용적이고 저비용 접근
4. **Client Attestation (HTTP 레벨 DRM)** — API 보안의 고급 기법
5. **Harness 엔지니어링 관점** — Claude Code의 실제 구현을 코드 레벨에서 학습할 수 있는 최고의 기회
