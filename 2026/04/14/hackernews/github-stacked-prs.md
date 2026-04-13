# 🔀 GitHub Stacked PRs — 대형 변경사항을 작고 리뷰 가능한 PR 체인으로

- **출처**: [github.github.com/gh-stack](https://github.github.com/gh-stack/)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47757495) (290 points, 184 comments)
- **태그**: `#GitHub` `#개발도구` `#코드리뷰` `#생산성`

## 상세 요약

GitHub가 **Stacked PRs**를 네이티브로 지원하는 기능을 프라이빗 프리뷰로 공개했다. 대규모 코드 변경을 여러 개의 작고 집중된 PR로 분리하여 순서대로 쌓아 올리는 방식이다.

**핵심 기능:**
- **`gh stack` CLI**: `gs init`, `gs add`, `gs push`, `gs submit` 명령으로 스택 생성/관리
- **GitHub UI 통합**: PR 페이지에 스택 맵이 표시되어 레이어 간 네비게이션 가능
- **캐스케이딩 리베이스**: 한 번의 클릭으로 전체 스택에 리베이스 적용
- **머지 큐 호환**: 각 PR을 개별 또는 머지 큐를 통해 병합 가능
- **브랜치 보호 규칙**: 최종 타겟 브랜치 기준으로 적용 (직접 베이스가 아닌)
- **AI 에이전트 통합**: `npx skills add github/gh-stack`으로 AI 코딩 에이전트에게 스택 작업 교육 가능

**왜 필요한가:** 대규모 PR은 리뷰가 어렵고, 머지가 느리며, 충돌이 발생하기 쉽다. 리뷰어가 컨텍스트를 잃고, 피드백 품질이 떨어지며, 팀 전체가 느려진다. Stacked PRs는 이를 체계적으로 해결한다.

현재 프라이빗 프리뷰 상태이며 [웨이트리스트 등록](https://gh.io/stacksbeta)이 가능하다.

## Soo에게 의미 있는 이유

AI 코딩 에이전트가 대규모 변경을 수행할 때 Stacked PRs는 필수적인 워크플로우가 될 것이다. R2-D2 같은 코딩 에이전트에게 "하나의 거대한 PR" 대신 "논리적 단위로 분리된 스택"을 생성하도록 하면 코드 리뷰 품질이 크게 향상된다. AInD 컨설팅에서 에이전트 개발 프로세스를 설계할 때 핵심 참고 사항.
