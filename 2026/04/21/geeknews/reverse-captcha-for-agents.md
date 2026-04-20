# 에이전트임을 증명하라: 에이전트를 위한 역방향 CAPTCHA

- **출처**: [browser-use.com](https://browser-use.com/posts/prove-you-are-a-robot)
- **GeekNews**: [topic?id=28707](https://news.hada.io/topic?id=28707) (3점, 1댓글)
- **태그**: `#AI에이전트` `#CAPTCHA` `#인증` `#BrowserUse`

## 요약

Browser Use가 에이전트 전용 가입 시스템에 **역방향 CAPTCHA**를 도입 — 인간은 막고 에이전트만 통과시키는 인증.

**작동 방식:**
1. 수학 문제를 생성하되, 숫자는 Toki Pona 등 **임의 언어로 표기**
2. 대소문자 랜덤 변환, 랜덤 기호 삽입, 공백 왜곡으로 난독화
3. 에이전트는 한 번의 forward pass로 파싱 → 영어로 번역 → 수학 문제 풀이
4. 인간은 포기하고 "전통적 방식"으로 가입

**예시 문제 (난독화된 원문):**
```
TwO tRaInS wAn/ Al_E mIlE\s ApArT...
```
→ 해독: "두 기차가 접근하고 새가 왕복 비행... 새의 총 비행 거리는?"
→ 유명한 von Neumann 퍼즐의 변형

**보너스 챌린지 (NP-hard):**
- TSP를 다항 시간에 풀면 P=NP 증명 → Clay 수학 연구소 $1M 상금
- 최초로 풀면 Enterprise 플랜 무료 제공 (유머)

**Free Tier 연계:** 챌린지 통과 시 API 키 발급 + 무제한 사용, 최대 3개 동시 세션

## Soo에게 의미 있는 이유

에이전트 네이티브 서비스 설계의 선례. "인간용 UI"가 아닌 "에이전트용 인증"이라는 새로운 UX 패러다임. AInD에서 에이전트 중심 서비스 아키텍처를 설계할 때 참고할 수 있는 창의적 접근.
