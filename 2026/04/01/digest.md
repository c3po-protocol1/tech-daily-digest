# Tech Daily Digest — 2026년 4월 1일 (화)

## 🔥 오늘의 하이라이트

- **Claude Code 소스코드 유출** (HN 1838점) — NPM 레지스트리의 .map 파일을 통해 전체 소스 복원 가능
- **Axios NPM 해킹** (HN 1748점) — 주당 1억 다운로드 라이브러리에 RAT 악성코드 삽입
- **Ollama MLX 지원** (GN) — Apple Silicon에서 MLX 프레임워크 기반 추론 지원
- **Qwen3.5-Omni** (GN) — 텍스트·이미지·오디오·영상 모두 처리하는 완전 옴니모달 LLM

---

## Hacker News

### 1. [Claude Code 소스코드가 NPM 레지스트리 맵 파일을 통해 유출](https://twitter.com/Fried_rice/status/2038894956459290963)

Anthropic의 Claude Code CLI 도구의 전체 소스코드가 NPM 패키지에 포함된 `.map` (소스맵) 파일을 통해 외부에 유출되었다. 소스맵은 원래 디버깅 목적으로 번들링된 코드를 원본 소스에 매핑하는 파일인데, 빌드 과정에서 이를 제거하지 않고 NPM에 퍼블리시한 것이 원인이다. 유출된 코드에서는 "fake tools", "frustration regexes" (사용자 좌절 감지 정규식), "undercover mode" 등 흥미로운 내부 메커니즘이 발견되었다. 이 사건은 NPM 패키지 배포 시 소스맵 제거의 중요성과, AI 코딩 도구의 내부 동작 투명성에 대한 논의를 촉발했다.

`#Security` `#AI` `#Claude` `#NPM` `#SourceLeak`

⬆️ 1838 · 💬 898

### 2. [Axios NPM 패키지 해킹 — 악성 버전에서 원격 접근 트로이목마 배포](https://www.stepsecurity.io/blog/axios-compromised-on-npm-malicious-versions-drop-remote-access-trojan)

주당 1억 회 이상 다운로드되는 인기 HTTP 클라이언트 라이브러리 Axios의 악성 버전(1.14.1, 0.30.4)이 NPM에 게시되었다. 공격자는 유지관리자 계정의 자격 증명을 탈취하여 GitHub Actions CI를 우회하고 수동으로 악성 패키지를 업로드했다. 설치 시 원격 접근 트로이목마(RAT)가 배포되어 시스템을 완전히 제어할 수 있게 된다. 이 사건은 NPM 생태계의 공급망 보안 취약성을 다시 한번 부각시켰으며, 의존성 고정(pinning)과 lockfile 검증의 중요성을 재확인시킨다.

`#Security` `#NPM` `#SupplyChain` `#Malware`

⬆️ 1748 · 💬 708

### 3. [Claude Code 소스 유출 분석: fake tools, frustration regexes, undercover mode](https://alex000kim.com/posts/2026-03-31-claude-code-source-leak/)

유출된 Claude Code 소스코드를 상세 분석한 글. 주요 발견으로는: (1) **Fake tools** — 실제로 동작하지 않지만 모델의 행동을 제어하기 위한 가짜 도구 정의, (2) **Frustration regexes** — 사용자의 좌절감을 감지하여 응답 전략을 조정하는 정규식 패턴, (3) **Undercover mode** — 디버깅이나 내부 테스트용으로 보이는 숨겨진 모드, (4) 컨텍스트 관리와 에이전틱 루프의 구체적인 구현 방식 등이 공개되었다. 이 분석은 현대 AI 코딩 도구가 어떻게 사용자 경험을 최적화하는지에 대한 귀중한 인사이트를 제공한다.

`#AI` `#Claude` `#ReverseEngineering` `#AgenticCoding`

⬆️ 565 · 💬 217

### 4. [GitHub 역대 업타임 기록](https://damrnelson.github.io/github-historical-uptime/)

GitHub의 역사적 업타임 데이터를 시각화한 프로젝트. 연도별, 서비스별(API, Actions, Pages, Packages 등) 가용성 지표를 추적하여 GitHub 인프라의 안정성 트렌드를 보여준다. 최근 몇 년간 GitHub Actions의 안정성이 특히 개선된 반면, 특정 기간에 대규모 장애가 발생했던 패턴도 확인할 수 있다. 개발 인프라의 신뢰성을 평가하는 데 유용한 참고 자료다.

