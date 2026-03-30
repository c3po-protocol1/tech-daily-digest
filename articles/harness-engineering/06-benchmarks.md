# 6. Benchmarks — 벤치마크

> 모델이 아닌 harness 품질을 비교할 수 있는 벤치마크 모음.

---

## 6.1 HAL: Holistic Agent Leaderboard (Princeton)

**출처:** [hal.cs.princeton.edu](https://hal.cs.princeton.edu/)

프린스턴 대학의 에이전트 리더보드. **신뢰성, 비용, 범용성**을 함께 측정하여 end-to-end harness 행동을 비교하는 데 유용. 단순 정확도가 아닌 총체적 관점의 에이전트 평가.

## 6.2 OSWorld

**출처:** [os-world.github.io](https://os-world.github.io/)

Ubuntu, Windows, macOS에서 369개 작업을 수행하는 **실제 컴퓨터 사용 벤치마크**. 초기 상태 설정과 실행 기반 평가기가 포함되어, 데스크톱 및 멀티모달 harness 테스트에 탁월.

## 6.3 SWE-bench Verified

**출처:** [swebench.com](https://www.swebench.com/)

**실제 GitHub 이슈와 테스트**를 기반으로 한 소프트웨어 엔지니어링 에이전트 벤치마크. 코드 검색, 패치, 검증에 대한 harness 선택이 점수에 직접적으로 드러남. 코딩 에이전트 harness 비교의 사실상 표준.

## 6.4 AppWorld

**출처:** [appworld.dev](https://appworld.dev/)

앱과 사용자로 구성된 **제어 가능한 세계**에서 인터랙티브 코딩 에이전트를 벤치마킹. 상태 기반 + 실행 기반 유닛 테스트로 planning, 코드 생성, 부수 효과(collateral damage) 통제에 대한 harness 품질이 드러남.

## 6.5 AgentBench

**출처:** [github.com/THUDM/AgentBench](https://github.com/THUDM/AgentBench)

OS, 데이터베이스, 지식 그래프, 웹 브라우징 등 **다양한 환경**을 아우르는 벤치마크. harness가 하나의 좁은 작업 루프를 넘어 일반화되는지 확인하는 데 유용.

## 6.6 tau2-bench

**출처:** [github.com/sierra-research/tau2-bench](https://github.com/sierra-research/tau2-bench)

**현실적인 멀티 스텝** 에이전트 작업 벤치마크. 도구 사용과 실행 품질이 성공을 좌우하며, 단일 정답이 아닌 과정의 품질을 평가.

## 6.7 WebArena-Verified

**출처:** [github.com/ServiceNow/webarena-verified](https://github.com/ServiceNow/webarena-verified)

검증된 웹 에이전트 벤치마크. 큐레이션된 작업, 결정론적 평가기, 네트워크 trace 캡처로 **웹 대상 harness** 측정에 적합.

## 6.8 WorkArena

**출처:** [github.com/ServiceNow/WorkArena](https://github.com/ServiceNow/WorkArena)

일반적인 지식 작업(enterprise-style web workflows)에서 브라우저 에이전트를 벤치마킹. 토이 브라우저 작업이 아닌 **현실적 기업 워크플로우**에서 harness 비교 가능.

## 6.9 GAIA

**출처:** [huggingface.co/datasets/gaia-benchmark/GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA)

범용 AI 어시스턴트 벤치마크. 도구, planning, 검증, 장기 자율성에 대한 **harness 수준 선택**을 비교하는 데 자주 사용됨.

## 6.10 Terminal-Bench

**출처:** [tbench.ai](https://www.tbench.ai/)

셸, 파일시스템, 검증이 중요한 환경에서 **터미널 네이티브 에이전트**를 벤치마킹하는 스위트. 코딩 에이전트 harness 비교에 특히 유용.

## 6.11 Terminal-Bench 2.0 and Harbor

**출처:** [tbench.ai/news/announcement-2-0](https://www.tbench.ai/news/announcement-2-0)

Terminal-Bench 2.0 발표. 더 어려운 작업과 일반화된 평가 harness인 Harbor를 소개. Harbor는 대규모 에이전트 평가/개선을 위한 범용 harness 프레임워크.

---

### 벤치마크 선택 가이드

| 목적 | 추천 벤치마크 |
|------|-------------|
| 코딩 에이전트 harness 비교 | SWE-bench Verified, Terminal-Bench |
| 웹 에이전트 harness | WebArena-Verified, WorkArena |
| 범용 에이전트 | GAIA, HAL |
| 멀티 환경 일반화 | AgentBench, OSWorld |
| 멀티 스텝 작업 | tau2-bench, AppWorld |
