# SuperGemma4 - 구글 Gemma 4 26B의 비검열/속도개선/양자화 모델

- **출처**: [HuggingFace](https://huggingface.co/Jiunsong/supergemma4-26b-uncensored-mlx-4bit-v2)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28584) (23 points)
- **태그**: `#AI` `#로컬LLM` `#Gemma` `#MLX` `#양자화`

## 상세 요약

Google Gemma 4 26B IT를 기반으로 한 **비검열/속도개선/양자화 모델**이 공개되었다. 애플 실리콘 MLX에 최적화된 4비트 양자화 버전으로, 약 **13GB** 크기다.

### 핵심 특징
- Gemma 4 26B IT를 기반으로 MLX 최적화 + 4비트 양자화한 텍스트 전용 모델
- 원본보다 더 스마트하고, 동일 머신에서 더 빠른 응답
- Safetensors 포맷, BF16·U32 텐서 지원
- `mlx_lm.server --model` 명령으로 OpenAI 호환 서빙 가능
- Ollama에서도 사용 가능 (0xIbra/supergemma4-26b-uncensored-gguf-v2)
- 31B 더 큰 모델도 별도 공개

### 주의사항
- 원본 Gemma 4와 라이선스가 다름 (Apache 2.0이 아님)
- `--chat-template`에 경로를 넣으면 응답이 손상될 수 있음

## Soo에게 의미 있는 이유
로컬에서 실행 가능한 비검열 모델의 등장은 기업 환경에서 민감한 데이터를 다룰 때 클라우드 의존 없이 AI를 활용할 수 있는 옵션을 제공한다. 특히 MLX 최적화는 Mac 기반 개발 환경에서 바로 활용 가능하다.