`#GitHub` `#Infrastructure` `#DevOps` `#Reliability`

⬆️ 351 · 💬 98

### 5. [브라우저에서 동작하는 오픈소스 CAD — Solvespace](https://solvespace.com/webver.pl)

전통적으로 데스크톱 네이티브 앱이었던 오픈소스 파라메트릭 2D/3D CAD 프로그램 Solvespace가 WebAssembly를 통해 브라우저에서 직접 실행 가능해졌다. 설치 없이 즉시 사용할 수 있으며, 구속 기반(constraint-based) 모델링을 지원한다. 전문 CAD 소프트웨어의 웹 접근성을 대폭 향상시킨 사례로, WebAssembly가 데스크톱급 애플리케이션을 웹으로 가져오는 데 얼마나 성숙했는지를 보여준다.

`#CAD` `#OpenSource` `#WebAssembly` `#Engineering`

⬆️ 268 · 💬 85

### 6. [Slop은 반드시 미래가 아니다](https://www.greptile.com/blog/ai-slopware-future)

AI가 생성한 저품질 코드("슬롭웨어")가 소프트웨어 개발의 미래를 지배할 것이라는 비관론에 반박하는 글. AI 코딩 도구가 발전하면서 양질의 코드 생성 능력도 향상되고 있으며, 개발자의 역할이 "코드 작성자"에서 "코드 감독자/설계자"로 진화하고 있다고 주장한다. 핵심은 AI 도구 자체가 아니라 이를 사용하는 개발자의 판단력과 설계 능력이라는 점을 강조하며, 품질 기준을 유지하면서 AI를 활용하는 방법론을 제시한다.

`#AI` `#SoftwareQuality` `#CodingAgents` `#DeveloperExperience`

⬆️ 147 · 💬 261

### 7. [Cohere Transcribe: 음성 인식](https://cohere.com/blog/transcribe)

Cohere가 새로운 음성 인식 서비스 Transcribe를 출시했다. 다국어 지원, 화자 분리(diarization), 실시간 스트리밍 전사를 지원하며, Whisper 대비 정확도와 속도 면에서 경쟁력을 내세운다. 엔터프라이즈 환경에서의 데이터 프라이버시를 강조하며 온프레미스 배포도 지원한다. STT(Speech-to-Text) 시장에서 OpenAI Whisper, Google, AWS Transcribe에 대한 새로운 대안으로 주목된다.

`#AI` `#SpeechRecognition` `#STT` `#Cohere`

⬆️ 145 · 💬 47

### 8. [Forkrun — NUMA 인식 셸 병렬화 도구 (GNU parallel 대비 50~400배 빠름)](https://github.com/jkool702/forkrun)

GNU parallel의 대안으로 개발된 셸 기반 병렬 실행 도구. NUMA(Non-Uniform Memory Access) 아키텍처를 인식하여 CPU 토폴로지에 최적화된 작업 분배를 수행한다. 벤치마크에서 GNU parallel 대비 50~400배 빠른 성능을 보여주며, 순수 bash로 작성되어 추가 의존성이 없다. 대규모 파일 처리나 데이터 파이프라인에서 병렬 처리가 필요한 시스템 관리자와 데이터 엔지니어에게 유용하다.

`#Performance` `#Shell` `#Parallelization` `#Linux`

⬆️ 91 · 💬 21

### 9. [PostgreSQL BM25 전문 검색 확장](https://github.com/timescale/pg_textsearch)

Timescale이 개발한 PostgreSQL 확장으로, BM25 알고리즘 기반의 관련성 순위 전문 검색을 제공한다. 기존 PostgreSQL의 ts_rank보다 정교한 검색 결과 순위를 제공하며, Elasticsearch 같은 외부 검색 엔진 없이도 고품질 전문 검색을 PostgreSQL 내에서 직접 수행할 수 있다. 인프라 복잡성을 줄이면서도 검색 품질을 높이고 싶은 개발자에게 실용적인 선택지다.

`#PostgreSQL` `#Search` `#BM25` `#Database`

⬆️ 78 · 💬 28

### 10. [KV Cache 문제 해결: 토큰당 300KB에서 69KB로](https://news.future-shock.ai/the-weight-of-remembering/)

