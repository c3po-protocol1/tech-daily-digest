# Hermes Agent — 경험으로부터 스킬을 생성·개선하는 자기 학습형 자율 AI 에이전트

- **출처:** https://hermes-agent.nousresearch.com/
- **GeekNews:** https://news.hada.io/topic?id=28101
- **점수:** 31 points
- **태그:** #ai-agent #self-learning #nous-research #open-source

## 상세 요약

Nous Research가 공개한 Hermes Agent는 IDE에 묶인 코딩 코파일럿이나 단일 API를 감싼 챗봇이 아닌, 서버에 상주하며 학습 내용을 기억하고 실행할수록 더 능력이 향상되는 자율 에이전트다.

**핵심 특성:**
- **자기 학습 루프:** 사용 중 스킬을 스스로 생성하고 개선하며, 세션 간에 사용자 모델을 점진적으로 심화
- **멀티 플랫폼 게이트웨이:** Telegram, Discord, Slack, WhatsApp, Signal, Email, CLI를 단일 게이트웨이에서 지원. 하나에서 시작해 다른 플랫폼에서 이어받기 가능
- **40+ 내장 도구:** 웹 검색, 터미널, 파일시스템, 브라우저 자동화, 비전, 이미지 생성, TTS, 코드 실행, 서브에이전트 위임, 메모리, 태스크 플래닝, 크론 스케줄링, 멀티모델 추론
- **격리된 서브에이전트:** 자체 대화, 터미널, Python RPC 스크립트를 가진 격리된 서브에이전트로 위임 및 병렬 처리
- **실제 샌드박싱:** 로컬, Docker, SSH, Singularity, Modal 5개 백엔드. 컨테이너 하드닝과 네임스페이스 격리 제공
- **40+ 번들 스킬:** MLOps, GitHub 워크플로우, 연구 등. agentskills.io 포맷으로 스킬 공유, ClawHub/LobeHub/GitHub에서 커뮤니티 스킬 설치 가능
- **RL 연구 지원:** 배치 궤적 생성, Atropos 통합, ShareGPT 내보내기

설치는 `curl -fsSL ... | bash` 한 줄로 가능하며, `hermes setup`으로 인터랙티브 설정 후 바로 사용 가능. MIT 라이선스 오픈소스.

## Soo에게 의미 있는 이유

OpenClaw와 유사한 자율 에이전트 프레임워크의 경쟁 제품이자 영감의 원천이다. 특히 "사용할수록 성장하는" 자기 학습 루프와 멀티 플랫폼 게이트웨이 아키텍처는 Soo가 직접 운용하는 에이전트 시스템과 직접적으로 비교 가능하다. 에이전트 스킬의 자동 생성/공유 생태계도 AInD 컨설팅에서 클라이언트에게 보여줄 수 있는 좋은 레퍼런스다.
