# emulate — 로컬에서 GitHub·Vercel·Google API를 완전 복제

- **출처:** [news.hada.io](https://news.hada.io/topic?id=27802)
- **태그:** `#DevTools` `#API` `#Testing` `#Vercel` `#Emulator` `#OfflineDev`

---

## 핵심 요약

Vercel에서 만든 **로컬 API 에뮬레이터**로, 단순한 mock이 아니라 실제 프로덕션과 동일한 상태·응답 구조를 가진 GitHub, Vercel, Google API를 로컬에서 실행할 수 있다. `npx emulate` 한 줄로 세 가지 서비스를 동시에 기동한다.

LocalStack이 계정 필수로 전환(어제 HN에서 논란)되면서, **계정 없이 사용 가능한 로컬 에뮬레이터**에 대한 수요가 증가하고 있다. emulate는 AWS가 아닌 GitHub/Vercel/Google을 대상으로 하지만, "API 의존성을 로컬에서 해결한다"는 같은 철학을 공유한다.

CI 파이프라인이나 네트워크 차단 환경에서의 개발·테스팅에 특히 유용하며, AI 에이전트가 이런 API를 호출하는 코드를 테스트할 때도 클라우드 비용 없이 로컬에서 검증할 수 있다.

## Soo에게 의미 있는 이유

AI 에이전트 개발 환경에서 외부 API 의존성을 로컬로 대체하는 것은 개발 속도와 비용 모두에 영향을 미친다. 컨설팅 시 개발 환경 구성 전략에 이런 에뮬레이터를 포함시키면 실용적이다.
