# Whispree — 한국어 개발자를 위한 STT + LLM 교정 음성 입력 macOS 앱

- **출처**: [https://github.com/Arsture/whispree](https://github.com/Arsture/whispree)
- **GeekNews**: [https://news.hada.io/topic?id=28150](https://news.hada.io/topic?id=28150)
- **점수**: 19 points
- **태그**: `stt` `llm` `korean` `macos` `voice-input` `developer-tools`

## 상세 요약

한 대학생 개발자가 AI에게 지시를 내릴 때 타이핑이 병목이라는 문제를 해결하기 위해 만든 macOS 음성 입력 앱이다.

### 탄생 배경
- Superwhisper 등 기존 앱을 사용했으나 인식률이 답답하고, 유료화 비용 부담
- GPT를 이미 구독 중이므로 OAuth로 LLM을 빌려 쓸 수 있다는 발상
- STT는 Groq 같은 서비스로 거의 무료에 가깝게 사용 가능

### 핵심 동작
핫키 누르고 말하면 **STT → LLM 교정 → 원래 커서 위치에 자동 붙여넣기**. 녹음 중 다른 창을 봐도 처음 포커스 위치를 기억하여 정확히 삽입.

### 한국어 개발자 특화 교정
- "밸리데이션 해야 되거든" → "validation 해야 되거든"
- "랙트 컴포넌트" → "React 컴포넌트"
- "깃헙에 펄 올려놨어" → "GitHub에 PR 올려놨어"

### 고급 기능
- **구조화 모드**: 두서없는 말을 불릿포인트로 정리해주는 모드
- **화면 자동 캡처**: 녹음 중 보고 있는 화면을 자동으로 캡처하여 맥락 제공 (탭 전환 시 즉시 캡처, 1.5초 정지 시 자동 캡처)
- **교정 사전**: 자주 틀리는 단어를 사전에 핫키로 등록
- **STT 백엔드**: WhisperKit / Groq / MLX Audio 3종
- **LLM**: 로컬 6종(Qwen, GLM) + OpenAI 5종
- **교정 모드**: Standard / Filler Removal / Structured / Custom 4가지
- **설치**: `brew tap Arsture/whispree && brew install --cask whispree`
- **요구사항**: macOS 14+ (Sonoma), Apple Silicon 전용

## Soo에게 의미 있는 이유

한국어 개발자의 실제 pain point를 AI로 해결한 우수 사례. STT + LLM 파이프라인의 실용적 구현이며, 특히 개발자 맥락에서의 한/영 혼용 교정은 독창적이다. Codex CLI 인증 토큰 재활용 등 기존 구독을 활용하는 경제적 접근도 주목할 만하다.
