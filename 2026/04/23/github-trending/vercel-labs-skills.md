# vercel-labs/skills — 오픈 에이전트 스킬 생태계 CLI

- **GitHub**: [vercel-labs/skills](https://github.com/vercel-labs/skills)
- **태그**: `#에이전트스킬` `#CLI` `#ClaudeCode` `#Codex` `#오픈소스`

## 상세 요약

Vercel Labs에서 만든 **오픈 에이전트 스킬 생태계를 위한 CLI 도구**. OpenCode, Claude Code, Codex, Cursor 등 **41개 이상의 에이전트**를 지원하며, 스킬을 설치/관리하는 통합 인터페이스를 제공한다.

**사용법:**
```bash
# GitHub에서 스킬 설치
npx skills add vercel-labs/agent-skills

# 특정 스킬만 설치
npx skills add vercel-labs/agent-skills --skill frontend-design

# 특정 에이전트에만 설치
npx skills add vercel-labs/agent-skills -a claude-code -a opencode

# 전체 스킬을 전체 에이전트에 설치
npx skills add vercel-labs/agent-skills --all
```

**지원 소스 형식:**
- GitHub shorthand (owner/repo)
- Full GitHub/GitLab URL
- 레포 내 특정 스킬 경로
- 로컬 경로

**옵션:**
- `--global`: 프로젝트 대신 사용자 디렉토리에 설치
- `--copy`: 심링크 대신 파일 복사
- `--list`: 설치 없이 가용 스킬 목록 확인
- `-y, --yes`: 확인 없이 설치 (CI/CD 친화)

에이전트 스킬의 **표준화된 설치/배포 인프라**를 목표로 하며, npm의 에이전트 스킬 버전.

## Soo에게 의미 있는 이유

OpenClaw의 ClawHub와 매우 유사한 포지셔닝. 에이전트 스킬 생태계가 여러 주체에서 동시에 발전하고 있음을 보여주며, 표준화 경쟁이 시작되었다. Soo의 에이전트 팀에서 이미 사용 중인 스킬 체계의 업계 방향성을 확인할 수 있다.
