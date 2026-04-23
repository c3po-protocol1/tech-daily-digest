# Bitwarden CLI가 Checkmarx 공급망 공격에 의해 침해됨

> **출처:** [socket.dev](https://socket.dev/blog/bitwarden-cli-compromised)
> **HN 토론:** [Hacker News](https://news.ycombinator.com/item?id=47876043) (581 points)
> **태그:** `#Security` `#SupplyChain` `#npm` `#Bitwarden`

## 요약

Socket 보안 연구팀이 **Bitwarden CLI npm 패키지(@bitwarden/cli 2026.4.0)**가 진행 중인 **Checkmarx 공급망 캠페인**의 일환으로 침해되었음을 발견했다. Bitwarden은 1,000만 이상의 사용자와 50,000개 이상의 기업이 사용하는 패스워드 매니저다.

### 공격 메커니즘
- 정상 Bitwarden 메타데이터와 브랜딩을 유지하면서, `preinstall` 스크립트와 `bw` 바이너리 진입점을 악성 로더 `bw_setup.js`로 교체
- 로더는 **Bun v1.3.13 런타임**을 GitHub에서 다운로드하고, 대형 난독화된 JS 페이로드(`bw1.js`)를 실행
- 악성 코드는 `audit.checkmarx[.]cx/v1/telemetry` (IP: 94.154.172.43)로 데이터 전송

### 탈취 대상 자격 증명
GitHub/npm 토큰, SSH 키, AWS/GCP/Azure 자격 증명, 셸 히스토리, `.env` 파일, 그리고 주목할 만하게도 **Claude/MCP 설정 파일**(~/.claude.json, ~/.claude/mcp.json, ~/.kiro/settings/mcp.json)까지 표적으로 삼는다.

### GitHub 무기화
단순 토큰 탈취를 넘어, 탈취한 GitHub 토큰으로:
1. 커밋 검색으로 PAT 스테이징 (`LongLiveTheResistanceAgainstMachines` 마커)
2. 서명된 커밋 메시지에서 대체 유출 도메인 복구
3. 피해자 계정에 레포지토리 생성하여 암호화된 JSON 업로드
4. GitHub Actions 시크릿 열거, 워크플로우 주입으로 **추가 시크릿 추출**

### 특이 사항
- 러시아 로케일 킬 스위치: 시스템 로케일이 "ru"로 시작하면 자동 종료
- 듄(Dune) 시리즈 테마 네이밍: "Shai-Hulud", "Butlerian Jihad", "sardaukar", "fremen" 등
- 셸 프로파일 지속성: ~/.bashrc, ~/.zshrc에 페이로드 주입

### 대응 권고
- 영향받은 패키지 즉시 제거
- 노출 가능한 모든 자격 증명 교체
- GitHub 비인가 레포지토리 생성, Actions 워크플로우 변경 확인
- `/tmp/tmp.987654321.lock` 파일, 셸 프로파일 변조 확인

## Soo에게 의미 있는 이유

**AI 도구 설정 파일이 공급망 공격의 타겟이 되기 시작했다.** Claude/MCP 설정 파일을 명시적으로 수집하는 것은, AI 코딩 에이전트 환경이 새로운 공격 벡터가 되었음을 의미한다. AInD 컨설팅에서 보안 가이드라인을 수립할 때, 에이전트 설정 파일의 보안 관리가 필수 항목이 되어야 한다.
