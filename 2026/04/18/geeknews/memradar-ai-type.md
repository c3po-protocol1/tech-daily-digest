# Memradar — AI와의 코딩 스타일을 분석해주는 오픈소스

- **출처**: [GitHub - on1659/memradar](https://github.com/on1659/memradar)
- **GeekNews**: [topic/28633](https://news.hada.io/topic?id=28633) (2P)
- **태그**: `#개발도구` `#분석` `#ClaudeCode` `#Codex`

## 요약

`npx memradar` 한 줄이면 PC의 Claude Code와 Codex 세션 로그를 스캔하여 **AI와의 코딩 스타일을 8가지 유형으로 분류**해주는 오픈소스 도구다.

### 3축 분류 체계

- **읽기형 vs 실행형**: 질문·탐색 위주인지, 코드 실행·수정 위주인지
- **깊이형 vs 넓이형**: 한 프로젝트를 파는지, 여러 개를 동시에 건드리는지
- **마라톤형 vs 스프린트형**: 긴 세션 몇 개인지, 짧은 세션 여러 개인지

### 기능

- Spotify Wrapped 스타일 Code Report 8장 이미지 저장
- 활동 히트맵, 시간대 차트, 워드 클라우드
- 세션 브라우저, 토큰·비용 통계
- 세션 데이터는 PC 밖으로 나가지 않음
- Node.js 18+ 기반, MIT 라이선스

### 기존 도구와의 차이

ccusage, claude-code-usage-monitor 등은 **토큰·비용 추적** 중심이지만, memradar는 **"내가 AI랑 어떤 식으로 일하고 있는지" 회고**에 초점을 맞춤.

## Soo에게 의미 있는 이유

AI 코딩 도구 사용 패턴 분석은 AInD 컨설팅에서 **개발자 생산성 측정**의 새로운 관점을 제공한다. 어떤 팀원이 어떤 스타일로 AI와 협업하는지 파악하면 교육·가이드라인 설계에 도움이 된다.
