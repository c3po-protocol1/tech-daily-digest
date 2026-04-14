# Claude Code Routines — 클라우드 자동화 기능 출시

- **출처**: [code.claude.com](https://code.claude.com/docs/en/routines)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47768133) (317 points, 203 comments)
- **태그**: #AI #ClaudeCode #자동화 #DevOps

## 상세 요약

Anthropic이 Claude Code에 **Routines** 기능을 리서치 프리뷰로 출시했다. Routines는 프롬프트, 레포지토리, 커넥터를 패키징하여 Anthropic의 클라우드 인프라에서 자동 실행되는 저장된 Claude Code 구성이다. 노트북을 닫아도 계속 작동한다.

**트리거 유형 3가지:**
- **Schedule**: 시간별, 일별, 주별 등 반복 실행. 크론 표현식 지원(최소 간격 1시간)
- **API**: HTTP POST 엔드포인트로 온디맨드 트리거. 알림 시스템, 배포 파이프라인 등에 연동
- **GitHub**: PR 생성, 푸시, 이슈, 워크플로우 실행 등 레포 이벤트에 반응

**실용 사례:**
- 백로그 유지보수: 매일 밤 이슈 트래커를 읽고 자동 라벨링, 담당자 배정, Slack 요약 전송
- 알림 분류: 에러 임계치 초과 시 스택 트레이스를 최근 커밋과 매칭하여 자동 PR 생성
- 맞춤 코드 리뷰: PR 생성 시 팀 고유 체크리스트 적용, 인라인 코멘트 자동 작성
- 배포 검증: 프로덕션 배포 후 스모크 체크, 에러 로그 스캔, go/no-go 판단
- 문서 드리프트 감지: 주간 단위로 머지된 PR의 API 변경 사항과 문서 불일치 탐지

**생성 방법:** 웹(claude.ai/code/routines), CLI(`/schedule`), Desktop 앱 세 곳에서 동일한 루틴 관리 가능. 루틴은 개인 계정에 귀속되며, GitHub 커밋이나 Slack 메시지 등은 사용자 계정으로 수행된다.

Pro, Max, Team, Enterprise 플랜에서 사용 가능하다.

## Soo에게 의미 있는 이유

AI 코딩 에이전트가 단발성 대화에서 **지속적인 자동화 워크플로우**로 진화하는 중요한 전환점이다. 스케줄 + API + GitHub 이벤트 트리거 조합은 기존 CI/CD와 AI 에이전트의 경계를 허문다. AInD 관점에서 "AI가 개발자를 대체하는 것"이 아니라 "AI가 개발 운영을 자동화하는 것"의 구체적 사례로 참고할 만하다.
