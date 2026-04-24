# DeepSeek V4: 100만 토큰 컨텍스트, MoE 기반 대규모 언어 모델

- **출처**: [Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)
- **GeekNews**: [토론](https://news.hada.io/topic?id=28845) (6P)
- **태그**: `#DeepSeek` `#LLM` `#MoE` `#오픈소스` `#1M토큰`

## 상세 요약

DeepSeek이 V4 시리즈를 공개했다. 1M(100만) 토큰 컨텍스트를 지원하는 Mixture-of-Experts(MoE) 기반 대규모 언어 모델로, Pro와 Flash 두 가지 버전으로 제공된다.

**모델 사양**:
| 모델 | 총 파라미터 | 활성 파라미터 | 컨텍스트 | 정밀도 |
|------|-----------|------------|---------|--------|
| V4-Flash-Base | 284B | 13B | 1M | FP8 |
| V4-Flash | 284B | 13B | 1M | FP4+FP8 |
| V4-Pro-Base | 1.6T | 49B | 1M | FP8 |
| V4-Pro | 1.6T | 49B | 1M | FP4+FP8 |

**벤치마크 성능** (V4-Pro vs V3.2):
- MMLU: 90.1 (vs 87.8) — 세계 지식에서 큰 향상
- MMLU-Pro: 73.5 (vs 65.5) — 전문 지식에서 8점 상승
- Simple-QA: 55.2 (vs 28.3) — 사실 정확성 거의 2배
- FACTS Parametric: 62.6 (vs 27.1) — 파라메트릭 지식 대폭 향상
- HumanEval: 76.8 (vs 62.8) — 코딩 능력 14점 상승
- SuperGPQA: 53.9 (vs 45.0) — 전문가 수준 QA 향상

**기술적 특징**:
- FP4 + FP8 혼합 정밀도: MoE 전문가 파라미터는 FP4, 나머지는 FP8 사용
- Flash 모델은 13B 활성 파라미터로 효율적 추론 가능
- HuggingFace와 ModelScope에서 모두 다운로드 가능

## Soo에게 의미 있는 이유

DeepSeek V4는 오픈소스/오픈웨이트 모델의 경쟁력이 빠르게 향상되고 있음을 보여준다. 특히 1M 토큰 컨텍스트와 FP4 정밀도를 통한 효율적 추론은, 기업 환경에서 비용 효율적인 AI 배포를 고려할 때 중요한 옵션이다. 100만 토큰은 대규모 코드베이스 전체를 컨텍스트로 넣을 수 있는 수준이며, 에이전트 시스템에서의 활용 가능성이 크다.
