# Gemma 4를 Codex CLI에서 로컬 모델로 실행하기

- **출처**: [blog.danielvaughan.com](https://blog.danielvaughan.com/i-ran-gemma-4-as-a-local-model-in-codex-cli-7fda754dc0d4)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28510) (27P, 댓글 5개)
- **태그**: #Gemma4 #로컬LLM #CodingAgent #벤치마크

## 상세 요약

Gemma 4를 클라우드 대신 로컬 Codex CLI 환경에서 실행해 도구 호출 성능과 안정성을 검증한 실험 보고서다.

**테스트 환경:**
- Mac M4 Pro 24GB: 26B MoE 모델, llama.cpp 사용
- NVIDIA GB10 128GB: 31B Dense 모델, Ollama 사용
- 대조군: GPT-5.4 (클라우드)

**핵심 결과:**
- Gemma 3의 도구 호출 성공률 6.6% → Gemma 4에서 **86.4%**로 도약 (핵심 전환점)
- GPT-5.4: 65초에 5개 테스트 첫 시도 통과, 후속 정리 불필요
- GB10 31B: 7분 소요, 3번의 도구 호출로 5개 테스트 첫 시도 통과
- Mac 26B: 4분 42초이지만 10번의 도구 호출, 5번의 테스트 작성 실패, 데드 코드 잔존

**속도 분석:** Mac이 토큰 생성 5.1배 빠르지만(52 vs 10 tok/s), 최종 완료 시간은 30%만 단축. 이유는 "첫 시도 성공률"의 차이. 빠른 토큰보다 정확한 도구 호출이 더 중요하다.

**설정 팁:** Apple Silicon에서는 llama.cpp + `--jinja` 필수, Ollama는 Gemma 4 도구 호출 버그 있음. `web_search = "disabled"` 설정, 컨텍스트 32,768 필요, KV 캐시 양자화로 메모리 절약.

**결론:** 로컬 모델도 실무 수준 코드 생성이 가능해졌다. 하이브리드 접근 권장 — 반복 작업과 프라이버시 민감 작업은 로컬, 복잡한 작업은 클라우드.

## Soo에게 의미 있는 이유

로컬 LLM이 "에이전틱 코딩"에 실용적으로 사용 가능한 수준에 도달했음을 보여주는 중요한 벤치마크다. 기업 환경에서 코드를 외부에 보내지 않고도 AI 코딩 에이전트를 활용할 수 있는 가능성이 열렸다.
