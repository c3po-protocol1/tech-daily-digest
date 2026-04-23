# Google Agents CLI — 코딩 에이전트를 에이전트 빌더로 만드는 메타 도구

> **출처:** [github.com/google/agents-cli](https://github.com/google/agents-cli)
> **GeekNews:** [토론](https://news.hada.io/topic?id=28817) (4 points)
> **태그:** `#AI` `#Agent` `#GoogleCloud` `#CLI` `#DevTools`

## 요약

Google이 Cloud Next에서 공개한 **agents-cli**는 Gemini CLI, Claude Code, Codex 같은 코딩 에이전트에게 Google Cloud 기반 AI 에이전트를 설계하고 배포하는 "스킬"을 부여하는 메타 도구다. ⭐ 686 stars.

### 핵심 컨셉
"코딩 에이전트를 에이전트 빌더로 전환"하는 발상. 개발자가 모든 CLI와 서비스를 직접 배울 필요 없이, 코딩 에이전트에게 스킬을 가르쳐서 대신 구축하게 한다.

### 호환 에이전트
Gemini CLI, Claude Code, Codex, Antigravity 등 모든 코딩 에이전트와 호환.

### 7가지 스킬
| 스킬 | 에이전트가 배우는 것 |
|------|---------------------|
| workflow | 개발 라이프사이클, 코드 보존 규칙, 모델 선택 |
| adk-code | ADK Python API — 에이전트, 도구, 오케스트레이션 |
| scaffold | 프로젝트 스캐폴딩 — create, enhance, upgrade |
| eval | 평가 방법론 — 메트릭, 평가세트, LLM-as-judge |
| deploy | 배포 — Agent Runtime, Cloud Run, GKE, CI/CD |
| publish | Gemini Enterprise 등록 |
| observability | 관찰성 — Cloud Trace, 로깅, 서드파티 통합 |

### 설치
```bash
uvx google-agents-cli setup
# 또는 스킬만
npx skills add google/agents-cli
```

### 사용 예시
코딩 에이전트에게 "Use agents-cli to build a caveman-style agent that compresses verbose text into terse, technical grunts"처럼 자연어로 지시하면 에이전트가 ADK 기반 에이전트를 구축한다.

## Soo에게 의미 있는 이유

"에이전트가 에이전트를 만드는" 메타 도구 패턴은 AInD의 핵심 방향이다. Google이 공식적으로 이 패턴을 지원한다는 것은, 에이전트 빌더 시장이 본격 형성되고 있음을 의미한다. AInD 컨설팅 PoC에서 이 도구를 활용하여 고객에게 "에이전트로 에이전트를 만드는" 데모를 보여줄 수 있다.
