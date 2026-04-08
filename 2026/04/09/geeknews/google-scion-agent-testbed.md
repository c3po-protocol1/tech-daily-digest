# Google, 실험적 에이전트 오케스트레이션 테스트베드 Scion 오픈소스 공개

- **출처:** [googlecloudplatform.github.io](https://googlecloudplatform.github.io/scion/overview/)
- **GeekNews:** [topic?id=28307](https://news.hada.io/topic?id=28307) (8 points)
- **태그:** `#Google` `#에이전트오케스트레이션` `#오픈소스` `#컨테이너` `#멀티에이전트`

## 상세 요약

Google Cloud Platform이 공개한 실험적 멀티에이전트 오케스트레이션 테스트베드. 컨테이너 안에서 동시 실행되는 LLM 기반 에이전트들을 로컬과 원격 클러스터에 걸쳐 관리한다.

### 아키텍처: Manager-Worker
- **scion CLI:** 에이전트 수명주기 관리, Grove(프로젝트 워크스페이스) 관리, 템플릿 관리
- **Agents:** 격리된 런타임 컨테이너(Docker)에서 실행. Gemini CLI, Claude Code, OpenAI Codex 등 지원

### 핵심 특징
- **Profile/Runtime/Harness 시스템:** 로컬 Docker vs 원격 Kubernetes 등 환경 전환
- **격리된 아이덴티티:** 각 에이전트에 별도 자격증명·워크스페이스
- **동적 그래프 실행:** 리서치·코딩·감사·테스팅 등 태스크 병렬 실행
- **tmux 세션:** 에이전트와 인터랙티브 상호작용
- **Hub 서버:** 팀/조직 수준의 관리, PAT, Git 기반 Grove

### 지원 하네스
Gemini CLI, Claude Code, Codex 등 주요 코딩 에이전트를 "하네스"로 플러그인 형태 지원.

### 시작하기
```bash
scion init          # 프로젝트 루트에 .scion 디렉토리 생성
scion start <name> "<task>"  # 에이전트 실행
scion attach <name>  # 에이전트 세션 접속
scion logs <name>    # 출력 확인
scion resume <name>  # 상태 보존하며 재시작
```

## Soo에게 의미 있는 이유
Google이 멀티에이전트 오케스트레이션의 표준을 어떻게 정의하려는지 보여주는 프로젝트. 우리 OpenClaw 기반 시스템과 아키텍처적으로 비교할 좋은 레퍼런스.
