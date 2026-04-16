# DFlash — Block Diffusion으로 Speculative Decoding 가속화

- **리포**: [z-lab/dflash](https://github.com/z-lab/dflash)
- **언어**: Python
- **⭐ Today**: 183 stars
- **태그**: `#AI` `#추론최적화` `#SpeculativeDecoding` `#LLM`

## 상세 요약

**Block Diffusion** 모델을 활용한 경량 speculative decoding 시스템. 효율적이고 고품질의 병렬 드래프팅을 가능하게 한다.

### 핵심 특징
- 다양한 모델 지원: Kimi-K2.5, Qwen3.5-4B/9B/27B/35B-A3B, gpt-oss-20b/120b 등
- 다중 백엔드: Transformers, SGLang, vLLM, MLX(Apple Silicon)
- 드래프트 모델 + 타겟 모델 조합으로 추론 속도 대폭 향상
- Speculative decoding으로 출력 품질 유지하면서 속도 개선

### 작동 원리
1. 경량 DFlash 드래프트 모델이 여러 토큰을 병렬로 예측
2. 타겟 모델이 이를 한 번에 검증
3. 수용된 토큰은 그대로 사용, 거부된 토큰만 재생성
4. 결과적으로 타겟 모델과 동일한 출력 품질, 더 빠른 속도

## Soo에게 의미 있는 이유
LLM 추론 비용 절감은 에이전트 시스템의 경제성에 직결된다. Speculative decoding이 실용화되면 에이전트의 대량 추론 호��� 비용을 크게 줄일 수 있다.
