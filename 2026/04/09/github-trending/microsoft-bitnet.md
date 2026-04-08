# microsoft/BitNet — 1비트 LLM 추론 프레임워크

- **GitHub:** [microsoft/BitNet](https://github.com/microsoft/BitNet)
- **태그:** `#1bitLLM` `#추론최적화` `#CPU` `#GPU` `#Microsoft`

## 상세 요약

1.58비트 LLM(BitNet b1.58) 공식 추론 프레임워크. CPU와 GPU에서 빠르고 무손실 추론을 지원.

### 성능 수치
- **ARM CPU:** 1.37x~5.07x 속도 향상, 55.4%~70.0% 에너지 절감
- **x86 CPU:** 2.37x~6.17x 속도 향상, 71.9%~82.2% 에너지 절감
- **최신 최적화:** 병렬 커널 + 타일링으로 추가 1.15x~2.1x 속도 향상
- **100B 모델을 단일 CPU에서 실행:** 사람 읽기 속도(5-7 tok/s) 달성

### 공식 모델
BitNet-b1.58-2B-4T (2.4B 파라미터) — HuggingFace에서 사용 가능.

### 기술 기반
llama.cpp 기반, T-MAC의 Lookup Table 방법론 활용.

### 로드맵
GPU 추론 지원 완료(2025.05), NPU 지원 예정.

## Soo에게 의미 있는 이유
로컬 디바이스에서 LLM을 실행하는 미래를 보여주는 프로젝트. AInD 컨설팅에서 "모든 기기에 AI"를 현실화하는 핵심 기술. 100B 모델이 단일 CPU에서 돌아간다는 것은 패러다임 전환.
