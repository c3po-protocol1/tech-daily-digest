# VeraCrypt 프로젝트 업데이트 — Microsoft의 드라이버 서명 계정 말소 사태

- **출처:** [SourceForge](https://sourceforge.net/p/veracrypt/discussion/general/thread/9620d7a4b3/)
- **HN 토론:** [Hacker News](https://news.ycombinator.com/item?id=47686549) (1,095 points / 408 comments)
- **태그:** `#보안` `#암호화` `#오픈소스` `#Microsoft` `#디스크암호화`

## 상세 요약

VeraCrypt 개발자 Mounir IDRASSI가 몇 달간의 부재 후 공유한 프로젝트 상태 업데이트. 핵심 위기는 **Microsoft가 그의 Windows 드라이버 서명 계정을 사전 경고 없이 말소**한 것이다.

### 위기 상황
- Microsoft가 수년간 사용해온 드라이버 서명 계정을 일방적으로 종료
- 이메일이나 사전 경고 없음. "항소 불가"라는 메시지만 표시
- 여러 채널로 Microsoft에 연락했으나 자동 응답과 봇만 받음. 사람과 접촉 불가
- VeraCrypt 외 본업에도 영향

### 영향
- **Windows 업데이트 배포 불가** — VeraCrypt 사용자 대다수가 Windows
- Linux/macOS 업데이트는 가능하지만, Windows가 핵심 플랫폼
- 현재 버전 1.26.24는 곧 만료될 2011 CA로 서명됨 → Secure Boot에 영향
- 비시스템 볼륨 마운트, 포터블 사용에도 영향 우려

### 커뮤니티 반응
Reddit과 X에 상황을 공유하자는 제안, Microsoft 지원 페이지 링크 공유, 30일 넘으면 계정 복구 불가할 수 있다는 경고 등 활발한 논의.

## Soo에게 의미 있는 이유
오픈소스 프로젝트의 플랫폼 종속성 위험을 극명히 보여주는 사례. 코드 서명/배포 인프라가 단일 기업에 의존할 때의 리스크는 AI 에이전트 배포 전략에서도 동일하게 적용됨.
