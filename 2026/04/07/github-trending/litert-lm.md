# LiteRT-LM — Google의 엣지 디바이스용 LLM 추론 프레임워크

- **GitHub**: [google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM)
- **태그**: `#엣지AI` `#Gemma4` `#온디바이스` `#Google`

## 요약

Google의 프로덕션 레디 고성능 오픈소스 엣지 LLM 추론 프레임워크. Chrome, Chromebook Plus, Pixel Watch 등에서 실제 운영 중.

### 핵심 기능

- **크로스 플랫폼**: Android, iOS, Web, Desktop, IoT(Raspberry Pi)
- **하드웨어 가속**: GPU, NPU 가속기 지원
- **멀티모달**: 비전, 오디오 입력
- **Tool Use**: 에이전트 워크플로를 위한 함수 호출
- **폭넓은 모델 지원**: Gemma, Llama, Phi-4, Qwen 등

### Gemma 4 지원

```bash
litert-lm run --from-huggingface-repo=litert-community/gemma-4-E2B-it-litert-lm \
  gemma-4-E2B-it.litertlm --prompt="What is the capital of France?"
```

Linux, macOS, Windows(WSL), Raspberry Pi에서 CLI 실행 가능.

## Soo에게 의미 있는 이유

엣지 AI 추론의 표준이 될 가능성이 높은 프레임워크. 특히 Tool Use(함수 호출) 지원은 온디바이스 에이전트 구현의 핵심 요소로, AInD 컨설팅에서 IoT/모바일 AI 전략 수립 시 참고.