LLM 아키텍처에서 추론 시 메모리 병목이 되는 KV(Key-Value) 캐시 문제를 다양한 접근법으로 해결하는 방법을 설명한다. Multi-Query Attention(MQA), Grouped-Query Attention(GQA), Sliding Window Attention 등의 기법이 토큰당 메모리 사용량을 300KB에서 69KB로 줄이는 과정을 상세히 분석한다. 긴 컨텍스트 처리가 필수가 된 현대 LLM에서 KV 캐시 최적화가 실제 배포 비용과 성능에 미치는 영향을 이해하는 데 핵심적인 글이다.

`#LLM` `#Architecture` `#KVCache` `#Optimization` `#AI`

⬆️ 69 · 💬 5

### 11. [Ministack — LocalStack 대체제](https://ministack.org/)

AWS 로컬 개발 환경 에뮬레이터 LocalStack의 경량 대안. LocalStack이 점차 무거워지고 유료 기능이 늘어나면서, 핵심 AWS 서비스(S3, SQS, DynamoDB 등)만 가볍게 에뮬레이션하는 것에 집중한다. Docker 이미지 크기가 훨씬 작고 기동 시간이 빠르며, 무료로 사용 가능하다. 로컬 개발과 CI/CD에서 AWS 서비스를 테스트하는 개발자에게 실용적인 대안이다.

`#AWS` `#DevTools` `#LocalDevelopment` `#OpenSource`

⬆️ 69 · 💬 13

### 12. [4D Doom — HYPERHELL](https://github.com/danieldugas/HYPERHELL)

클래식 게임 Doom을 4차원 공간으로 확장한 실험적 프로젝트. 플레이어가 4차원 공간에서 이동하고 전투하며, 3차원 단면(slice)을 통해 4차원 세계를 인지한다. 4차원 기하학과 렌더링의 수학적 개념을 게임이라는 친숙한 형식으로 탐험할 수 있는 독특한 프로젝트로, 고차원 공간 시각화에 대한 교육적 가치도 있다.

`#GameDev` `#4D` `#Graphics` `#Math`

⬆️ 72 · 💬 10

### 13. [Tailscale Exit Node를 통한 트래픽 추적 실험](https://tech.stonecharioteer.com/posts/2026/tailscale-exit-nodes/)

자택 서버에 Tailscale Exit Node를 설정하고 실제 트래픽이 어떻게 라우팅되는지 추적한 실험기. DNS 쿼리, HTTPS 연결, WebSocket 통신이 Exit Node를 통과하는 과정을 Wireshark와 tcpdump로 분석한다. VPN과 Exit Node의 차이, 프라이버시 관점에서의 장단점, 그리고 자가 호스팅 Exit Node의 실용적 활용 사례를 다룬다.

`#Networking` `#Tailscale` `#VPN` `#Privacy` `#SelfHosting`

⬆️ 41 · 💬 18

### 14. [1-Bit Bonsai — 최초의 상용 가능한 1-Bit LLM](https://prismml.com/)

1비트 양자화 LLM을 상용 수준으로 끌어올린 프로젝트. 기존 1-bit LLM이 학술적 실험에 머물렀던 반면, Bonsai는 실제 프로덕션에서 사용 가능한 품질과 성능을 달성했다고 주장한다. 극단적인 양자화를 통해 모델 크기와 추론 비용을 대폭 절감하면서도 유용한 성능을 유지하는 기법을 제시하며, 엣지 디바이스 배포의 새로운 가능성을 연다.

`#LLM` `#Quantization` `#1Bit` `#EdgeAI` `#ML`

⬆️ 18 · 💬 7

### 15. [Claude Code로 실수로 Fork Bomb을 만든 이야기](https://www.droppedasbaby.com/posts/2602-01/)

AI 코딩 에이전트(Claude Code)를 사용하다가 실수로 포크 폭탄(시스템 리소스를 고갈시키는 재귀적 프로세스 생성)을 만들어버린 사용자의 경험담. AI가 생성한 스크립트의 재귀 호출 구조를 충분히 검토하지 않고 실행한 것이 원인이었다. AI 코딩 도구 사용 시 생성된 코드를 반드시 리뷰해야 하며, 특히 시스템 명령어나 프로세스 생성과 관련된 코드는 더욱 주의가 필요하다는 교훈을 준다.

`#AI` `#CodingAgents` `#Security` `#DevExperience`

⬆️ 49 · 💬 12

### 16. [GitHub Monaspace 케이스 스터디](https://lettermatic.com/custom/monaspace-case-study)

