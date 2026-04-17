# NIST, 대부분의 CVE 보강(enrichment) 포기

- **출처**: [Risky Business](https://risky.biz/risky-bulletin-nist-gives-up-enriching-most-cves/)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47806777) (154점, 37댓글)
- **태그**: `#보안` `#CVE` `#NIST` `#사이버보안`

## 요약

미국 국립표준기술연구소(NIST)가 NVD(National Vulnerability Database)의 새로운 정책을 발표했다. **앞으로는 중요한 취약점에 대해서만 enrichment(보강 데이터 추가)를 수행**하겠다는 것이다. 이는 사실상 항복 선언이다.

### 새 정책 핵심

NIST가 enrichment를 수행할 3가지 유형의 CVE:
1. **CISA KEV**에 등재된 취약점 (실제 악용되고 있는 버그)
2. **미국 연방 기관**이 사용하는 소프트웨어의 CVE
3. **"크리티컬 소프트웨어"**로 분류된 소프트웨어의 CVE (OS, 웹 브라우저, 보안 소프트웨어, 방화벽, 백업 소프트웨어, VPN 등)

### 배경

- 2024년 초부터 미보강 CVE가 2,100건에서 시작하여 연말에 **30,000건 가까이** 누적
- 트럼프 행정부의 DHS/CISA 예산 삭감으로 상황 악화
- 매년 **48,000건 이상**의 취약점이 CVE 번호를 받고 있으며, AI 보안 에이전트의 도입으로 이 숫자는 폭발적으로 증가할 전망

### 추가 변경사항

- NIST는 **자체 CVSS 심각도 점수 제공을 중단**하고, CVE를 발행한 조직의 초기 심각도 점수를 그대로 표시
- 이로 인해 소프트웨어 제조사가 자사 버그의 심각도를 **의도적으로 낮출 가능성** 증가 (수십 년간 반복된 패턴)

### 업계 반응

Aikido Security의 Sooraj Shah: *"더 이상 단일 진실 공급원은 없다(만약 존재한 적이 있었다면). NVD는 우선순위를 낮추고, EUVD는 초기 단계이며, MITRE 같은 CVE 프로그램도 자금 위기를 겪었다. 하나의 데이터베이스에 의존하는 시대는 공식적으로 끝났다."*

### 같은 뉴스레터의 주요 보안 소식들

- **OpenAI가 사이버 보안 전용 모델 GPT-5.4-Cyber 발표** — Anthropic의 Mythos/Glasswing에 대응
- **Anthropic이 Claude에 KYC(신원인증) 도입** — 셀카와 정부 ID로 사용자 확인
- **Thymeleaf RCE 취약점(CVE-2026-40478)** — Spring Boot의 기본 템플릿 엔진에 모든 버전에 영향
- **NGINX UI 버그 실전 악용 중** — MCP 엔드포인트를 통한 미인증 접근
- **Windows 제로데이 2건 연속 공개** — 불만 품은 연구자가 PoC 코드 공개

## Soo에게 의미 있는 이유

보안은 AInD 컨설팅에서 필수 고려사항이다. NVD의 사실상 항복은 **기업이 취약점 관리를 단일 소스에 의존할 수 없게 되었음**을 의미한다. AI 에이전트(Mythos 등)가 취약점 발견을 가속화하면서 CVE 수가 폭발할 것으로 예상되며, 이는 **AI 기반 보안 자동화**의 필요성을 더욱 높인다. 또한 OpenAI의 GPT-5.4-Cyber와 Anthropic의 Mythos 간 AI 보안 에이전트 경쟁이 본격화되고 있다.
