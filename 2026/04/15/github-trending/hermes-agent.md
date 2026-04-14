# 🔥 NousResearch/hermes-agent — 자기 개선 AI 에이전트

- **레포**: [github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- **태그**: #AIAgent #NousResearch #셀프임프루빙 #오픈소스
- 🔥 2일 이상 연속 트렌딩

## 상세 요약

Nous Research가 만든 **자기 개선(self-improving) AI 에이전트**다. 내장 학습 루프로 경험에서 스킬을 생성하고, 사용 중 개선하며, 세션 간 지식을 영속화한다.

**핵심 특징:**
- **학습 루프**: 에이전트가 복잡 작업 후 자동으로 스킬 생성. 스킬이 사용 중 자체 개선. 주기적 nudge로 지식 영속화
- **멀티 플랫폼**: Telegram, Discord, Slack, WhatsApp, Signal + CLI — 단일 게이트웨이에서 모든 플랫폼
- **모델 자유**: Nous Portal, OpenRouter(200+ 모델), Xiaomi, z.ai, Kimi, MiniMax, Hugging Face, OpenAI 등
- **서브에이전트 + 병렬화**: 격리된 서브에이전트 스폰, Python 스크립트로 도구 RPC 호출
- **6가지 실행 백엔드**: 로컬, Docker, SSH, Daytona, Singularity, Modal — $5 VPS부터 GPU 클러스터까지

**학습 시스템:** FTS5 세션 검색 + LLM 요약으로 크로스세션 리콜. Honcho 변증법적 사용자 모델링. agentskills.io 오픈 표준 호환.

OpenClaw에서 마이그레이션도 지원(`hermes claw migrate`).

## Soo에게 의미 있는 이유

"자기 개선 에이전트"는 AI 에이전트의 다음 단계를 보여준다. 경험에서 스킬을 생성하고 자체 개선하는 학습 루프는 OpenClaw의 스킬 시스템과 비교하여 흥미로운 설계 차이를 제공한다.
