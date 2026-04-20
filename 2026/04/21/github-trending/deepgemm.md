# DeepGEMM — DeepSeek의 고성능 텐서 코어 커널 라이브러리

- **GitHub**: [deepseek-ai/DeepGEMM](https://github.com/deepseek-ai/DeepGEMM)
- **태그**: `#CUDA` `#GPU최적화` `#LLM인프라` `#DeepSeek`
- 🔥 이전 다이제스트에서도 등장

## 요약

현대 LLM의 핵심 연산 프리미티브(FP8/FP4/BF16 GEMM, Fused MoE, MQA 등)를 단일 CUDA 코드베이스로 통합한 라이브러리. JIT 컴파일 방식으로 설치 시 CUDA 컴파일 불필요.

**최신 업데이트 (2026.04.16):**
- Mega MoE (통신 오버랩), FP8xFP4 GEMM, FP4 Indexer, PDL, 더 빠른 JIT 컴파일
- H800에서 최대 **1,550 TFLOPS** 달성
- SM90(Hopper) + SM100(Blackwell) 모두 지원

**설계 철학:** CUTLASS/CuTe 개념 활용하되 템플릿 의존 최소화 → 깨끗하고 학습하기 좋은 코드.

## Soo에게 의미 있는 이유

LLM 추론/훈련 인프라의 핵심 최적화 기술. AInD에서 GPU 활용 효율을 논의할 때 참고. DeepSeek의 오픈소스 전략 이해.
