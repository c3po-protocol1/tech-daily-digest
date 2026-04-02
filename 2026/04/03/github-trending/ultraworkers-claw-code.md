# 🔥 claw-code — 역사상 가장 빠르게 100K 스타 돌파한 저장소

- **GitHub:** https://github.com/ultraworkers/claw-code
- **스타:** 149,321 ⭐ | **포크:** 101K
- **언어:** Rust
- **태그:** #coding-agent #rust #claude-code #harness #open-source

## 상세 요약

Claude Code 소스 유출을 계기로 탄생한 claw-code는 역사상 가장 빠르게 100K 스타를 돌파한 저장소다(공개 후 2시간 만에 50K 돌파). 단순 아카이브가 아닌, "더 나은 Harness Tools"를 지향하며 Rust로 재작성되고 있다.

**배경:** 한국 개발자 Sigrid Jin(@instructkr)이 2026년 3월 31일 새벽 4시, 유출된 코드의 하네스 구조를 분석한 뒤 Python으로 클린룸 재작성을 시작. oh-my-codex(OmX) 워크플로우를 사용해 병렬 코드 리뷰($team 모드)와 아키텍트 검증 루프($ralph 모드)를 통해 전체 포팅 세션을 오케스트레이션했다.

**Rust 포트 구조:**
- `crates/api-client` — 프로바이더 추상화, OAuth, 스트리밍 지원 API 클라이언트
- `crates/runtime` — 세션 상태, 압축, MCP 오케스트레이션, 프롬프트 구성
- `crates/tools` — 도구 매니페스트 정의 및 실행 프레임워크
- `crates/commands` — 슬래시 명령어, 스킬 탐색, 설정 검사
- `crates/plugins` — 플러그인 모델, 훅 파이프라인, 번들 플러그인
- `crates/compat-harness` — 업스트림 에디터 통합 호환 계층
- `crates/claw-cli` — 인터랙티브 REPL, 마크다운 렌더링, 프로젝트 부트스트랩

WSJ에서도 "1조 달러 규모의 자동화 경쟁" 기사에서 Sigrid Jin의 Claude Code 활용 사례를 소개. 현재 소유권 이전 중이며 parity 브랜치에서 개발 계속 중.

## Soo에게 의미 있는 이유

에이전트 하네스 엔지니어링의 핵심을 Rust로 재구현하는 프로젝트로, 에이전트 런타임의 성능과 안정성을 극대화하려는 시도다. 149K 스타라는 폭발적 관심은 개발자 커뮤니티가 에이전트 코딩 도구에 얼마나 갈망하는지를 보여준다.
