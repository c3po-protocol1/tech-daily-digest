# Git Bayesect — 비결정적 버그를 위한 베이지안 Git Bisection

- **출처**: [GitHub](https://github.com/hauntsaninja/git_bayesect)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47557921)
- **점수**: 163 points
- **태그**: `#Git` `#디버깅` `#베이지안` `#DevTools` `#오픈소스`

## 상세 요약

기존 `git bisect`는 결정적(deterministic) 버그에만 효과적이다. 하지만 현실에서는 "가끔 실패하는" flaky 테스트나 비결정적 버그가 흔하다. `git bayesect`는 베이지안 추론을 사용하여 이런 비결정적 변화를 감지하는 도구다.

**핵심 원리:**
- 베이지안 추론으로 변화를 도입한 커밋을 식별
- 예상 엔트로피의 탐욕적(greedy) 최소화를 통해 다음 테스트할 커밋을 선택
- Beta-Bernoulli 켤레 사전분포(conjugacy trick)를 활용해 미지의 실패율을 효율적으로 처리
- 실패 확률이 정확히 얼마인지 몰라도, "어떤 시점에서 뭔가가 변했다"는 것만으로 추적 가능

**주요 기능:**
- `git bayesect pass/fail` — 현재 커밋의 관찰 결과를 기록
- `git bayesect run <command>` — 자동으로 bisection 실행
- `git bayesect prior` — 특정 커밋에 사전확률 가중치 부여
- `git bayesect priors_from_filenames` — 파일명 기반 사전확률 설정 (의심스러운 파일에 가중치)
- `git bayesect priors_from_text` — 커밋 메시지/diff 텍스트 기반 사전확률 설정

**사용 예시:**
`priors_from_filenames`로 "suspicious" 단어가 포함된 파일을 수정한 커밋에 10배 가중치를 부여하거나, `priors_from_text`로 커밋 메시지에 "timeout"이 포함된 커밋에 가중치를 줄 수 있다.

## Soo에게 의미 있는 이유

AI 에이전트가 자동으로 코드를 수정하는 시대에, 비결정적 회귀 버그를 추적하는 도구는 매우 실용적이다. 특히 AI 코딩 에이전트의 자동 테스트/디버깅 파이프라인에 통합하면 효과적일 것이다. 베이지안 접근법 자체도 확률적 시스템을 다루는 AInD 실무에서 참고할 만한 패턴이다.
