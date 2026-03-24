# Trivy GitHub Actions 태그 변조 — 공급망 공격으로 비밀정보 유출

- **출처:** [news.hada.io](https://news.hada.io/topic?id=27791)
- **태그:** `#Security` `#SupplyChain` `#GitHubActions` `#CICD` `#Trivy`

---

## 핵심 요약

보안 스캐닝 도구 Trivy의 공식 GitHub Action이 **태그 강제 업데이트(force push)**로 변조되어 악성코드가 배포되는 공급망 공격이 발생했다. 공격자는 76개 중 75개 태그를 악성 커밋으로 교체했으며, **약 1만 개 이상의 워크플로**가 영향을 받았다.

변조된 스크립트는 CI/CD 환경의 비밀정보(시크릿, 토큰, API 키)를 외부로 유출하는 것을 목적으로 했다. GitHub Actions의 **태그 기반 버전 관리의 구조적 취약점**을 악용한 공격으로, `uses: aquasecurity/trivy-action@v1` 같이 태그로 버전을 지정하면 해당 태그가 가리키는 커밋이 변경될 수 있다.

같은 날 LiteLLM PyPI 공급망 공격까지 겹치면서, AI/DevSecOps 도구 생태계의 공급망 보안이 심각한 상황에 처해 있음을 보여준다. 방어 전략으로는 **태그 대신 커밋 해시로 고정**, **Dependabot/Renovate로 자동 업데이트 관리**, **Actions의 최소 권한 원칙 적용** 등이 논의되고 있다.

어제(3/24) GitHub Trending에서 Trivy가 보안 스캐너로 트렌딩되었던 것과 아이러니하게 겹치는 사건이다.

## Soo에게 의미 있는 이유

CI/CD 파이프라인 보안은 AI 에이전트가 코드를 자동 생성하고 배포하는 환경에서 더욱 중요해진다. 에이전트 워크플로에 보안 스캔을 통합할 때, 그 보안 도구 자체가 공격받을 수 있다는 점을 인식해야 한다.
