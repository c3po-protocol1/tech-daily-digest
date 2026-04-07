# Project Glasswing: AI 시대의 핵심 소프트웨어 보안

- **출처:** https://www.anthropic.com/glasswing
- **HN 토론:** https://news.ycombinator.com/item?id=47679121
- **점수:** 728 points | 311 comments
- **태그:** `#AI` `#보안` `#Anthropic` `#사이버보안`

## 상세 요약

Anthropic이 AWS, Apple, Broadcom, Cisco, CrowdStrike, Google, JPMorganChase, Linux Foundation, Microsoft, NVIDIA, Palo Alto Networks와 함께 **Project Glasswing**을 발표했다. 이는 AI 시대에 세계에서 가장 중요한 소프트웨어를 보안하기 위한 대규모 이니셔티브다.

핵심은 Anthropic이 훈련한 미공개 프론티어 모델 **Claude Mythos Preview**다. 이 모델은 소프트웨어 취약점을 찾고 악용하는 능력에서 최고 수준의 인간 전문가를 제외하면 모두를 능가하는 수준에 도달했다. Mythos Preview는 이미 **모든 주요 운영체제와 웹 브라우저**에서 수천 개의 고위험 zero-day 취약점을 발견했다.

구체적 사례:
- **OpenBSD**에서 27년 된 취약점 발견 (원격으로 시스템 크래시 가능)
- **FFmpeg**에서 16년 된 취약점 발견 (자동 테스트 도구가 500만 번 실행해도 못 찾은 것)
- **Linux 커널**에서 여러 취약점을 연계하여 일반 사용자에서 완전한 시스템 제어 권한 획득

벤치마크 성과:
- SWE-bench Verified: 93.9% (Opus 4.6: 80.8%)
- Terminal-Bench 2.0: 82.0% (Opus 4.6: 65.4%)
- CyberGym: 83.1% (Opus 4.6: 66.6%)
- Humanity's Last Exam (도구 사용): 64.7% (Opus 4.6: 53.1%)

Anthropic은 Mythos Preview를 일반 공개할 계획은 없으며, 파트너들에게 **$100M의 사용 크레딧**을 제공한다. 가격은 $25/$125 per million input/output tokens. 오픈소스 보안을 위해 Linux Foundation에 $2.5M, Apache Software Foundation에 $1.5M을 기부했다.

## Soo에게 의미 있는 이유

AI 모델의 사이버보안 능력이 인간을 능가하기 시작한 전환점이다. AInD 컨설팅에서 "AI 보안" 영역이 필수 주제가 될 것이며, 기업 고객 대상 PoC에서 보안 관련 유즈케이스를 반드시 포함해야 한다. Mythos Preview의 벤치마크 수치는 현재 AI 모델 능력의 최전선을 보여준다.
