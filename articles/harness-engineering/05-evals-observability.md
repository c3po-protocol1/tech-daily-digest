# 5. Evals & Observability — 평가와 관측성

> 에이전트가 제대로 작동하는지 어떻게 측정하고 관찰하는가.

---

## 5.1 OpenAI — Testing Agent Skills Systematically with Evals

**출처:** [developers.openai.com](https://developers.openai.com/blog/eval-skills/)

### 핵심 내용

에이전트 trace를 **반복 가능한 eval**로 변환하는 OpenAI의 구체적 가이드.

**접근법:**
- 에이전트 실행 로그(JSONL)를 수집
- 각 trace에서 **성공/실패 기준**을 결정론적으로 판별
- 도구 호출 순서, 최종 결과, 부작용을 검증

**Eval 설계 원칙:**
- **결정론적 체크** 우선 — "파일이 생성되었는가", "테스트가 통과했는가"
- LLM 기반 판별은 보조적으로 사용 (비결정적)
- **회귀 탐지** — 새 harness 변경이 기존 성능을 깨뜨리지 않는지 확인

### 핵심 교훈
> "에이전트의 품질은 결과물만으로 판단하지 말고, trace 전체를 eval하라."

---

## 5.2 OpenAI — Agent Evals (Product Guide)

**출처:** [platform.openai.com](https://platform.openai.com/docs/guides/agent-evals)

### 핵심 내용

에이전트 품질을 **재현 가능한 task-level 및 workflow-level 평가**로 측정하는 OpenAI의 제품 가이드.

**두 가지 eval 수준:**
- **Task-level** — 단일 작업 완료 여부 (e.g., "버그를 고쳤는가?")
- **Workflow-level** — 전체 워크플로우의 효율성 (e.g., "몇 번 시도 만에 해결했는가, 비용은?")

**실용 가이드:**
- 테스트 케이스를 미리 작성하고 에이전트에게 풀게 함
- 결과를 자동으로 채점
- 시간 경과에 따른 성능 추이 추적

---

## 5.3 OpenAI — Evaluation Best Practices

**출처:** [platform.openai.com](https://platform.openai.com/docs/guides/evaluation-best-practices)

### 핵심 내용

현실 세계 분포에 맞는 eval suite를 구축하고 조기에 회귀를 잡는 일반 가이드.

**핵심 원칙:**
- Eval 데이터가 **실제 사용 패턴과 일치**해야 함
- 쉬운 케이스만 eval하면 실전에서 실패
- **에지 케이스, 모호한 케이스**를 포함해야 의미 있는 eval
- 정기적으로 eval suite를 업데이트 (데이터 노화 방지)

---

## 5.4 OpenAI — Trace Grading

**출처:** [platform.openai.com](https://platform.openai.com/docs/guides/trace-grading)

### 핵심 내용

에이전트 trace를 **직접 채점**하는 방법. 멀티 스텝 작업에서 특히 유용.

- 최종 결과만이 아닌 **중간 단계**도 채점 대상
- "올바른 도구를 올바른 순서로 호출했는가"
- "불필요한 탐색 없이 효율적으로 도달했는가"
- trace 채점으로 **harness의 어느 부분이 약한지** 진단 가능

---

## 5.5 Anthropic — Demystifying Evals for AI Agents

**출처:** [anthropic.com](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

### 핵심 내용

에이전트는 **성공/실패 경로가 다양**하므로 전통적 eval이 그대로 적용되지 않는다.

**에이전트 eval의 특수성:**
- 같은 작업에 여러 올바른 경로가 존재 — 단일 정답 비교 불가
- **과정도 중요** — 올바른 결과를 비효율적으로 얻는 것도 문제
- 환경 상태가 변하므로 **재현성 확보**가 어려움

**권장 접근:**
- 결과 기반(outcome-based) + 과정 기반(trajectory-based) 혼합
- 환경을 **스냅샷/리셋** 가능하게 설계
- 확률적 결과를 감안하여 **여러 번 실행 후 통계적 평가**

### 핵심 교훈
> "에이전트 eval은 '정답이 맞는가'가 아니라 '신뢰할 수 있는가'를 측정하는 것이다."

---

## 5.6 Anthropic — Quantifying Infrastructure Noise in Agentic Coding Evals

**출처:** [anthropic.com](https://www.anthropic.com/engineering/infrastructure-noise)

### 핵심 내용

**런타임 구성 변경만으로 벤치마크 점수가 리더보드 격차 이상으로 움직일 수 있다**는 충격적 발견.

**발견:**
- 같은 모델, 같은 harness에서 인프라 설정(타임아웃, 재시도 횟수, 샌드박스 구성)만 바꿔도 점수 변동
- 이 변동 폭이 **모델 간 차이보다 클 수 있음**
- 벤치마크 리더보드의 순위가 실질적으로 무의미할 수 있음을 시사

**실무 시사점:**
- 벤치마크 결과를 볼 때 **harness와 인프라 설정**을 반드시 확인
- 자체 eval 시 **인프라 변수를 고정**하지 않으면 결과가 노이즈에 묻힘
- A/B 테스트 시 인프라를 완전히 동일하게 유지해야 의미 있는 비교

### 핵심 교훈
> "모델 비교 전에 인프라 노이즈를 제거하라. 그렇지 않으면 인프라를 비교하는 것이지 모델을 비교하는 것이 아니다."

---

## 5.7 LangChain — Evaluating Deep Agents: Our Learnings

**출처:** [blog.langchain.com](https://blog.langchain.com/evaluating-deep-agents-our-learnings/)

### 핵심 내용

**단일 스텝, 전체 실행, 멀티턴** eval 설계에 대한 LangChain의 실전 경험.

**3가지 eval 레벨:**
1. **Single-step** — 개별 도구 호출/결정의 품질
2. **Full-run** — 전체 작업 완수 여부와 효율성
3. **Multi-turn** — 사용자와의 대화가 포함된 반복적 작업

**실전 교훈:**
- Single-step eval은 **빠르고 싸지만** 전체 품질을 대변하지 않음
- Full-run eval은 **비싸지만** 실제 사용자 경험에 가장 가까움
- 두 가지를 **조합**하여 효율성과 정확성 균형

---

## 5.8 LangChain — Improving Deep Agents with Harness Engineering

**출처:** [blog.langchain.com](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/)

### 핵심 내용

**Harness 변경만으로 벤치마크 성능이 유의미하게 개선**된다는 실증적 증거.

**발견:**
- 같은 모델에서 harness(프롬프트, 도구, 검증 로직)만 수정
- SWE-bench 등 벤치마크에서 **점수 대폭 상승**
- 모델을 바꾸지 않고도 **harness 개선만으로 모델 업그레이드 수준의 효과**

**구체적 개선 사례:**
- 도구 설명 개선 → 올바른 도구 선택률 향상
- 컨텍스트 관리 개선 → 장기 작업 성공률 향상
- 검증 루프 추가 → 최종 결과 품질 향상

### 핵심 교훈
> "더 좋은 모델을 기다리기 전에 harness를 개선하라. 비용 대비 효과가 훨씬 높다."
