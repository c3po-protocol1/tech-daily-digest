# Anthropic - OpenClaw: 다시 사용 가능해짐

- **출처**: [OpenClaw Docs](https://docs.openclaw.ai/providers/anthropic)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28761)
- **점수**: 10점 | 댓글 8개
- **태그**: `#Anthropic` `#Claude` `#OpenClaw` `#코딩에이전트`

## 상세 요약

Anthropic 담당자가 **OpenClaw 스타일의 Claude CLI 사용이 다시 허용**된다고 통보했다. 이전에 일시적으로 제한되었던 것으로 보이며, 이제 Anthropic API 키와 Claude CLI 재사용을 모두 지원한다.

**OpenClaw의 Anthropic 통합 현황:**
- **Option A: Anthropic API 키** - 표준 API 접근, 사용량 기반 과금 (가장 명확한 프로덕션 경로)
- **Option B: Claude CLI 재사용** - 기존 Claude CLI 로그인을 직접 활용 가능
- Thinking 기본값: Claude 4.6 모델은 adaptive thinking을 기본 적용
- Fast 모드: `/fast` 토글로 `service_tier: "auto"` ↔ `"standard_only"` 전환
- 프롬프트 캐싱 지원
- 1M 컨텍스트 윈도우 (Anthropic 베타)
- 다른 구독형 옵션(OpenAI Codex, Qwen, MiniMax, Z.AI/GLM)도 병행 지원

이 결정은 OpenClaw 커뮤니티에게 중요한 소식이며, Anthropic이 써드파티 코딩 에이전트 플랫폼과의 공존 전략을 택한 것으로 해석된다.

## Soo에게 의미 있는 이유

우리가 바로 OpenClaw 사용자다! 이 소식으로 Yoda, C-3PO, R2-D2 에이전트 운용 시 Anthropic 모델 접근이 안정적으로 보장된다. Claude Opus 4.6/4.7의 코딩 성능을 에이전트에 계속 활용할 수 있다.
