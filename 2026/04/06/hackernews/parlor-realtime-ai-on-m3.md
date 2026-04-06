# Parlor: M3 Pro에서 실시간 AI (오디오/비디오 입력 → 음성 출력)

- **출처**: [GitHub - fikrikarim/parlor](https://github.com/fikrikarim/parlor)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47652007) (103 points, 8 comments)
- **태그**: `#Gemma4` `#음성AI` `#멀티모달` `#로컬AI` `#오픈소스`

## 요약

Parlor는 Gemma 4 E2B 모델을 활용하여 **M3 Pro 맥북에서 실시간 음성+비전 AI를 구동**하는 오픈소스 프로젝트다. 기존에는 RTX 5090급 GPU가 필요했던 작업을 로컬 Mac에서 수행할 수 있게 되었다.

### 아키텍처

```
Browser (마이크 + 카메라)
    ↓ WebSocket (오디오 PCM + JPEG 프레임)
FastAPI 서버
├── Gemma 4 E2B (LiteRT-LM, GPU) → 음성+비전 이해
└── Kokoro TTS (MLX/Mac, ONNX/Linux) → 음성 합성
    ↓ WebSocket (스트리밍 오디오)
Browser (재생 + 트랜스크립트)
```

### 핵심 기능

- **브라우저 기반 음성 활성화 감지(VAD)**: Silero VAD를 사용하여 핸즈프리, 푸시투톡 불필요
- **Barge-in 지원**: AI가 말하는 도중에 끼어들기(인터럽트) 가능
- **문장 단위 TTS 스트리밍**: 전체 응답 생성 전에 오디오 재생 시작
- **약 3GB RAM**으로 동작, 모델 자동 다운로드 (~2.6GB)
- **Python 3.12+**, macOS Apple Silicon 또는 Linux GPU 지원

### 사용 목적

원래 언어 학습 앱(월간 활성 사용자 보유)의 서버 비용을 제거하기 위해 개발되었다. 몇 년 후에는 핸드폰에서도 이런 수준의 실시간 AI가 가능해질 것으로 전망하며, OpenAI가 몇 년 전에 데모한 것과 본질적으로 같은 기능을 오픈소스로 구현한 셈이다.

## Soo에게 의미 있는 이유

서버 비용 없는 실시간 멀티모달 AI의 실현은 엔터프라이즈 PoC에서 큰 의미가 있다. "GPU 서버 없이 로컬 맥에서 실시간 비전+음성 AI가 가능하다"는 것은 클라이언트 데모 시나리오에서 강력한 임팩트를 줄 수 있다.
