# 모든 공개 Notion 페이지는 편집자 이메일 주소를 노출하고 있음

- **출처**: [Twitter/@weezerOSINT](https://twitter.com/weezerOSINT/status/2045849358462222720)
- **GeekNews**: [topic?id=28701](https://news.hada.io/topic?id=28701) (9점, 2댓글)
- **태그**: `#보안` `#Notion` `#PII유출` `#프라이버시`

## 요약

공개 Notion 페이지에서 편집자의 이름, 이메일, 프로필 사진이 **인증 없이** 노출되는 심각한 프라이버시 문제.

**재현 방법:**
- 공개 페이지의 블록 권한 정보에서 편집자 UUID가 인증 없이 반환됨
- `/api/v3/syncRecordValuesMain`에 UUID를 전달하면 이메일 주소 획득
- Notion Community 페이지에서 13개 사용자 ID 중 **12개 이메일 확인**
- 쿠키, 토큰, 인증 절차 **일체 불필요**

**영향 범위:**
- 500명 직원의 엔터프라이즈 워크스페이스가 공개 페이지 공유 시 **한 번의 요청으로 500개 이메일** 획득 가능
- Rate limiting 없음, 50명씩 배치 처리 가능
- `getLoginOptions` API로 비밀번호 로그인/SSO 여부까지 구분 가능
- **Credential stuffing의 무료 타깃 목록**으로 활용 가능

**타임라인:**
- 2022년 7월 최초 HackerOne 신고
- **약 4년간 미수정** — HackerOne에서 "informative"로 분류
- CVE 미부여, 버그 바운티 미지급
- Notion 측: 문서화돼 있고 경고 주지만 충분하지 않다고 인정, 이메일 프록시 방안 검토 중

## Soo에게 의미 있는 이유

많은 기업이 Notion을 위키, 채용 페이지, 온보딩 가이드 등으로 사용한다. AInD 컨설팅에서 기업 도구 보안 감사 시 반드시 점검해야 할 항목. 공개 페이지 사용 가이드라인 수립의 필요성.
