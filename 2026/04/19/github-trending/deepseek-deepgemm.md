# 🔥 DeepGEMM — DeepSeek의 통합 고성능 텐서 코어 커널 라이브러리

- **출처**: [GitHub](https://github.com/deepseek-ai/DeepGEMM)
- **태그**: `#CUDA` `#GPU` `#LLM` `#performance` `#DeepSeek`

## 상세 요약

DeepSeek이 공개한 통합 고성능 텐서 코어 커널 라이브러리. 현대 LLM의 핵심 연산 프리미티브를 하나의 CUDA 코드베이스로 통합했다.

**지원 연산:**
- **GEMM**: FP8, FP4, BF16 형식의 행렬 곱셈
- **Fused MoE**: 통신 오버랩이 적용된 Mixture-of-Experts (Mega MoE)
- **MQA Scoring**: Lightning Indexer용 다중 쿼리 어텐션 스코어링
- **HyperConnection (HC)**: 연결 최적화

**기술적 특징:**
- **JIT 컴파일**: 런타임 시 경량 Just-In-Time 모듈로 커널 컴파일 → 설치 시 CUDA 컴파일 불필요
- **CUTLASS/CuTe 개념 활용**: 그러나 무거운 템플릿/대수 의존 없이 깔끔하게 구현
- **핵심 커널 함수 수 제한**: 학습 및 이해가 쉬운 설계
- **H800에서 최대 1550 TFLOPS** 달성

**최신 업데이트 (2026.04.16):**
- Mega MoE, FP8xFP4 GEMM, FP4 Indexer, PDL 지원
- JIT 컴파일 속도 개선
- SM90/SM100 모두 지원

**요구사항:**
- NVIDIA SM90 or SM100 GPU
- CUDA 12.3+ (SM90), 12.9+ (SM100)
- PyTorch 2.1+, CUTLASS 4.0+

## Soo에게 의미 있는 이유

LLM 추론/학습의 핵심 하드웨어 최적화 라이브러리다. DeepSeek이 자사 모델의 성능을 끌어올리는 데 사용하는 실제 커널을 오픈소스로 공개한 것은 AI 인프라 이해에 매우 중요하다. 특히 FP4까지 지원하는 것은 양자화 트렌드의 최전선을 보여주며, "왜 DeepSeek 모델이 같은 하드웨어에서 더 효율적인가"의 답을 제공한다.
