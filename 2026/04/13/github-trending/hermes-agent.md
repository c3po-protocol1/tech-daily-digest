# 🔥 NousResearch/hermes-agent — 자기 학습하는 AI 에이전트

> **GitHub**: [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
> **태그**: `#AI에이전트` `#자기학습` `#멀티플랫폼` `#오픈소스`
> 🔥 **3일 이상 연속 트렌딩**

## 요약

Nous Research가 만든 **자기 개선 학습 루프를 내장한 AI 에이전트**. 경험에서 스킬을 생성하고, 사용 중 스킬을 개선하며, 세션 간 지식을 축적한다.

**핵심 차별점:**
- **폐쇄 학습 루프**: 복잡한 작업 후 자율적으로 스킬 생성, 사용 중 자기 개선, FTS5 세션 검색으로 과거 대화 회상
- **어디서든 실행**: $5 VPS, GPU 클러스터, 서버리스 (Daytona, Modal로 유휴 시 비용 0)
- **모든 모델**: Nous Portal, OpenRouter(200+ 모델), z.ai/GLM, OpenAI 등 — `hermes model`로 변경
- **멀티플랫폼**: Telegram, Discord, Slack, WhatsApp, Signal + CLI — 단일 게이트웨이 프로세스
- **스케줄링**: 내장 cron으로 일일 보고서, 야간 백업, 주간 감사 — 자연어로 설정

**OpenClaw에서 마이그레이션**: `hermes claw migrate` 명령으로 OpenClaw에서 이전 가능.

**연구용 기능**: 배치 트래젝토리 생성, Atropos RL 환경, 트래젝토리 압축 — 차세대 도구 호출 모델 학습용.

## Soo에게 의미 있는 이유

OpenClaw의 직접적인 경쟁자이자 참고 대상. 특히 "자기 학습 루프"와 "스킬 자동 생성" 패턴은 OpenClaw에 아직 없는 기능이다. agentskills.io 오픈 표준 호환, Honcho 사용자 모델링 등의 접근법도 주목.
