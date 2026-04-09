# Ruff·uv 만든 Astral이 공개한 오픈소스 보안 전략 전모

- **출처**: [astral.sh](https://astral.sh/blog/open-source-security-at-astral)
- **GeekNews**: [토론](https://news.hada.io/topic?id=28340) (13 points)
- **태그**: `#security` `#open-source` `#supply-chain` `#ci-cd`

## 상세 요약

전 세계 수백만 개발자가 의존하는 Ruff, uv, ty를 만드는 Astral이 Trivy/LiteLLM 공급망 해킹 사건을 계기로 자신들의 보안 전략을 전면 공개했다.

**CI/CD 보안:**
- `pull_request_target`, `workflow_run` 같은 위험한 트리거를 조직 전체에서 금지
- 모든 액션을 특정 커밋에 핀 고정 (태그/브랜치가 아닌). impostor commit도 검증
- 워크플로우/잡 권한을 `permissions: {}`로 시작하고 잡별로만 확대
- 시크릿을 organization/repository 수준이 아닌 deployment environment별로 격리

**릴리스 보안:**
- Trusted Publishing으로 장기 레지스트리 크레덴셜 제거
- Sigstore 기반 어테스테이션으로 릴리스 아티팩트 ↔ 빌드 워크플로우 간 암호학적 검증 체인
- 릴리스 태그 생성을 deployment 성공 후에만 허용하는 tag protection ruleset
- 최소 2인 승인 + 강력한 2FA 필수

**의존성 보안:**
- 의존성 쿨다운(업데이트 직후 바로 적용하지 않음) — 일시적으로 변조된 패키지의 영향 최소화
- 업스트림과의 사회적 연결 유지 및 보안 기여

## Soo에게 의미 있는 이유

오픈소스 보안의 교과서적 사례. 공급망 공격이 일상화된 시대에 CI/CD 파이프라인 보안이 얼마나 복잡한지를 보여줌.
