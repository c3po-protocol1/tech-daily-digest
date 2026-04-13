# 🎤 Voicebox — 오픈소스 음성 합성 스튜디오

- **저장소**: [jamiepine/voicebox](https://github.com/jamiepine/voicebox)
- **태그**: `#TTS` `#음성클로닝` `#오픈소스` `#로컬AI`

## 상세 요약

Voicebox는 ElevenLabs의 **무료 오픈소스 대안**을 표방하는 로컬 우선 음성 합성 스튜디오다.

**핵심 기능:**
- **5개 TTS 엔진**: Qwen3-TTS, LuxTTS, Chatterbox Multilingual, Chatterbox Turbo, HumeAI TADA
- **23개 언어** 지원 (영어, 한국어, 일본어, 아랍어 등)
- **음성 클로닝**: 몇 초의 오디오만으로 음성 복제
- **표현적 발화**: `[laugh]`, `[sigh]`, `[gasp]` 등 파라언어적 태그 지원
- **무제한 길이**: 자동 청킹 + 크로스페이드
- **스토리 에디터**: 멀티트랙 타임라인으로 대화, 팟캐스트, 내러티브 구성
- **후처리 효과**: 피치 시프트, 리버브, 딜레이, 코러스, 압축, 필터
- **API 우선**: REST API로 음성 합성을 자체 앱에 통합

**기술 스택:** Tauri(Rust) — Electron이 아닌 네이티브 성능

**실행 환경:** macOS(MLX/Metal), Windows(CUDA), Linux, AMD ROCm, Intel Arc, Docker

**프라이버시:** 모든 모델과 음성 데이터가 로컬에서 처리

## Soo에게 의미 있는 이유

ElevenLabs에 의존하지 않는 로컬 TTS 솔루션이다. 에이전트에 음성 기능을 추가하거나, 콘텐츠 생성 파이프라인에 음성을 포함할 때 비용 부담 없이 사용할 수 있다. 특히 한국어 지원이 있다는 점이 중요.
