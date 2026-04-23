# Google Cloud의 AI 에이전트 거버넌스 스택 — "에이전트를 엔지니어 조직처럼 관리하라"

> **출처:** [x.com/GoogleCloudTech](https://x.com/GoogleCloudTech/status/2047120160100860290)
> **GeekNews:** [토론](https://news.hada.io/topic?id=28810) (8 points)
> **태그:** `#AI` `#Agent` `#Governance` `#GoogleCloud` `#Security`

## 요약

Google Cloud가 Cloud Next 26에서 발표한 **Gemini Enterprise Agent Platform의 5계층 거버넌스 스택**이다. 핵심 철학: "에이전트 집단(fleet)을 엔지니어링 조직처럼 다루라."

### 5계층 구조

**1. Agent Identity (에이전트 아이덴티티)**
- 모든 에이전트에 고유 암호화 ID 부여
- 최소 권한 원칙(PoLP) 적용 — 에이전트별 테이블, 버킷, API 엔드포인트 세밀 지정
- 기존: 하나의 서비스 계정으로 전체 에이전트 운영 → 문제 추적 불가

**2. Agent Registry (에이전트 레지스트리)**
- 모든 에이전트, MCP 도구, 엔드포인트를 중앙 관리하는 카탈로그
- 기업 내부 npm 저장소와 유사. 승인된 도구만 프로덕션 사용 가능
- 취약점 패치 시 영향 범위 즉시 파악

**3. Agent Gateway (에이전트 게이트웨이)**
- 보안 정책을 **자연어로 작성** → 게이트웨이를 통과하는 모든 에이전트에 즉시 적용
- 50개 에이전트 개별 수정 불필요. 정책 하나로 전체 적용
- Model Armor 통합: 프롬프트 인젝션, 민감 데이터 유출 방어

**4. Anomaly & Threat Detection**
- 통계 모델로 정상 행동 기준선 설정, 이탈 시 경고
- **LLM-as-judge**: 별도 LLM이 에이전트 추론 과정 감사
- 리버스 셸, 악성 IP 연결, 권한 상승 시도 모니터링

**5. Agent Security Dashboard**
- Security Command Center 기반 통합 시각화
- 에이전트-모델 관계 매핑, 취약점 스캔, 계층 간 신호 상관 분석

### 차별점
자연어 정책 작성 + 전역 즉시 적용, LLM-as-a-judge 추론 감사는 기존 클라우드 보안과 구별되는 접근.

## Soo에게 의미 있는 이유

AInD 컨설팅에서 **에이전트 거버넌스**는 엔터프라이즈 고객의 최대 관심사다. Google의 5계층 프레임워크는 "에이전트를 엔지니어 조직처럼 관리하라"는 비유를 통해 경영진에게도 직관적으로 설명 가능한 모델을 제시한다. 이 프레임워크를 AInD 거버넌스 제안서의 레퍼런스로 활용할 수 있다.