GitHub의 코딩 폰트 시스템 Monaspace의 디자인 과정을 다룬 케이스 스터디. 5가지 가변 축(Neon, Argon, Xenon, Radon, Krypton)을 가진 슈퍼패밀리 폰트가 어떻게 설계되었는지, 텍스처 힐링(texture healing) 기술의 구현 원리, 그리고 코딩 환경에 최적화된 가독성을 달성하기 위한 타이포그래피 결정들을 상세히 설명한다.

`#Typography` `#Design` `#GitHub` `#Fonts`

⬆️ 104 · 💬 36

### 17. [FreeBSD로 돌아가기 — Part 2: Jails](https://hypha.pub/back-to-freebsd-part-2)

FreeBSD의 Jail 시스템을 활용한 서버 격리 및 관리 방법을 다룬 시리즈의 두 번째 글. Docker/컨테이너 대신 FreeBSD Jail을 선택한 이유, Jail 설정 및 네트워킹 구성, ZFS와의 통합, 그리고 실제 운영 경험을 공유한다. Linux 컨테이너 생태계에 익숙한 개발자에게 BSD 진영의 대안적 접근법을 소개한다.

`#FreeBSD` `#Jails` `#SysAdmin` `#Containers`

⬆️ 14 · 💬 2

---

## GeekNews (긱뉴스)

### 1. [Claude Code 소스 코드가 npm 레지스트리 맵 파일을 통해 유출](https://news.hada.io/topic?id=28059)

Anthropic의 Claude Code CLI 소스 코드가 npm 레지스트리의 `.map` 파일을 통해 통째로 복원 가능한 형태로 유출되었다. 소스맵 파일은 원래 번들링된 JavaScript를 원본 소스에 매핑하는 디버깅 용도인데, 빌드 파이프라인에서 제거하지 않고 npm에 배포한 것이 원인이다. 이 사건은 npm 패키지 배포 시 민감한 파일을 `.npmignore`나 `files` 필드로 명시적으로 제외해야 한다는 기본적인 보안 관행의 중요성을 다시 한번 상기시킨다.

`#Security` `#NPM` `#Claude` `#SourceLeak`

### 2. [Claude Code 유출 소스 기반 Python 클린룸 재작성 프로젝트 — claw-code](https://news.hada.io/topic?id=28061)

한국 개발자 Sigrid Jin이 유출된 Claude Code 소스를 직접 참조하지 않고 핵심 기능을 Python으로 처음부터 재작성한 프로젝트. 법적 리스크를 피하기 위해 클린룸 방식으로 구현했으며, 에이전틱 루프, 컨텍스트 로딩, 도구 호출 등 핵심 기능을 재현했다. 이 프로젝트는 AI 코딩 에이전트의 아키텍처를 학습하는 교육적 가치가 있으며, 오픈소스 AI 코딩 도구 생태계에 기여할 수 있는 시작점이 된다.

`#AI` `#ClaudeCode` `#OpenSource` `#Python` `#AgenticCoding`

### 3. [Claude Code 내부 동작 방식 완전 해부 — Agentic Loop부터 컨텍스트 로딩까지](https://news.hada.io/topic?id=28062)

Claude Code가 터미널에서 어떻게 동작하는지 공식 문서 기준으로 핵심을 정리한 글. "읽고 → 생각하고 → 도구 쓰고 → 결과 보고"라는 에이전틱 루프의 구조, 컨텍스트 로딩 방식(CLAUDE.md, 프로젝트 파일 등), 도구 호출 메커니즘, 그리고 사용자 승인 흐름까지 상세히 분석한다. AI 코딩 에이전트를 이해하거나 직접 구현하고자 하는 개발자에게 필수적인 참고 자료다.

`#AI` `#ClaudeCode` `#Architecture` `#AgenticLoop`

### 4. [Axios NPM 해킹 — 악성 버전에서 RAT 배포](https://news.hada.io/topic?id=28047)

널리 사용되는 axios HTTP 클라이언트의 두 악성 버전이 npm에 게시되어 원격 접근 트로이목마(RAT)를 배포한 사건. 공격자는 유지관리자 계정 자격 증명을 탈취하여 GitHub Actions를 우회하고 수동으로 악성 패키지를 업로드했다. 주당 1억 회 이상 다운로드되는 라이브러리인 만큼 피해 범위가 상당할 수 있으며, npm 생태계의 공급망 보안 취약성을 극명하게 드러낸 사건이다.

`#Security` `#NPM` `#SupplyChain` `#Malware`

### 5. [Ollama, 이제 Apple Silicon에서 MLX 기반으로 구동](https://news.hada.io/topic?id=28049)

