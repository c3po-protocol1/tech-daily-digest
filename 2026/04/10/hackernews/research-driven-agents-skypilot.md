# Research-Driven Agents: 에이전트가 코드 전에 논문을 읽을 때

- **출처**: [SkyPilot Blog](https://blog.skypilot.co/research-driven-agents/)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47706141) (103 points, 38 comments)
- **태그**: `#ai-agents` `#llm-optimization` `#llama.cpp` `#autoresearch`

## 상세 요약

SkyPilot 팀이 Karpathy의 autoresearch 루프에 "문헌 조사 단계"를 추가한 실험 결과를 공개했다. 코드만 보는 에이전트는 피상적인 가설만 생성하지만, 논문과 경쟁 프로젝트를 먼저 조사한 에이전트는 근본적으로 다른 최적화를 시도한다.

**실험 설계:**
- 대상: llama.cpp CPU 추론 경로 (TinyLlama 1.1B, Q4_0 양자화)
- 인프라: AWS c6i.2xlarge (x86, AVX-512) + c7g.2xlarge (ARM, Graviton3) 각 4대
- 비용: ~$29 ($20 CPU VM + $9 API), ~3시간

**1차 시도 실패 (코드만 분석):** SIMD 마이크로 최적화 4개 시도 → 모두 노이즈 범위 내. 에이전트 자체 분석: "텍스트 생성은 메모리 대역폭 병목이지 연산 병목이 아니다."

**연구 단계 후 성공:** ik_llama.cpp 포크, FlashAttention 논문, Blockbuster 논문 등을 읽은 후 방향 전환. 30+ 실험 중 5개 성공:
1. Softmax 퓨전 (3패스→1패스)
2. RMS norm 퓨전
3. 적응형 from_float 병렬화
4. 그래프 수준 RMS_NORM+MUL 퓨전 (CUDA/Metal에만 있고 CPU에는 없던 것을 발견)
5. Flash Attention KQ 퓨전 (AVX2 FMA 단일 패스)

**결과:** x86에서 TG +15.1%, ARM에서 TG +5.0%. 분산도 크게 감소 (±19 → ±0.59 t/s).

**핵심 인사이트:** 포크 분석이 arxiv 검색보다 더 생산적이었다. 컴파일러와 하드웨어가 이미 하는 최적화를 에이전트가 예측하지 못하는 한계도 발견.

## Soo에게 의미 있는 이유

"코드만 보는 에이전트 vs 연구를 먼저 하는 에이전트"의 차이는 AInD에서 핵심 주제. 에이전트에게 더 좋은 컨텍스트를 주는 것이 결과를 근본적으로 바꾼다는 실증 데이터.
