# Claude Advisor 전략 — Opus를 조언자로, Sonnet/Haiku를 실행자로 (상세 요약)

> **출처**: [Claude Blog](https://claude.com/blog/the-advisor-strategy)
> **발행일**: 2026년 4월 9일
> **태그**: `#AI` `#Claude` `#멀티모델` `#비용최적화` `#에이전트`

---

## TL;DR

- Anthropic이 **Advisor 전략**을 Claude Platform에 공식 도입
- Opus = 조언자(advisor), Sonnet/Haiku = 실행자(executor)
- 기존 서브에이전트 패턴의 **역전**: 작은 모델이 운전하고, 큰 모델은 필요할 때만 에스컬레이션
- Haiku + Opus 조합: 성능 **2배 이상** 향상, 비용 **85% 절감** (vs Sonnet 단독)
- API 한 줄 변경으로 적용 가능 (`advisor_20260301` 도구 추가)

---

## 1. Advisor 전략이란

### 1.1 핵심 구조

```
Executor (Sonnet/Haiku)  ──── 전체 작업 수행 ────→
     │                                              │
     │  해결 못 하는 결정에 부딪힘                      │
     ▼                                              │
Advisor (Opus)  ──── 계획/수정/중단 신호 반환 ────→   │
                                                    │
     ◄──── Executor가 재개하여 계속 실행 ─────────────┘
```

- **Executor (Sonnet/Haiku)**: 전체 작업을 end-to-end로 수행. 도구 호출, 결과 읽기, 반복
- **Advisor (Opus)**: 공유 컨텍스트에 접근하여 **계획(plan)**, **수정(correction)**, **중단 신호(stop signal)** 반환
- Advisor의 제약: **도구를 절대 호출하지 않고**, **사용자 대면 출력을 생성하지 않음**. 오직 executor에게 가이던스만 제공

### 1.2 기존 서브에이전트 패턴과의 핵심 차이

| 차원 | 기존 서브에이전트 | Advisor 전략 |
|------|-----------------|-------------|
| 주도권 | 큰 모델(오케스트레이터)이 운전 | **작은 모델(executor)이 운전** |
| 분해 | 큰 모델이 작업 분해 → 작은 모델에 위임 | 분해 없음. executor가 **통째로 수행** |
| 에스컬레이션 | 없음 (위→아래 단방향) | executor가 **필요할 때만** advisor에 에스컬레이션 |
| 오케스트레이션 | 워커 풀 + 오케스트레이션 로직 필요 | **불필요** |
| 프론티어 추론 비용 | 전체 실행에 걸쳐 발생 | **executor가 필요로 할 때만** 발생 |

핵심 통찰: **프론티어급 추론은 executor가 필요로 할 때만 적용되고, 나머지 실행은 executor급 비용으로 유지된다.**

---

## 2. 벤치마크 결과

### 2.1 Sonnet + Opus Advisor

| 벤치마크 | Sonnet 단독 | Sonnet + Advisor | 변화 |
|---------|------------|-----------------|------|
| SWE-bench Multilingual | baseline | **+2.7%p** | 성능 ↑ |
| 비용/태스크 | baseline | **-11.9%** | 비용 ↓ |
| BrowseComp | baseline | 향상 | 성능 ↑ |
| Terminal-Bench 2.0 | baseline | 향상 | 성능 ↑ |

→ **성능이 오르면서 비용도 내려가는** 드문 케이스

### 2.2 Haiku + Opus Advisor (가장 극적인 결과)

| 메트릭 | Haiku 단독 | Haiku + Advisor | vs Sonnet 단독 |
|--------|-----------|----------------|---------------|
| BrowseComp 점수 | 19.7% | **41.2%** (+109%) | -29% (점수) |
| 비용/태스크 | — | — | **-85%** (비용) |

→ Haiku + Advisor는 Sonnet 단독 대비 **점수 29% 부족이지만 비용 85% 절감**. 대량 처리 작업에서 **지능과 비용의 균형**이 필요할 때 강력한 선택지.

### 2.3 벤치마크 조건 상세

- **SWE-bench Multilingual**: Sonnet 단독은 adaptive thinking, Sonnet + Advisor는 thinking off. 둘 다 high effort, bash+file editing. 300문제×9개 언어, 5회 평균
- **BrowseComp**: thinking off, web search + web fetch. Sonnet은 medium effort. 1,266문제, 시도 1회
- **Terminal-Bench 2.0**: thinking off, bash + file editing. Sonnet은 medium effort. 격리 pod, 3x 자원, 1x 타임아웃. 89태스크, 5회 평균
- 모든 실험에서 advisor 모델: **Opus 4.6**

---

## 3. API 사용법

### 3.1 기본 구현

```python
response = client.messages.create(
    model="claude-sonnet-4-6",    # executor
    tools=[
        {
            "type": "advisor_20260301",
            "name": "advisor",
            "model": "claude-opus-4-6",
            "max_uses": 3,
        },
        # ... 기존 도구들
    ],
    messages=[...]
)
# Advisor 토큰은 usage 블록에서 별도 보고
```

### 3.2 핵심 특징

**단일 요청 내 핸드오프**: `/v1/messages` 요청 하나 안에서 모델 핸드오프가 일어남. **추가 라운드트립이나 컨텍스트 관리 불필요.**

**과금 방식**:
- Advisor 토큰 → advisor 모델(Opus) 요금으로 과금
- Executor 토큰 → executor 모델(Sonnet/Haiku) 요금으로 과금
- Advisor는 보통 **400-700 텍스트 토큰의 짧은 계획**만 생성 → 전체 비용이 advisor 모델 단독 실행보다 훨씬 낮음

**비용 제어**: `max_uses`로 요청당 advisor 호출 횟수 상한 설정. Advisor 토큰은 usage 블록에서 별도 추적 가능.

**기존 도구와 호환**: advisor tool은 Messages API 요청의 다른 도구 항목일 뿐. **웹 검색, 코드 실행, Opus 상담을 같은 루프에서** 수행 가능.

### 3.3 시작 방법

1. Beta 헤더 추가: `anthropic-beta: advisor-tool-2026-03-01`
2. `advisor_20260301`을 Messages API 요청에 추가
3. 사용 사례에 맞게 시스템 프롬프트 수정

**권장 평가**: Sonnet 단독, Sonnet + Advisor, Opus 단독으로 기존 eval suite를 돌려 비교

---

## 4. 사용자 피드백

> **Eric Simmons (Bolt CEO)**: "복잡한 태스크에서 더 나은 아키텍처 결정을 내리면서, 단순한 태스크에서는 오버헤드가 전혀 없다. 계획과 경로가 완전히 다른 수준."

> **Kay Zhu (Genspark CTO)**: "에이전트 턴, 도구 호출, 전체 점수에서 명확한 개선. 우리가 직접 만든 planning tool보다 낫다."

> **Anuraj Pandey (Eve Legal ML Engineer)**: "구조화된 문서 추출에서 advisor tool이 Haiku 4.5가 복잡도에 따라 Opus 4.6에 상담하여 동적으로 지능을 스케일링할 수 있게 한다. 프론티어 모델 수준 품질을 **5배 낮은 비용**으로."

---

## 5. 설계 원리 분석

### 5.1 왜 "역전"이 작동하는가

기존 패턴: Opus(오케스트레이터) → Sonnet/Haiku(워커)
- Opus가 **모든 턴**에 관여 → 전체 비용이 Opus급
- 오케스트레이션 로직 복잡

Advisor 패턴: Sonnet/Haiku(executor) → Opus(advisor)
- Opus는 **필요한 순간에만** 관여 → 대부분의 비용이 Sonnet/Haiku급
- 분해·위임 로직 불필요

**핵심**: 대부분의 에이전트 작업에서 "어려운 결정"은 소수이고, 나머지는 routine execution이다. Advisor 전략은 이 **비대칭성을 비용 구조에 반영**한다.

### 5.2 하네스 엔지니어링과의 관계

Advisor 전략은 **하네스 레벨의 설계 결정**이다:
- Fowler/Böckeler의 2×2 분류에서 **"비결정론적 피드백"** 사분면에 해당
- 에이전틱 패턴 4년 기록의 맥락에서: Ng의 **Reflection 패턴**의 진화형 — 같은 모델이 자기를 평가하는 대신 **더 강력한 모델이 평가**
- Anthropic 3-에이전트 아키텍처의 교훈("채점은 다른 사람이 해야 한다")을 **API 레벨에서 상품화**한 것

### 5.3 적용 시나리오

| 시나리오 | 추천 구성 | 이유 |
|---------|----------|------|
| 고품질 필수 + 비용 민감 | Sonnet + Opus Advisor | 성능↑ 비용↓ |
| 대량 처리 + 적당한 품질 | **Haiku + Opus Advisor** | 85% 비용 절감 |
| 최고 품질 필수 | Opus 단독 | advisor 오버헤드 없음 |
| 단순 작업 | Sonnet/Haiku 단독 | advisor 불필요 |

---

## Soo에게 의미 있는 이유

1. **AInD 비용 최적화 교과서**: 클라이언트에게 "AI 에이전트는 비싸다"는 우려에 대한 구체적 답변 — Haiku + Advisor로 **85% 비용 절감** 가능
2. **멀티모델 전략의 공식 표준**: 더 이상 자체 오케스트레이션 로직이 필요 없음. API 한 줄이면 됨
3. **Starforge에 직접 적용**: 하네스가 executor/advisor 모델을 선택할 수 있는 구조 → Starforge의 모델 라우팅 설계에 참조
4. **PoC 제안서 근거**: Bolt, Genspark, Eve Legal 등 실사용 기업의 피드백 인용 가능
5. **"역전된 서브에이전트"라는 프레이밍**: AInD 컨설팅에서 클라이언트에게 직관적으로 설명 가능한 개념

## 참고

- [Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) (2024.12)
- [Anthropic: Advisor Tool Docs](https://docs.anthropic.com/en/docs/agents-and-tools/advisor)
- [에이전틱 패턴 4년 기록 상세 요약](./2026-04-13-agentic-patterns-4-years-history.md)
