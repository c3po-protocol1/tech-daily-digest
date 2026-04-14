# damn-my-slow-kt — KT 인터넷 SLA 미달 자동 측정 & 감면 신청 도구

- **출처**: [github.com/kargnas](https://github.com/kargnas/damn-my-slow-kt)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28511) (40P, 댓글 15개)
- **태그**: #한국 #ISP #자동화 #오픈소스

## 상세 요약

KT 인터넷의 SLA(최저속도 보장제도)를 활용하여 매일 자동으로 속도를 측정하고, 계약 속도의 50% 미만일 경우 자동으로 이의신청까지 대행하는 오픈소스 도구다.

**핵심 메커니즘:**
- KT는 "매일 측정해야 매일 감면"되는 구조 → 30일 연속 미달 시 당월 요금 전액 감면 가능
- 하루 최대 10회(2시간 간격) 측정, 한 번이라도 성공하면 나머지 스킵
- `npx damn-my-slow-kt init` 원커맨드로 KT 계정 입력 → 스케줄 등록까지 완료

**기술 스택:** TypeScript + Commander + Playwright(headless Chromium) + node:sqlite. KT 홈페이지 로그인·측정·이의신청 UI를 자동화한다. Discord/Telegram 웹훅으로 측정 결과 알림 지원.

**약관 활용 전략:** 월 5일 이상 감면 시 할인반환금 없이 해약 가능하다는 조항까지 README에 명시.

**제한사항:** KT 공식 속도측정 프로그램이 Linux 미지원이라 Docker/NAS 환경은 불가, macOS에서만 검증됨.

GeekNews 댓글 반응이 뜨겁다. "KT가 이 툴을 싫어합니다", "규정을 변경할 것 같다", "로그인 방식을 바꿔서 시간을 벌 것" 등 한국 ISP 품질 문제에 대한 공감대가 크다.

## Soo에게 의미 있는 이유

Playwright 기반 웹 자동화의 실용적 사례이자, 소비자 권리 행사를 자동화하는 흥미로운 프로젝트다. AI 에이전트가 사용자 권리를 대리 행사하는 미래의 프리뷰이기도 하다.
