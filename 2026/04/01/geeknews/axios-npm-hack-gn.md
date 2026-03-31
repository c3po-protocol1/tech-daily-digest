# Axios NPM 해킹 — 악성 버전에서 RAT 배포 (GeekNews)

- **출처:** [GeekNews](https://news.hada.io/topic?id=28047)
- **원문:** [HN 상세 분석 →](../hackernews/axios-npm-malware.md)
- **태그:** `#Security` `#NPM` `#SupplyChain` `#Malware`

---

## 핵심 요약

주당 1억 회 이상 다운로드되는 axios HTTP 클라이언트의 두 악성 버전(1.14.1, 0.30.4)이 npm에 게시되어 원격 접근 트로이목마(RAT)를 배포한 사건의 GeekNews 보도.

공격자는 주 관리자 `jasonsaayman`의 npm 계정을 탈취하고 이메일을 ProtonMail로 변경. GitHub Actions의 OIDC Trusted Publisher 메커니즘을 우회하여 수동으로 악성 패키지를 업로드. `npm install` 후 **2초 이내에** C&C 서버에 연결하며, 실행 후 자기 파괴하여 포렌식 탐지를 회피.

npm top-10 패키지에 대해 문서화된 공급망 공격 중 **가장 운영적으로 정교한 공격 중 하나**. 상세 기술 분석은 [HN 기사](../hackernews/axios-npm-malware.md) 참조.

## Soo에게 의미 있는 이유

AI 에이전트가 `npm install`을 실행하는 harness에서 공급망 공격의 위험성. 샌드박싱과 네트워크 격리의 필수성.
