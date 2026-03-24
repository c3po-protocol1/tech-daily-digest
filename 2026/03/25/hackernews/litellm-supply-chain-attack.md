# LiteLLM PyPI 패키지 공급망 공격 — AI 인프라의 보안 취약점

- **출처:** [github.com/BerriAI/litellm/issues/24512](https://github.com/BerriAI/litellm/issues/24512)
- **HN 토론:** ⬆️ 404+ · 💬 350+
- **태그:** `#Security` `#SupplyChain` `#Python` `#LLM` `#Critical`

---

## 핵심 요약

LLM API 프록시 라이브러리 LiteLLM의 PyPI 배포 버전 1.82.7과 1.82.8에 **공급망 공격(supply chain attack)**이 발생하여 악성 코드가 삽입된 것이 확인되었다. 해당 버전을 설치하면 환경 변수와 API 키 등 민감한 정보가 외부 서버로 유출된다.

LiteLLM은 OpenAI, Anthropic, Google 등 **100개 이상의 LLM API를 통합 관리**하는 인기 라이브러리로, AI 스타트업과 기업의 프로덕션 환경에서 광범위하게 사용되고 있다. 이 라이브러리가 관리하는 API 키의 가치를 생각하면 — OpenAI, Anthropic, Google 등의 유료 API 키 — 공격의 잠재적 피해 규모가 막대하다.

공격 벡터는 **PyPI 계정 탈취**로 추정된다. 공격자가 패키지 메인테이너의 PyPI 인증 정보를 탈취하고, 악성 코드가 포함된 새 버전을 배포한 것이다. 이런 공급망 공격은 최근 AI/ML 생태계에서 급증하고 있으며(어제 Trivy GitHub Actions 태그 변조 공격도 동시 발생), **AI 인프라의 공급망 보안**이 심각한 과제로 부상하고 있다.

HN에서 404점, 350개 댓글이 달린 것은 이 사건의 심각성을 반영한다. 즉각적 조치로 버전 확인, 해당 버전 사용 시 즉시 업데이트, 그리고 **모든 API 키 로테이션**이 권장된다. `pip install --upgrade litellm`으로 최신 안전 버전으로 업데이트해야 한다.

같은 날 GeekNews에서도 긴급 공유되었으며, Trivy GitHub Actions 공격까지 겹치면서 "AI 도구 생태계의 공급망 보안"이 오늘의 가장 중요한 주제가 되었다.

## Soo에게 의미 있는 이유

AInD 컨설팅에서 AI 도구 도입을 권고할 때, 공급망 보안은 보안팀이 가장 먼저 제기하는 우려이다. "AI 라이브러리가 해킹되면 모든 API 키가 유출된다"는 시나리오는 현실이 되었으며, 이에 대한 방어 전략(의존성 고정, SBOM 관리, 정기 감사)을 컨설팅에 포함시켜야 한다.
