# GitHub 99.9% 가용성도 버거운 모습 — 잦은 장애 우려

- **출처:** [news.hada.io](https://news.hada.io/topic?id=27793)
- **태그:** `#GitHub` `#Reliability` `#Infrastructure` `#DevOps` `#SPOF`

---

## 핵심 요약

GitHub의 잦은 서비스 장애가 이어지며 업계 표준 **'5 nines(99.999%)'는커녕 '3 nines(99.9%)' 달성도 어려운** 상황임을 분석한 글이다. 2월에는 Actions, Pull Request, 알림, Copilot 등 주요 기능이 동시 장애를 겪었다.

전 세계 개발자 인프라가 **단일 서비스(GitHub)에 과도하게 의존**하는 구조적 위험이 재조명되고 있다. GitHub가 다운되면 CI/CD 파이프라인이 멈추고, PR 리뷰가 중단되고, Copilot이 작동을 멈추며, 에이전트 기반 워크플로도 정지된다. 이는 전형적인 **SPOF(Single Point of Failure)** 문제이다.

AI 에이전트가 GitHub API에 의존하는 비율이 높아지면서(코드 커밋, PR 생성, 이슈 관리 등), GitHub 장애의 영향 범위가 인간 개발자를 넘어 **에이전트 워크플로 전체**로 확장되고 있다.

## Soo에게 의미 있는 이유

AInD 컨설팅에서 에이전트 워크플로를 설계할 때, 외부 서비스 의존성의 가용성 리스크를 고려해야 한다. GitHub 장애 시의 폴백(fallback) 전략, 멀티 Git 플랫폼 지원 등을 아키텍처에 포함시키는 것이 중요하다.
