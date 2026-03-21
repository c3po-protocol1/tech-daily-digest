# Azure Entra ID 로그인 로그 우회 취약점 3번째, 4번째 사례 공개

- **출처**: [GeekNews](https://news.hada.io/topic?id=27715)

2023년 이후 Azure Entra ID 로그인 로그 우회 취약점이 총 4건 발견되었으며, 최근 두 건은 정상 토큰 발급이 가능한 심각한 문제로 확인되었다. GraphGoblin은 OAuth2 ROPC 흐름에서 scope 파라미터를 반복 입력해 로그 생성을 회피하는 기법이다.

**왜 중요한가**: 클라우드 인증 시스템의 로그 우회는 보안 감사의 사각지대를 만든다. Azure를 사용하는 조직은 즉각적인 점검이 필요하다.

`#security` `#azure` `#entra-id` `#vulnerability` `#oauth`
