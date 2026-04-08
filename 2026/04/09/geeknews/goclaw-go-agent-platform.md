# GoClaw — OpenClaw를 Go로 재구성한 멀티 에이전트 게이트웨이

- **출처:** [goclaw.sh](https://goclaw.sh/)
- **GeekNews:** [topic?id=28310](https://news.hada.io/topic?id=28310) (7 points)
- **태그:** `#Go` `#에이전트플랫폼` `#OpenClaw` `#보안` `#엔터프라이즈`

## 상세 요약

OpenClaw 계열 에이전트 프레임워크를 Go 기반으로 재구성한 엔터프라이즈급 플랫폼. NextLevelBuilder.io 팀이 개발.

### 핵심 차별점
- **<1초 시작 시간**, ~25MB 바이너리 (Node.js 런타임 불필요)
- **멀티테넌트 PostgreSQL:** Row-Level Security로 테넌트 간 데이터 격리
- **5중 보안 계층:** 레이트 리밋, SQL/프롬프트 인젝션 탐지, SSRF 보호, 셸 패턴 매칭, AES-256-GCM 암호화
- **CVE-2026-25253 패치:** OpenClaw 4만+ 인스턴스에 여전히 존재하는 취약점 해결
- **에이전트 팀:** 공유 태스크 보드, 대화 핸드오프, 평가 루프, 품질 게이트

### 비교 (GoClaw vs OpenClaw vs ZeroClaw vs PicoClaw)
| 특성 | GoClaw | OpenClaw |
|------|--------|----------|
| 멀티테넌트 | RLS(DB) | ✕ |
| 5중 보안 | ✓ | ✕ |
| LLM 제공자 | 20+ | 35+ |
| 시작 시간 | <1s | >5s |
| 바이너리 | ~25MB | 28MB+Node |
| 메시징 채널 | 7 | 23+ |

### 지원 채널
Telegram, Discord, Slack, Zalo, Feishu/Lark, WhatsApp, WebSocket

### 지원 LLM
Anthropic, OpenAI, Google Gemini, Groq, Mistral, Ollama, Cohere, DeepSeek 등 20+

## Soo에게 의미 있는 이유
우리가 사용하는 OpenClaw의 Go 대안. 엔터프라이즈 환경에서의 보안·멀티테넌트 요구사항을 어떻게 해결하는지 참고할 가치가 있으며, CVE-2026-25253 취약점은 우리 인스턴스도 확인 필요.
