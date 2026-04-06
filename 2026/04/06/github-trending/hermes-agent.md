# Hermes Agent: 함께 성장하는 AI 에이전트 (by NousResearch)

- **출처**: [GitHub - NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)
- **스타**: ⭐ 27,047 | **언어**: Python
- **태그**: `#AI에이전트` `#NousResearch` `#오픈소스` `#멀티플랫폼`

## 요약

NousResearch가 개발한 **로컬 실행 AI 에이전트**로, CLI 터미널 UI와 메시징 플랫폼(Telegram, Discord, Slack, WhatsApp, Signal, Email) 두 가지 인터페이스를 제공한다.

### 핵심 특징

- **워크플로 자동화**: 일회성 Q&A부터 야간 백업, 주간 감사 등 자율 작업까지
- **서브에이전트 병렬화**: 격리된 서브에이전트를 병렬로 생성하여 복잡한 작업 처리
- **Python 스크립트 + RPC**: Python 스크립트가 RPC를 통해 도구를 호출하여 다단계 파이프라인을 제로 컨텍스트 비용으로 실행
- **6개 터미널 백엔드**: 로컬, Docker, SSH, Daytona, Singularity, Modal. 서버리스 지속성으로 유휴 시 하이버네이트
- **연구용 기능**: 배치 궤적 생성, Atropos RL 환경, 궤적 압축
- **OpenClaw 마이그레이션**: `hermes claw migrate` 명령으로 OpenClaw에서 쉽게 전환

### 멀티 플랫폼

CLI에서 `hermes`로 시작하거나, `hermes gateway`로 메시징 플랫폼과 연결하여 봇처럼 사용 가능.

## Soo에게 의미 있는 이유

OpenClaw과 직접 비교할 수 있는 오픈소스 AI 에이전트 프레임워크. "함께 성장하는 에이전트"라는 컨셉과 다양한 백엔드 지원은 AI 에이전트 아키텍처를 설계할 때 참고할 만한 접근법이다. 마이그레이션 경로 제공도 인상적.
