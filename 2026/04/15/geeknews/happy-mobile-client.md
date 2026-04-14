# Happy — Codex 및 Claude Code용 모바일/웹 클라이언트

- **출처**: [github.com/slopus/happy](https://github.com/slopus/happy)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28500) (18P, 댓글 6개)
- **태그**: #ClaudeCode #Codex #모바일 #원격제어

## 상세 요약

Claude Code와 Codex를 모바일(iOS/Android)과 웹에서 원격 제어할 수 있는 오픈소스 클라이언트다. MIT 라이선스, TypeScript 기반.

**핵심 기능:**
- CLI 래퍼 방식: `happy claude` / `happy codex`로 세션 시작 후 휴대폰에서 이어서 조작
- AI가 작업 중인 상태를 폰에서 실시간 확인 — 데스크톱 앞에 앉아있을 필요 없음
- 푸시 알림: 권한 요청이나 오류 발생 시 즉시 통보
- 엔드투엔드 암호화: 회사 코드가 평문으로 서버를 거치지 않음
- 셀프호스팅 릴레이 서버 옵션 제공

**프로젝트 구성:** Happy App(Expo 기반 웹/모바일), Happy CLI(커맨드라인), Happy Agent(원격 에이전트 제어), Happy Server(암호화 동기화 백엔드)

**사용법:** 앱스토어에서 앱 설치 → `npm install -g happy` → `happy claude`로 시작 → 바코드로 모바일 연동

## Soo에게 의미 있는 이유

AI 코딩 에이전트의 "비동기 작업" 패턴이 부상하고 있다. 에이전트가 작업하는 동안 개발자는 다른 일을 하다가 모바일로 진행상황을 확인하는 워크플로우. AInD에서 AI 에이전트의 UX 설계 시 참고할 패턴이다.