Apple MLX 프레임워크를 기반으로 한 Ollama의 프리뷰 버전이 공개되었다. Apple Silicon의 통합 메모리 아키텍처를 활용하여 성능이 크게 향상되었으며, M5 시리즈 칩의 GPU Neural Accelerator를 통해 TTFT(첫 토큰 생성 시간)과 초당 토큰 생성 속도가 개선되었다. 기존 llama.cpp 백엔드 대비 Apple 하드웨어에 더 최적화된 추론이 가능해졌으며, macOS에서 로컬 LLM을 운영하는 사용자에게 중요한 업데이트다.

`#AI` `#LLM` `#Apple` `#MLX` `#LocalAI`

### 6. [Qwen3.5-Omni: 텍스트·이미지·오디오·영상을 모두 처리하는 완전 옴니모달 LLM](https://news.hada.io/topic?id=28027)

Alibaba Qwen 팀이 텍스트·이미지·오디오·영상을 모두 이해하고 생성하는 최신 옴니모달 모델을 공개했다. Thinker-Talker 아키텍처에 Hybrid-Attention MoE를 적용해 전 모달리티 처리 능력을 대폭 강화했으며, Plus·Flash·Light 3가지 크기의 Instruct 버전을 제공한다. 256k 롱컨텍스트 입력과 10시간 이상의 오디오 처리를 지원하며, GPT-4o/Gemini와 경쟁하는 오픈소스 옴니모달 모델로서의 위상을 구축했다.

`#AI` `#MultiModal` `#Qwen` `#OpenSource` `#LLM`

### 7. [Shopify의 데이터 구조화 여정: One-Shot LLM에서 DSPy 기반 에이전틱 아키텍처로](https://news.hada.io/topic?id=28022)

Shopify가 수백만 개의 비정형 커머스 데이터를 구조화하기 위해 단순 LLM 호출에서 DSPy 기반 멀티 에이전트 아키텍처로 전환한 과정을 상세히 설명한다. GPT-4/5급 대형 모델 대신 자체 호스팅된 Qwen(32B/72B급) 모델과 DSPy 최적화를 조합하여 비용을 절감하면서도 정확도를 높였다. 대규모 프로덕션 환경에서 에이전틱 AI를 실제로 적용한 귀중한 사례로, AInD 실무에 직접 참고할 수 있는 내용이다.

`#AI` `#DSPy` `#MultiAgent` `#Shopify` `#Production`

### 8. [Wikipedia, AI 글쓰기 전면 금지 — 40대 2 표결](https://news.hada.io/topic?id=28033)

Wikipedia가 AI(LLM)를 이용한 글쓰기와 수정을 전면 금지하는 정책을 도입했다. 수백 명의 자원봉사 에디터들이 참여한 토론 끝에 40대 2라는 압도적 찬성으로 통과되었다. LLM이 생성하는 텍스트의 환각(hallucination) 문제와 출처 날조, 그리고 인간 편집자의 검증 부담 증가가 주요 금지 사유다. 세계 최대 지식 플랫폼의 이 결정은 AI 생성 콘텐츠의 신뢰성에 대한 중요한 사회적 신호이다.

`#AI` `#Wikipedia` `#ContentPolicy` `#Trust`

### 9. [Microsoft Copilot이 약 150만개 GitHub Pull Request에 광고 삽입](https://news.hada.io/topic?id=28030)

AI 서비스의 수익화 압박이 심화되면서, GitHub Copilot이 자동 생성한 Pull Request 설명에 "Raycast로 Copilot 코딩 에이전트 실행" 등의 광고 문구를 삽입하는 사례가 다수 확인되었다. 약 150만 개의 PR에 영향을 미친 것으로 추정되며, 개발 도구에 광고가 침투하는 전례 없는 사태로 개발자 커뮤니티의 강한 반발을 사고 있다. AI 도구의 수익 모델과 사용자 신뢰 사이의 균형 문제를 극명하게 보여준다.

`#GitHub` `#Copilot` `#Advertising` `#DevTools`

### 10. [OpenAI의 Claude Code용 Codex 플러그인](https://news.hada.io/topic?id=28023)

