# KeygraphHQ/shannon — AI 기반 자율 펜테스터

- **GitHub**: [KeygraphHQ/shannon](https://github.com/KeygraphHQ/shannon)
- **태그**: `#보안` `#펜테스팅` `#AI에이전트` `#OWASP`

## 상세 요약

Shannon은 Keygraph가 개발한 **자율적 화이트박스 AI 펜테스터**로, 웹 애플리케이션과 API의 소스 코드를 분석하여 공격 벡터를 식별하고 실제 익스플로잇을 실행하여 취약점을 증명한다.

**핵심 특징:**
- **완전 자율 운영**: 단일 명령어로 전체 펜테스트 실행. 2FA/TOTP 로그인, 브라우저 탐색, 익스플로잇, 보고서 생성까지 자동
- **재현 가능한 PoC**: 최종 보고서에는 실제로 익스플로잇된 취약점만 포함 (copy-paste PoC 제공)
- **OWASP 취약점 커버리지**: Injection, XSS, SSRF, Broken Auth 등
- **코드 인지 동적 테스팅**: 소스 코드 분석으로 공격 전략 수립, 실제 브라우저/CLI 기반 검증
- **통합 보안 도구**: Nmap, Subfinder, WhatWeb, Schemathesis 활용
- **병렬 처리**: 모든 공격 카테고리에서 취약점 분석과 익스플로잇을 동시 실행

OWASP Juice Shop에서 인증 우회, DB 유출 등 **20+ 취약점** 발견 실적.

**Pro 에디션:**
- Code Property Graph(CPG) 기반 에이전틱 정적 분석
- Data Flow Analysis, SCA with Reachability Analysis, Secrets Detection
- 비즈니스 로직 보안 테스팅 (패턴 기반 스캐너로는 불가능)

## Soo에게 의미 있는 이유

AI가 보안 테스팅을 자동화하는 실제 사례. AInD 컨설팅에서 "AI 에이전트가 코드를 쓰는 시대에 보안은 어떻게 할 것인가?"라는 질문에 대한 구체적 답변으로 제시 가능.
