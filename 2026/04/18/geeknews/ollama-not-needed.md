# 로컬 LLM 생태계에는 Ollama가 필요하지 않다

- **출처**: [sleepingrobots.com](https://sleepingrobots.com/dreams/stop-using-ollama/)
- **GeekNews**: [topic/28622](https://news.hada.io/topic?id=28622) (18P)
- **태그**: `#LLM` `#로컬AI` `#Ollama` `#오픈소스`

## 요약

Ollama가 로컬 LLM 실행을 대중화했지만, 핵심 엔진인 **llama.cpp의 공로를 은폐**하고 **클라우드 중심 전환**으로 신뢰를 잃었다는 비판적 분석이다.

### Ollama의 주요 문제점

**1. llama.cpp 크레딧 은폐**
- Ollama의 추론 기능은 전적으로 Georgi Gerganov의 llama.cpp에 의존
- 1년 넘게 어디에도 llama.cpp 언급 없었고 MIT 라이선스 고지조차 누락
- 커뮤니티의 라이선스 준수 요청 이슈(#3185)는 400일 이상 무응답

**2. 자체 백엔드 전환과 성능 저하**
- 2025년 중반, llama.cpp 대신 ggml 기반 자체 구현체로 전환
- 커뮤니티 벤치마크에서 **llama.cpp가 Ollama보다 1.8배 빠름** (161 vs 89 tokens/s)
- Gerganov가 직접 "Ollama가 ggml을 잘못 포크했다"고 지적

**3. 모델 명칭 오도**
- DeepSeek-R1-Distill-Qwen-32B(축소 모델)을 단순히 "DeepSeek-R1"로 표기
- 실제 671B 모델이 아님에도 사용자들이 오해

**4. 폐쇄형 앱 출시**
- macOS/Windows GUI 앱을 비공개 저장소에서 개발, 소스 코드 비공개로 배포
- 오픈소스 이미지와 모순

**5. Modelfile의 비효율성**
- GGUF에 이미 포함된 정보를 중복 정의하는 불필요한 복잡성
- 파라미터 변경 시 30~60GB 모델 전체 복사 발생
- Go 템플릿 문법 사용으로 모델 제작자의 Jinja 템플릿과 불일치

### 대안 도구

- **llama.cpp**: 직접 빌드/실행, 최고 성능
- **LM Studio**: GUI 기반, 높은 투명성
- **Jan**: 오픈소스 대안

## Soo에게 의미 있는 이유

로컬 LLM 실행은 AInD 컨설팅에서 데이터 보안이 중요한 기업 클라이언트를 위한 핵심 옵션이다. Ollama의 문제점을 이해하고 llama.cpp 직접 사용이나 LM Studio 같은 대안을 알아두면, 클라이언트에게 더 적절한 로컬 AI 인프라를 추천할 수 있다.
