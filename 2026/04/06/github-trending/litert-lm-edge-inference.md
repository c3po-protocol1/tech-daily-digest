# LiteRT-LM: Google의 엣지 디바이스용 LLM 추론 프레임워크

- **출처**: [GitHub - google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM)
- **스타**: ⭐ 1,759 | **언어**: C++
- **태그**: `#온디바이스AI` `#추론엔진` `#Google` `#엣지컴퓨팅`

## 요약

Google의 프로덕션급 고성능 오픈소스 LLM 추론 프레임워크로, 엣지 디바이스에서의 대규모 언어 모델 배포를 위해 설계되었다.

### 핵심 특징

- **크로스 플랫폼**: Android, iOS, Web, Desktop, IoT(Raspberry Pi 포함)
- **하드웨어 가속**: GPU 및 NPU를 통한 최적 성능
- **멀티모달**: 비전 및 오디오 입력 지원
- **도구 사용(Tool Use)**: 에이전트 워크플로를 위한 함수 호출 지원
- **폭넓은 모델 지원**: Gemma, Llama, Phi-4, Qwen 등

### 프로덕션 실적

Chrome, Chromebook Plus, Pixel Watch 등 Google 제품에서 실제 사용 중. CLI로 코드 한 줄 없이 즉시 사용 가능.

### Gemma 4 지원

최신 Gemma 4를 Linux, macOS, Windows(WSL), Raspberry Pi에서 구동 가능.

## Soo에게 의미 있는 이유

온디바이스 AI 배포의 핵심 런타임. TensorFlow Lite의 후계자로서 실제 Google 프로덕트에서 검증된 기술이며, 엣지 AI PoC에 필수적인 인프라 도구다.
