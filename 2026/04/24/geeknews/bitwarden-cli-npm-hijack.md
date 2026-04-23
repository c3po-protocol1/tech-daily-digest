# Bitwarden CLI npm 패키지 하이재킹 — 개발자 인증정보 대규모 탈취 공격

> **출처:** [research.jfrog.com](https://research.jfrog.com/post/bitwarden-cli-hijack/)
> **GeekNews:** [토론](https://news.hada.io/topic?id=28819) (3 points)
> **태그:** `#Security` `#SupplyChain` `#npm` `#Bitwarden`

## 요약

JFrog 보안 연구팀의 상세 기술 분석. Socket의 발견과 같은 사건이지만, 더 깊은 기술적 분석을 제공한다.

### 공격 체인 상세
1. `@bitwarden/cli 2026.4.0`이 하이재킹됨. 내부 메타데이터는 여전히 `2026.3.0`을 참조 — 기존 패키지 위에 악성 레이어 추가
2. `bw_setup.js` 로더가 Bun v1.3.13을 다운로드하여 `bw1.js` 실행
3. 3단계 수집기 동작: 파일시스템 수집기, 셸/환경 수집기, GitHub Actions Runner 수집기

### 수집 대상 (상세)
- SSH 키: `~/.ssh/id_*`, `known_hosts`
- Git: `.git/config`, `.git-credentials`
- npm: `~/.npmrc`, `.npmrc`
- AWS: `~/.aws/credentials`
- GCP: `~/.config/gcloud/credentials.db`
- **AI/MCP 설정**: `~/.claude.json`, `~/.claude/mcp.json`, `~/.kiro/settings/mcp.json`

### GitHub 무기화 상세
- `gh auth token` 실행하여 GitHub 토큰 직접 획득
- `LongLiveTheResistanceAgainstMachines` 커밋 검색으로 PAT 스테이징
- `beautifulcastle`으로 시작하는 서명된 커밋에서 대체 유출 도메인 복구
- 피해자 계정에 레포 생성 → 암호화된 결과 업로드
- GitHub Actions 시크릿 열거 → 워크플로우 주입 → 아티팩트 다운로드 → 증거 삭제

### 암호화 방식
AES-256-GCM + RSA-OAEP-SHA256으로 이중 암호화 후 전송. 정교한 수준.

## Soo에게 의미 있는 이유

동일 사건의 JFrog 분석으로, Socket 기사보다 기술적으로 더 깊다. 특히 **"수동적 탈취를 넘어 GitHub Actions를 통한 2차 공격"**이라는 점이 새롭다. AI 에이전트가 CI/CD에 깊이 통합되는 AInD 환경에서, 이런 공급망 공격의 blast radius가 기하급수적으로 커질 수 있다.
