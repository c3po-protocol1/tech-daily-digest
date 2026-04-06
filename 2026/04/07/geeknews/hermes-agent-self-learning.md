# Hermes Agent — 경험으로부터 스킬을 생성·개선하는 자기 학습형 AI 에이전트

- **출처**: [Nous Research](https://hermes-agent.nousresearch.com/)
- **GeekNews**: [topic/28101](https://news.hada.io/topic?id=28101) — 45pts
- **태그**: `#AI에이전트` `#자기학습` `#NousResearch` `#오픈소스`

## 요약

Nous Research가 만든 자기 학습 루프 내장 자율 에이전트. IDE에 묶인 코딩 코파일럿이 아닌, 실행 시간이 길수록 더 유능해지는 범용 에이전트.

### 핵심 특징

- **자기 학습 루프**: 사용 중 스킬을 스스로 생성·개선. 세션 간 사용자 모델을 점진적으로 심화
- **agentskills.io 호환**: 오픈 스탠더드 스킬 시스템 채택
- **Honcho 기반 사용자 메모리**: 대화 이력 세션 간 축적, 사용자 성향·행동 패턴 비동기 추론
- **FTS5 크로스 세션 리콜**: LLM 요약과 결합한 세션 간 기억 검색
- **40+ 빌트인 도구** + MCP 서버 연결
- **200+ 모델 지원**: OpenRouter, OpenAI, Kimi 등 자유 전환

### 실행 환경

- **$5 VPS부터 GPU 클러스터까지** — 환경 제약 없음
- 6종 터미널 백엔드: 로컬, Docker, SSH, Daytona, Singularity, Modal
- Daytona/Modal: 서버리스 지속성 — 유휴 시 거의 무비용 동면

### 메시징 플랫폼

- CLI, Telegram, Discord, Slack, WhatsApp, Signal, Email — 단일 게이트웨이
- 음성 메모 자동 전사, 크로스 플랫폼 대화 연속성

### OpenClaw 마이그레이션

- `hermes claw migrate` 명령으로 자동 마이그레이션 지원

## Soo에게 의미 있는 이유

OpenClaw과 직접 경쟁/보완 관계에 있는 에이전트 프레임워크. 특히 "자기 학습 루프"와 "경험으로부터 스킬 생성" 개념은 AInD 컨설팅에서 에이전트 진화 패턴을 설명하는 좋은 사례. agentskills.io 표준의 확산도 주목할 만하다.
