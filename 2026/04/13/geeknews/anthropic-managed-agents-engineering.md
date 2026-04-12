# Anthropic — Managed Agents 확장: 두뇌와 손을 분리하기

> **출처**: [Anthropic Engineering Blog](https://www.anthropic.com/engineering/managed-agents) | [GeekNews 토론](https://news.hada.io/topic?id=28427)
> **점수**: 9점
> **태그**: `#AI에이전트` `#Anthropic` `#아키텍처` `#인프라` `#하네스`

## 요약

Anthropic이 장기 실행 에이전트를 위한 호스팅 서비스 **Managed Agents**의 아키텍처를 공개했다. 핵심 철학은 **"두뇌(brain)와 손(hands)을 분리하라"**이다.

**문제 — "반려동물 컨테이너":**
초기에는 세션, 하네스, 샌드박스를 하나의 컨테이너에 넣었다. 컨테이너가 실패하면 세션이 유실되고, 디버깅을 위해 사용자 데이터가 있는 컨테이너에 셸을 열어야 했다.

**해결 — 가상화 패턴:**
OS가 하드웨어를 process, file로 가상화한 것처럼, 에이전트 구성 요소를 가상화했다:
- **Session**: 이벤트의 append-only 로그 (세션 전체 기록)
- **Harness**: Claude를 호출하고 도구 호출을 라우팅하는 루프
- **Sandbox**: 코드 실행 및 파일 편집 환경

각 구성 요소가 독립적으로 교체 가능하며, 실패해도 다른 구성 요소에 영향을 주지 않는다.

**"두뇌와 손의 분리":**
- 하네스(두뇌)가 더 이상 컨테이너 안에 살지 않음
- 컨테이너(손)는 `execute(name, input) → string`으로 호출되는 도구에 불과
- 컨테이너가 죽으면 하네스가 오류를 Claude에게 전달, Claude가 재시도 결정
- 하네스도 소(cattle)가 됨 — 세션 로그가 분리되어 있으므로

**하네스 가정의 유통기한:**
Claude Sonnet 4.5에서 필요했던 "context anxiety" 대응 코드가 Opus 4.5에서는 필요 없어짐. 모델이 발전하면 하네스의 가정이 무효화되므로, **인터페이스가 구현보다 오래 지속되도록** 설계해야 한다.

## Soo에게 의미 있는 이유

에이전트 인프라 설계의 교과서적 사례. "Pets vs Cattle" 패턴을 에이전트 아키텍처에 적용하는 방법, 하네스와 실행 환경을 분리하는 이유를 명확히 보여준다. OpenClaw의 아키텍처가 나아갈 방향과도 맞닿아 있다. AInD 컨설팅에서 에이전트 인프라를 설명할 때 핵심 참고 자료.
