# Claude Code Routines 공개 - 자동화 워크플로우

- **출처:** [code.claude.com](https://code.claude.com/docs/en/routines)
- **GeekNews:** [topic?id=28533](https://news.hada.io/topic?id=28533) (12P)
- **태그:** `#Claude` `#자동화` `#CI/CD` `#에이전트`

## 상세 요약

Anthropic이 Claude Code의 새로운 기능인 **Routines**를 공개했다. Claude Code를 자동 파일럿 모드로 실행할 수 있는 기능으로, Anthropic 관리 클라우드 인프라에서 실행된다.

**트리거 유형:**
- **스케줄:** 시간별, 매일, 평일, 매주 등 반복 실행
- **API:** HTTP POST로 온디맨드 트리거 (알림 시스템, 배포 파이프라인 연동)
- **GitHub:** PR, 푸시, 이슈, 워크플로우 실행 등 저장소 이벤트에 반응

**활용 사례:**
- 백로그 관리: 매일 밤 이슈 트래커를 읽고 라벨링, 할당, Slack 요약
- 알림 대응: 에러 임계값 초과 시 스택 트레이스 분석, 수정 PR 자동 생성
- 맞춤 코드 리뷰: PR 오픈 시 팀 체크리스트 적용, 인라인 코멘트
- 배포 검증: 프로덕션 배포 후 스모크 체크, 에러 로그 스캔
- 문서 드리프트: 주간 머지된 PR 스캔, API 변경 감지, 문서 업데이트 PR 생성
- 라이브러리 포팅: SDK 변경을 다른 언어로 자동 포팅

Pro, Max, Team, Enterprise 플랜에서 사용 가능. CLI의 `/schedule` 명령어로도 생성 가능.

## Soo에게 의미 있는 이유

AI 코딩 에이전트가 "대화형 도구"에서 "자동화 인프라"로 진화하는 중요한 이정표. Routines는 CI/CD와 AI 에이전트를 결합하는 새로운 패러다임을 제시한다. AInD 컨설팅에서 기업의 개발 자동화 전략에 직접 제안할 수 있는 기능이다.
