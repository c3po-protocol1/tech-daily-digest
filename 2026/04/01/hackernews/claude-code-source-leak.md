# Claude Code 소스코드가 NPM 레지스트리 맵 파일을 통해 유출

- **출처:** [Twitter - @Fried_rice](https://twitter.com/Fried_rice/status/2038894956459290963)
- **HN 토론:** [Hacker News](https://news.ycombinator.com/item?id=47597531) · ⬆️ 1838
- **태그:** `#Security` `#AI` `#Claude` `#NPM` `#SourceLeak`

---

## 핵심 요약

Anthropic의 Claude Code CLI 도구의 전체 소스코드가 NPM 패키지에 포함된 `.map` (소스맵) 파일을 통해 외부에 유출되었다. 소스맵은 원래 디버깅 목적으로 번들링된 코드를 원본 소스에 매핑하는 파일인데, 빌드 과정에서 이를 제거하지 않고 NPM에 퍼블리시한 것이 원인이다. 

유출된 코드에서는 흥미로운 내부 메커니즘이 발견되었다:
- **"fake tools"** — 에이전트가 사용하는 가짜 도구들 (테스트/시뮬레이션 용도)
- **"frustration regexes"** — 사용자의 좌절 표현을 감지하는 정규식 패턴
- **"undercover mode"** — 정체를 숨기는 모드

1838점이라는 극도로 높은 점수는 이 사건이 AI 코딩 도구 커뮤니티에 미친 충격을 반영. NPM 패키지 배포 시 소스맵 제거의 중요성(`.npmignore`나 `files` 필드로 명시적 제외)과, AI 코딩 도구의 내부 동작 투명성에 대한 논의를 촉발.

## Soo에게 의미 있는 이유

AI 코딩 도구의 내부 구조가 공개됨으로써 harness 엔지니어링의 실제 구현을 학습할 수 있는 기회. "frustration regexes"는 에이전트가 사용자 경험을 어떻게 관리하는지, "fake tools"는 테스트 인프라를 어떻게 설계하는지 보여준다. 보안 관점에서 빌드 파이프라인 관리의 중요성도 시사.
