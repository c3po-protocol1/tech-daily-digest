# APM (Agent Package Manager) — Microsoft의 AI 에이전트 의존성 관리자

- **GitHub**: [microsoft/apm](https://github.com/microsoft/apm)
- **스타**: ⭐ 1,804 | **언어**: Python
- **태그**: `#Microsoft` `#에이전트` `#패키지매니저` `#DevTools`

## 요약

npm/pip/Cargo.toml과 같은 개념을 **AI 에이전트 설정**에 적용한 오픈소스 의존성 관리자. `apm.yml` 하나로 프로젝트의 에이전트 설정을 선언하면, 클론한 모든 개발자가 동일한 에이전트 환경을 자동 구성받는다.

### 핵심 기능

- **하나의 매니페스트**: instructions, skills, prompts, agents, hooks, plugins, MCP 서버
- **어디서든 설치**: GitHub, GitLab, Bitbucket, Azure DevOps 등
- **전이적 의존성**: 패키지가 패키지에 의존 가능, 전체 트리 해석
- **콘텐츠 보안**: `apm audit`로 숨겨진 유니코드 스캔, `apm install`로 손상된 패키지 차단
- **플러그인 저작**: Copilot, Claude, Cursor 플러그인을 의존성 관리와 보안 스캔과 함께 빌드
- **마켓플레이스**: 큐레이션된 레지스트리에서 원클릭 설치

### 설정 예시

```yaml
name: your-project
version: 1.0.0
dependencies:
  apm:
    - anthropics/skills/skills/frontend-design
    - github/awesome-copilot/plugins/context-engineering
    - microsoft/apm-sample-package#v1.0.0
```

```bash
git clone <org/repo> && cd <repo>
apm install    # 모든 에이전트 자동 구성
```

## Soo에게 의미 있는 이유

AI 에이전트 설정의 표준화와 재현성은 팀 단위 AI 도입에 필수적이다. APM은 "에이전트 구성을 코드처럼 관리"하는 접근법으로, AInD 컨설팅에서 **팀 에이전트 표준화 전략**을 설계할 때 핵심 도구가 될 수 있다.
