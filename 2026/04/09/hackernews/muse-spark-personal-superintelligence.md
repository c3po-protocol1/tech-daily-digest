# Meta, Muse Spark 발표 — "개인 초지능"을 향한 첫 걸음

- **출처:** [ai.meta.com](https://ai.meta.com/blog/introducing-muse-spark-msl/)
- **HN 토론:** [Hacker News](https://news.ycombinator.com/item?id=47692043) (229 points / 265 comments)
- **태그:** `#AI` `#Meta` `#멀티모달` `#강화학습` `#추론`

## 상세 요약

Meta Superintelligence Labs가 개발한 Muse 모델 패밀리의 첫 번째 모델. 네이티브 멀티모달 추론, 도구 사용, 비주얼 체인오브쏘트(Visual CoT), 멀티에이전트 오케스트레이션을 지원한다.

### 핵심 역량
- **Contemplating 모드:** 여러 에이전트가 병렬로 추론하는 오케스트레이션 시스템. Humanity's Last Exam 58%, FrontierScience Research 38% 달성 — Gemini Deep Think, GPT Pro급 극한 추론과 경쟁
- **멀티모달:** 시각 정보를 도구와 통합해 STEM 질문, 엔티티 인식, 로컬라이제이션에서 강한 성능. 홈 가전 고장 진단, 미니게임 생성 등 인터랙티브 경험 가능
- **헬스:** 1,000명 이상의 의사와 협업해 건강 추론 능력 강화. 영양 정보 시각화, 운동별 근육 활성화 표시 등

### 스케일링 축 3가지
1. **프리트레이닝:** 아키텍처·최적화·데이터 큐레이션 개선으로 Llama 4 Maverick 대비 **10배 이상 적은 컴퓨트**로 동일 성능 도달
2. **강화학습(RL):** pass@1과 pass@16 모두 로그-선형 성장. RL이 모델 신뢰성을 높이면서 추론 다양성은 유지
3. **테스트타임 추론:** Contemplating 모드로 테스트타임 컴퓨트 스케일링

### Hyperion 데이터센터
전체 스택 투자의 일환으로, Muse 시리즈 훈련을 위한 대규모 인프라 Hyperion 데이터센터 투자 병행.

## Soo에게 의미 있는 이유
Meta가 "개인 초지능(Personal Superintelligence)"이라는 비전을 공식화하고, 멀티에이전트 오케스트레이션(Contemplating 모드)을 모델 레벨에서 내장한 것이 주목할 만하다. AInD 컨설팅에서 멀티에이전트 패턴의 진화 방향을 이해하는 데 핵심 레퍼런스.
