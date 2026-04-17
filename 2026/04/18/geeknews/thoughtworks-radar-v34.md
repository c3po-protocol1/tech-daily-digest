# Thoughtworks Technology Radar Volume 34 공개

- **출처**: [thoughtworks.com/radar](https://www.thoughtworks.com/radar)
- **GeekNews**: [topic/28625](https://news.hada.io/topic?id=28625) (7P)
- **태그**: `#기술동향` `#에이전트` `#아키텍처` `#보안`

## 요약

Thoughtworks의 기술 레이더 34호가 공개되었다. 이번 호의 **4대 핵심 테마**는 모두 AI 에이전트 시대를 다루고 있다.

### 테마 1: 에이전트 시대와 기술 평가의 난제

- **시맨틱 확산(semantic diffusion)** 심화 — spec-driven development, harness engineering 등 용어 의미가 안정되기 전에 새 용어 등장
- 한 달도 안 된 도구들이 다수 등장, 일부는 단일 기여자가 코딩 에이전트와 함께 유지
- **코드베이스 인지 부채(Codebase Cognitive Debt)**: AI 생성 코드가 늘수록 작동 원리에 대한 멘탈 모델 없이 솔루션 채택 → 시스템 추론·디버깅 어려워짐

### 테마 2: 원칙 유지, 패턴 재검토

- **커맨드라인의 부활**: agentic 도구가 개발자를 터미널로 복귀시킴
- DORA 메트릭에 5번째 메트릭 **rework rate** 추가 — AI 생성 코드의 재작업 비율 측정
- "규율 없는 속도는 비용을 가중시킨다"

### 테마 3: 권한을 탐하는 에이전트의 보안 문제

- **"Permission hungry"** — 유용한 에이전트일수록 모든 것에 접근 필요
- Simon Willison의 **"lethal trifecta"**: 사적 데이터 + 비신뢰 콘텐츠 + 외부 행동 → 대부분의 유용한 에이전트에 기본 해당
- 안전한 에이전트 = 모놀리식이 아닌 **제약된 에이전트들의 파이프라인**

### 테마 4: 코딩 에이전트 하네스(harness)

- **Feedforward 통제**: Agent Skills, Superpowers, spec-driven development
- **Feedback 통제**: 컴파일러, 린터, 테스트 스위트를 에이전트 워크플로우에 직접 통합

### Adopt 등급 기법

- **Context engineering**: 프롬프트 엔지니어링을 넘어 컨텍스트 윈도우를 설계 표면으로 다루기
- **Curated shared instructions**: CLAUDE.md, AGENTS.md 같은 지시 파일을 팀 협업 자산으로 관리
- **DORA metrics**: AI 시대에 더 중요해진 딜리버리 메트릭

## Soo에게 의미 있는 이유

Technology Radar는 글로벌 기업들의 기술 도입 방향을 결정하는 영향력 있는 보고서다. 이번 호가 AI 에이전트에 집중한다는 것은 **AInD가 이제 주류 기술 전략의 핵심**임을 확인시켜준다. 특히 "context engineering", "coding agent harness", "Agent Skills"가 Adopt/Trial 등급으로 올라간 것은 Soo의 컨설팅 방향과 완전히 일치한다.
