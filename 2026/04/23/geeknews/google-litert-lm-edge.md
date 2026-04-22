# Google LiteRT-LM — 엣지 디바이스용 고성능 LLM 추론 프레임워크

- **출처**: [GitHub](https://github.com/google-ai-edge/LiteRT-LM)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28758)
- **점수**: 10점 | 댓글 2개
- **태그**: `#Google` `#엣지AI` `#LLM` `#온디바이스` `#오픈소스`

## 상세 요약

Google이 만든 **프로덕션 수준의 온디바이스 LLM 추론 엔진** LiteRT-LM이 오픈소스로 공개되어 있다. Android, iOS, 웹, 데스크톱, IoT(Raspberry Pi) 등 엣지 환경 전반에서 대규모 언어 모델을 구동하는 프레임워크다.

**핵심 기능:**
- 📱 **크로스 플랫폼**: Android, iOS, Web, Desktop, IoT 지원
- 🚀 **하드웨어 가속**: GPU 및 NPU 활용
- 👁️ **멀티모달**: 비전, 오디오 입력 지원
- 🔧 **Tool Use**: 에이전틱 워크플로우를 위한 함수 호출 지원
- 📚 **광범위한 모델 지원**: Gemma, Llama, Phi-4, Qwen 등

**프로덕션 실적:**
- Google의 **Chrome, Chromebook Plus, Pixel Watch**에서 이미 사용 중
- Google AI Edge Gallery 앱으로 즉시 체험 가능

**지원 언어:**
- Kotlin (Android) ✅ Stable
- Python ✅ Stable
- C++ ✅ Stable
- Swift (iOS/macOS) 🚀 개발 중

**최신 업데이트: Gemma 4 지원**
```bash
litert-lm run \
   --from-huggingface-repo=litert-community/gemma-4-E2B-it-litert-lm \
   gemma-4-E2B-it.litertlm \
   --prompt="What is the capital of France?"
```

uv를 통한 코드 없이도 즉시 시작 가능하며, CLI만으로 엣지 디바이스에서 LLM을 실행할 수 있다.

## Soo에게 의미 있는 이유

엣지 AI는 AInD 컨설팅의 핵심 영역 중 하나가 될 것이다. 클라우드 의존도를 줄이고 프라이버시를 보장해야 하는 고객(금융, 의료, 제조)에게 온디바이스 LLM은 필수 제안이다. LiteRT-LM은 Google의 프로덕션 검증을 받은 유일한 오픈소스 엣지 추론 엔진.
