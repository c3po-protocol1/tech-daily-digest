# 로컬 LLM 생태계에는 Ollama가 필요하지 않다

- **출처**: [Sleeping Robots](https://sleepingrobots.com/dreams/stop-using-ollama/)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28622)
- **포인트**: 26점
- **태그**: `#LLM` `#로컬AI` `#오픈소스` `#llama.cpp`

## 요약

Ollama가 로컬 LLM 실행을 대중화한 초기 공로는 인정하면서도, 현재 Ollama의 문제점을 체계적으로 비판하고 대안을 제시하는 심층 분석.

**주요 비판:**
1. **출처 은폐**: llama.cpp에 대한 크레딧을 1년 이상 누락. MIT 라이선스 의무인 저작권 표시도 미포함.
2. **포크 실패**: 2025년 중반 llama.cpp에서 분기하여 ggml 기반 자체 백엔드 구축 → 이미 해결된 버그 재발생. 성능도 llama.cpp 대비 **1.8배 느림** (161 vs 89 tok/s)
3. **모델명 오도**: DeepSeek R1 디스틸 모델을 "DeepSeek-R1"로 표시하여 사용자 혼란 유발
4. **클로즈드 소스 앱**: 2025년 7월 GUI 앱을 비공개 저장소에서 개발, 라이선스 없이 배포
5. **클라우드 전환**: 2025년 말 클라우드 호스팅 모델 도입, 로컬 AI의 취지 퇴색
6. **VC 패턴**: Y Combinator 투자 → 커뮤니티 신뢰 구축 → 벤더 락인 → 수익화

**추천 대안:**
- **llama.cpp**: 원본 엔진, OpenAI 호환 API, 일관되게 더 빠른 성능
- **llamafile**: 모델+런타임을 하나의 실행파일로 패키징
- **llama-swap**: 멀티 모델 오케스트레이션
- **Jan** (AGPLv3): 로컬 우선 채팅 앱
- **LM Studio**: 프로프라이어터리지만 llama.cpp를 정당하게 크레딧

## Soo에게 의미 있는 이유

로컬 AI 도구 선택 시 기술적 성능뿐 아니라 오픈소스 생태계의 건전성까지 고려해야 한다는 교훈. AInD 컨설팅에서 기업에 로컬 LLM 도입을 권고할 때 Ollama 대신 llama.cpp 직접 활용을 추천하는 근거가 된다.
