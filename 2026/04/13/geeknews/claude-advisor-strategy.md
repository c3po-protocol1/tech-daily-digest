# Advisor 전략: Opus를 조언자로 활용해 Sonnet의 지능을 끌어올리기

> **출처**: [Claude Blog](https://claude.com/blog/the-advisor-strategy) | [GeekNews 토론](https://news.hada.io/topic?id=28370)
> **점수**: 32점 | **댓글**: 1개
> **태그**: `#AI` `#Claude` `#멀티모델` `#비용최적화` `#에이전트`

## 요약

Anthropic이 Claude Platform에 **Advisor 전략**을 공식 도입했다. 핵심은 Opus를 조언자(advisor)로, Sonnet/Haiku를 실행자(executor)로 조합하는 것.

**작동 방식:**
- Sonnet/Haiku가 전체 작업을 수행하며 도구를 호출하고 반복
- 스스로 해결할 수 없는 결정에 부딪히면 **Opus에게 상담**
- Opus는 공유 컨텍스트에 접근해 계획, 수정, 중단 신호를 반환
- Opus는 절대 도구를 호출하거나 사용자 대면 출력을 생성하지 않음

**일반적인 서브에이전트 패턴과의 차이:**
기존: 큰 모델(오케스트레이터) → 작은 모델(워커)로 분해·위임
Advisor: **작은 모델이 운전**하고, 필요할 때만 큰 모델에 에스컬레이션

**벤치마크 결과:**
- Sonnet + Opus Advisor: SWE-bench Multilingual에서 Sonnet 단독 대비 **+2.7%p**, 비용 **-11.9%**
- Haiku + Opus Advisor: BrowseComp에서 19.7% → **41.2%** (2배 이상 향상), Sonnet 단독 대비 **85% 비용 절감**

**API 사용법:**
```python
response = client.messages.create(
    model="claude-sonnet-4-6",
    tools=[{"type": "advisor_20260301"}],
    ...
)
```
단일 `/v1/messages` 요청 안에서 모델 핸드오프가 일어남 — 추가 라운드트립 없음.

## Soo에게 의미 있는 이유

멀티모델 전략의 공식 표준이 된 중요한 발표. AInD 컨설팅에서 "비용 대비 성능 최적화"를 설명할 때 핵심 도구가 된다. 특히 Haiku + Opus 조합의 극적인 비용 절감(85%)은 대규모 에이전트 배포 시 실용적인 솔루션.
