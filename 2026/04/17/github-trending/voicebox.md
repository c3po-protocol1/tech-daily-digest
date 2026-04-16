# Voicebox — 오픈소스 음성 합성 스튜디오

- **리포**: [jamiepine/voicebox](https://github.com/jamiepine/voicebox)
- **언어**: TypeScript
- **⭐ Today**: 887 stars
- **태그**: `#TTS` `#음성합성` `#오픈소스` `#로컬AI` `#ElevenLabs대안`

## 상세 요약

**ElevenLabs의 무료 오픈소스 대안**. 로컬에서 실행되는 음성 복제 스튜디오로, 몇 초의 오디오에서 음성을 복제하고 23개 언어로 음성을 생성한다.

### 핵심 기능
- **5개 TTS 엔진**: Qwen3-TTS, LuxTTS, Chatterbox Multilingual/Turbo, HumeAI TADA
- **23개 언어** 지원 (한국어 포함 가능)
- **음성 복제**: 몇 초의 오디오 샘플로 음성 복제
- **표현력 있는 음성**: `[laugh]`, `[sigh]`, `[gasp]` 등 부언어적 태그
- **후처리 이펙트**: 피치 시프트, 리버브, 딜레이, 코러스, 컴프레션
- **스토리 에디터**: 멀티트랙 타임라인으로 대화, 팟캐스트, 내러티브 구성
- **API-first**: REST API로 다른 프로젝트에 음성 합성 통합
- **Tauri(Rust) 기반**: Electron이 아닌 네이티브 성능
- **크로스 플랫폼**: macOS(MLX/Metal), Windows(CUDA), Linux, AMD ROCm, Intel Arc, Docker

### 완전한 프라이버시
모델과 음성 데이터가 모두 로컬에 유지. 클라우드 전송 없음.

## Soo에게 의미 있는 이유
ElevenLabs 같은 상용 TTS 서비스의 오픈소스 대안이 성숙해지고 있다. AInD 컨설팅에서 음성 AI를 포함하는 프로젝트 시, 비용과 프라이버시를 동시에 해결할 수 있는 옵션이다.
