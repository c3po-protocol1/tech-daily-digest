# Gemma 4 on iPhone: Google AI Edge Gallery 앱으로 온디바이스 LLM 실행

- **출처**: [App Store - Google AI Edge Gallery](https://apps.apple.com/nl/app/google-ai-edge-gallery/id6749645337)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47652561) (660 points, 184 comments)
- **태그**: `#Gemma4` `#온디바이스AI` `#모바일` `#Google`

## 요약

Google이 AI Edge Gallery 앱을 통해 **Gemma 4 모델을 iPhone에서 직접 실행**할 수 있게 했다. iOS 17.0 이상, Apple M1 칩 이상의 Mac에서도 동작하며, Android 12 이상도 지원한다.

### 핵심 기능

- **완전 오프라인 실행**: 인터넷 연결 없이 모든 추론이 디바이스에서 수행되어 완벽한 프라이버시 보장
- **Gemma 4 공식 지원**: 최신 Gemma 4 패밀리의 고급 추론, 논리, 창작 기능을 서버 전송 없이 테스트
- **Agent Skills**: 위키피디아 기반 사실 검증, 인터랙티브 맵, 비주얼 요약 카드 등으로 모델 기능 확장
- **Thinking Mode**: 모델의 단계별 추론 과정을 실시간으로 관찰 가능 (현재 Gemma 4 패밀리 지원)
- **멀티모달 지원**: 카메라나 사진으로 객체 인식, 비주얼 퍼즐 풀기, 상세 설명 생성
- **Audio Scribe**: 음성 녹음을 실시간 텍스트로 변환
- **벤치마크 기능**: 각 모델이 특정 하드웨어에서 어떤 성능을 내는지 직접 측정
- **모바일 액션**: FunctionGemma 270m 파인튠 기반의 오프라인 기기 제어 및 자동화

### 기술 기반

LiteRT(경량 런타임)를 사용하여 GPU/NPU 가속을 통한 최적화된 실행 성능을 제공하며, Hugging Face 통합으로 모델 검색 및 다운로드가 용이하다.

## Soo에게 의미 있는 이유

온디바이스 AI는 AInD 컨설팅에서 점점 중요한 주제가 되고 있다. 특히 프라이버시가 중요한 엔터프라이즈 환경에서 "서버 없이 로컬에서 AI를 돌릴 수 있다"는 것은 강력한 셀링 포인트다. Gemma 4의 모바일 배포가 이렇게 쉬워졌다는 것은 PoC 단계에서 클라이언트 데모용으로도 매우 유용하다.
