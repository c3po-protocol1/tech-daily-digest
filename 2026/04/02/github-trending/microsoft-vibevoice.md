# microsoft/VibeVoice — Microsoft의 오픈소스 프론티어 음성 AI

- **GitHub**: [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice)
- **언어**: Python
- **태그**: `#음성AI` `#ASR` `#TTS` `#Microsoft` `#오픈소스`

## 상세 요약

Microsoft Research가 공개한 음성 AI 모델 패밀리로, TTS(텍스트→음성)와 ASR(음성→텍스트)을 모두 포함한다. 핵심 혁신은 7.5Hz 초저프레임률의 연속 음성 토크나이저(Acoustic + Semantic)로, 오디오 충실도를 유지하면서 긴 시퀀스 처리 효율을 극적으로 향상시킨다.

**VibeVoice-ASR:**
- 60분 긴 오디오를 단일 패스로 처리하는 통합 STT 모델
- "누가(Speaker), 언제(Timestamps), 무엇을(Content)"을 구조화하여 출력
- 50개 이상 언어 지원, 사용자 맞춤 핫워드 제공
- ASR + 화자분리(diarization) + 타임스탬핑을 한 번에 수행

**VibeVoice-TTS:**
- 90분 대화를 단일 패스로 합성
- 4명 다중 화자 지원, 자연스러운 턴테이킹
- ICLR 2026 Oral 논문으로 채택

**VibeVoice-Streaming (0.5B 모델):**
- 300ms 첫 음성 지연(First Audible Latency)의 실시간 TTS
- 스트리밍 텍스트 입력 지원
- 약 10분 장문 생성 가능
- 9개 다국어 음성 + 11개 영어 스타일 음성 지원 (한국어 포함)

**커뮤니티 채택:**
Vibing이라는 음성 입력 방식 프로젝트가 VibeVoice-ASR 위에 구축됨. Hugging Face Transformers에도 통합.

## Soo에게 의미 있는 이유

음성 AI의 최전선 기술을 오픈소스로 활용 가능. 특히 60분 단일 패스 ASR + 화자분리는 회의록 자동화, 고객 상담 분석 등 AInD 컨설팅 PoC에 즉시 적용 가능한 기술이다. 한국어 지원도 포함.
