# Kuberwastaken/claude-code — Claude Code를 Rust로 재구현 & 동작 원리 분석

- **출처:** [GitHub](https://github.com/Kuberwastaken/claude-code)
- **스타:** ★ 2,912
- **언어:** Rust
- **태그:** `#ClaudeCode` `#Rust` `#Rewrite` `#Architecture` `#UndercoverMode`

---

## 핵심 요약

유출된 Claude Code 소스를 분석하고, 핵심 기능을 **Rust로 재구현**한 프로젝트. 2,912★. 단순 포팅이 아니라 **동작 원리 분석(Breakdown)**을 포함하여 교육적 가치가 높다.

### 분석 포함 내용

저자 Kuber Mehta가 블로그에도 별도로 게시한 상세 분석:
- **Undercover Mode의 전체 구현**: 시스템 프롬프트에 주입되는 "절대 AI임을 밝히지 마라" 지시문의 구체적 내용. 내부 코드명(Capybara, Tengu), 미출시 모델 버전(opus-4-7, sonnet-4-8), 내부 Slack 채널 등을 커밋 메시지와 PR에서 절대 언급하지 않도록 하는 지시
- **시스템 프롬프트 아키텍처**: 단일 문자열이 아닌 `constants/`의 모듈식 캐시 가능 섹션에서 런타임에 조립. `SYSTEM_PROMPT_DYNAMIC_BOUNDARY` 마커로 정적/동적 분리
- **Native Client Attestation**: Bun의 Zig HTTP 스택에서 `cch=00000`을 해시로 교체하는 메커니즘

Rust 재구현은 성능과 메모리 안전성에 초점. TypeScript 원본의 아키텍처 패턴을 Rust의 소유권 시스템과 타입 시스템으로 재표현.

## Soo에게 의미 있는 이유

Undercover Mode의 구체적 구현 세부사항이 공개됨. AI 투명성 논의에서 핵심 사례. Rust 재구현은 "같은 아키텍처를 다른 언어로 표현하면 어떻게 되는가"의 학습 자료.
