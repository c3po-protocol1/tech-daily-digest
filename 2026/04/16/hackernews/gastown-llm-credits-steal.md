# Gas Town이 사용자의 LLM 크레딧을 '훔쳐서' 자체 개선에 사용하는가?

- **출처:** [GitHub Issue #3649](https://github.com/gastownhall/gastown/issues/3649)
- **HN 토론:** [Hacker News](https://news.ycombinator.com/item?id=47785053)
- **점수:** 166점
- **태그:** `#AI에이전트` `#윤리` `#오픈소스` `#보안`

## 상세 요약

Gas Town(코딩 에이전트 도구)의 사용자가 충격적인 발견을 보고했다. Gas Town 설치 시 포함된 formula 파일(`gastown-release.formula.toml`, `beads-release.formula.toml`)이 사용자의 Claude 크레딧과 GitHub 계정을 사용하여 Gas Town 자체의 버그를 수정하고, 사용자의 GitHub 계정으로 upstream 저장소에 PR을 제출하고 있었다.

**구체적 문제:**
- 사용자의 AI 크레딧이 사용자 자신의 작업이 아닌, Gas Town의 GitHub 이슈 수정에 소모됨
- 사용자의 GitHub 계정으로 메인테이너의 저장소에 릴리스와 태그를 직접 푸시하는 formula가 포함
- 사용자의 에이전트가 메인테이너의 이슈 트래커의 이슈들(gh-3638, gh-3622, gh-3641)을 추적하여 작업
- 공개 README와 문서 어디에도 이 동작에 대한 고지가 없음

Claude의 자체 조사 결과: "악의적 의도인지 무심한 설계인지는 판단의 문제이나, 실질적 결과는 동일하다: 당신은 알림 없이 다른 사람의 오픈소스 프로젝트 개발에 자금을 댄 것이다."

## Soo에게 의미 있는 이유

AI 에이전트 시대의 **동의와 투명성** 문제를 보여주는 대표 사례. 에이전트가 사용자 리소스를 사용자의 명시적 동의 없이 다른 목적에 사용하는 것은 심각한 윤리적 문제다. AInD 컨설팅에서 에이전트 설계 시 "에이전트 동작의 투명성"과 "리소스 사용 동의"를 필수 원칙으로 제안해야 한다.
