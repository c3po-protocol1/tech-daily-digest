# Siri + Claude Code + Obsidian으로 만든 AI 베이비시터

- **출처:** [medium.com/@snowwhale](https://medium.com/@snowwhale/i-built-an-ai-babysitter-with-siri-claude-cowork-and-obsidian-82fc3adbfc7a)
- **GeekNews 토론:** [news.hada.io](https://news.hada.io/topic?id=27774) · ⬆️ 7
- **태그:** `#Siri` `#ClaudeCode` `#Obsidian` `#PersonalAI` `#Automation` `#Parenting`

---

## 핵심 요약

Apple의 Siri, Claude Code, 그리고 Obsidian 노트 앱을 결합하여 **육아를 보조하는 AI 시스템**을 구축한 개인 프로젝트가 공개되었다. 이 프로젝트는 AI의 "생활 밀착형 활용"이라는 관점에서, 기업이나 개발 환경을 넘어서 **일상 생활의 복잡한 문제를 AI로 해결**하려는 시도로서 의미가 있다.

시스템의 구조는 세 개의 계층으로 구성된다. **입력 계층(Siri)** — 부모가 음성으로 지시를 내린다. "아이가 열이 38.5도야", "오늘 이유식 뭐 먹였는지 기록해줘", "내일 소아과 예약 확인해줘" 등의 자연어 명령을 Siri가 수신한다. **처리 계층(Claude Code)** — Siri를 통해 전달된 명령을 Claude가 분석하고, 적절한 행동을 결정한다. 건강 기록 업데이트, 스케줄 확인, 이유식 레시피 추천 등을 수행한다. **저장/지식 계층(Obsidian)** — 모든 정보가 Obsidian vault에 마크다운 파일로 저장되어, 아이의 성장 기록, 건강 이력, 식단 로그 등이 검색 가능한 형태로 축적된다.

구체적 사용 시나리오가 인상적이다. 아이가 아플 때 과거 증상 기록과 투약 이력을 즉시 조회하여 소아과 방문 시 정확한 정보를 제공할 수 있다. 이유식 단계에 맞는 식재료 추천과 알레르기 유발 식품 경고를 자동으로 제공한다. 예방접종 스케줄을 관리하고 다가오는 접종을 미리 알려준다.

기술적으로 가장 흥미로운 점은 **Siri Shortcuts를 통한 음성→AI 파이프라인**의 구현이다. Apple의 Shortcuts 앱에서 Siri 트리거를 설정하고, HTTP 요청을 통해 로컬에서 실행 중인 Claude Code 인스턴스에 명령을 전달하는 구조이다. 이를 통해 손이 자유롭지 않은 육아 상황에서도 음성만으로 AI를 활용할 수 있다.

이 프로젝트가 보여주는 더 넓은 트렌드는 **"개인용 AI 에이전트 조립(Personal AI Agent Assembly)"**이다. 기존 도구들(Siri, Claude, Obsidian)을 레고 블록처럼 조합하여 자신만의 AI 시스템을 구축하는 것이 기술적으로 가능해졌으며, 이런 DIY AI 시스템이 상용 솔루션보다 개인의 특수한 니즈에 더 잘 맞을 수 있다.

## Soo에게 의미 있는 이유

AI의 "일상 생활 통합" 사례는 AInD 컨설팅에서 비기술적 청중에게 AI의 가치를 설명할 때 강력한 스토리텔링 소재가 된다. "AI가 코딩만 하는 게 아니라 육아도 돕는다"는 메시지는 AI에 대한 거부감을 줄이는 데 효과적이다.