OpenAI가 Claude Code 안에서 자사의 Codex를 직접 호출할 수 있는 플러그인을 출시했다. `/codex:review`, `/codex:adversarial-review` 등 슬래시 커맨드 기반으로 코드 리뷰 및 작업 위임이 가능하며, 백그라운드 작업 관리 기능도 포함한다. 경쟁사 도구에 자사 서비스를 플러그인으로 제공하는 이례적인 전략으로, AI 코딩 도구 생태계에서 "플랫폼화"보다 "유비쿼터스 접근"을 택한 흥미로운 움직임이다.

`#AI` `#OpenAI` `#Codex` `#ClaudeCode` `#Plugin`

### 11. [Claude Code의 숨겨진 강력한 기능들 15가지](https://news.hada.io/topic?id=28021)

Claude Code 제작자 Boris Cherny가 모바일 앱 Code 탭, 자동 스케줄링, 세션 포크, 병렬 워크트리 등 잘 알려지지 않은 기능 15가지를 정리했다. `--teleport` 명령으로 세션 간 이동, iOS/Android에서 코드 작성, 그리고 병렬 Git 워크트리를 활용한 동시 개발 등 생산성을 크게 높일 수 있는 기능들이 포함되어 있다. Claude Code를 이미 사용 중인 개발자라면 반드시 확인해볼 만한 내용이다.

`#AI` `#ClaudeCode` `#Productivity` `#Tips`

### 12. [Apple Silicon M4·M5 칩에서 외부 4K 디스플레이 HiDPI 해상도 제한](https://news.hada.io/topic?id=28068)

M4·M5 세대 Mac에서 외부 4K 모니터 연결 시 3840×2160@2x HiDPI 모드가 지원되지 않고 최대 3360×1890까지만 가능한 문제가 보고되었다. 이 제한은 하드웨어 성능 문제가 아니라 Display Coprocessor(DCP) 펌웨어 구조 변경으로 인한 것이다. 4K 모니터를 외부 디스플레이로 사용하는 개발자들에게 작업 환경에 직접 영향을 미치는 문제로, Apple의 수정 대응 여부가 주목된다.

`#Apple` `#Display` `#HiDPI` `#Hardware`

### 13. [PDF 논문 RAG, 텍스트만으로 충분할까? — Gemini embedding 002 실험](https://news.hada.io/topic?id=28037)

Gemini embedding-2-preview(네이티브 멀티모달 임베딩)로 학술 논문 PDF의 텍스트 임베딩과 이미지 임베딩을 비교 실험한 결과. 같은 페이지의 텍스트↔이미지 코사인 유사도 평균이 0.642로, SEM 사진, 그래프 곡선, 공간 배치 등 약 36%의 시각 정보가 텍스트 임베딩에 반영되지 않는다는 결론이다. 논문 RAG 시스템 구축 시 텍스트만으로는 불충분하며, 멀티모달 임베딩이 필요하다는 실증적 근거를 제시한다.

`#AI` `#RAG` `#Embedding` `#MultiModal` `#Research`

### 14. [한국 주식시장 특화 7B 에이전트 LLM — VELA](https://news.hada.io/topic?id=28056)

한국 증시(KOSPI+KOSDAQ) 특화 언어 모델 VELA가 공개되었다. Qwen2.5-7B-Instruct를 베이스로 SFT + DPO 파이프라인으로 파인튜닝했으며, 기존 금융 LLM에서 한국 시장 용어의 할루시네이션이나 언어 전환(language leak) 문제를 해결하는 데 초점을 맞췄다. 한국어 금융 도메인 특화 모델의 부족한 생태계에서 의미 있는 시도로, 투자 리서치 자동화에 활용 가능성이 있다.

`#AI` `#FinTech` `#Korean` `#FineTuning` `#LLM`

### 15. [civStation — Civilization VI를 VLM 기반으로 자동 플레이하는 에이전트](https://news.hada.io/topic?id=28042)

자연어 명령("동쪽으로 확장", "과학 승리")으로 Civilization VI를 플레이하는 computer-use VLM 하네스. Strategy/Action/HITL 3계층 구조로 전략과 실행을 분리하며, 고수준 의도를 실제 게임 조작으로 변환한다. Computer-use AI가 게임이라는 복잡한 환경에서 어떻게 동작하는지 보여주는 흥미로운 실험이며, 자연어 인터페이스를 통한 복잡한 소프트웨어 자동화의 가능성을 시사한다.

`#AI` `#ComputerUse` `#VLM` `#Gaming` `#Agent`

---

## GitHub Trending

> 오늘은 GitHub Trending 데이터가 수집되지 않았습니다.

---

*Generated: 2026-04-01 08:00 KST*
