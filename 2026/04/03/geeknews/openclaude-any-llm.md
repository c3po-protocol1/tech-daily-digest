# OpenClaude — Claude Code 소스 유출 기반, GPT-4o/Gemini/Ollama 등 200+ 모델 지원

- **출처:** https://github.com/Gitlawb/openclaude
- **GeekNews:** https://news.hada.io/topic?id=28115
- **점수:** 16 points
- **태그:** #claude-code #open-source #multi-llm #fork

## 상세 요약

2026년 3월 31일 Claude Code의 npm 소스맵 유출을 기반으로 만들어진 OpenClaude는 Claude Code의 모든 도구(bash, 파일 읽기/쓰기/편집, grep, glob, 에이전트, 태스크, MCP)를 유지하면서 OpenAI 호환 API를 지원하는 프로바이더 심(shim)을 추가한 프로젝트다.

**지원 모델:** GPT-4o, DeepSeek, Gemini, Llama, Mistral 등 OpenAI 채팅 완성 API를 지원하는 모든 모델. ChatGPT Codex 백엔드도 codexplan/codexspark으로 지원하며, Apple Silicon에서 Atomic Chat을 통한 로컬 추론도 가능.

**설치:** `npm install -g @gitlawb/openclaude` 한 줄로 설치 후 `openclaude` 명령어로 실행. Windows, macOS, Linux 모두 지원. 비기술자용 설정 가이드, 고급 설정 가이드 등 다양한 문서 제공. 현재 7.3K 스타, 2.8K 포크.

## Soo에게 의미 있는 이유

Claude Code의 인터페이스와 도구 시스템이 우수하지만 Anthropic 모델에 락인되어 있다는 제약을 해소하는 프로젝트다. 다양한 LLM을 Claude Code와 동일한 에이전트 프레임워크에서 테스트할 수 있어, AInD 컨설팅에서 "모델 비교 평가"나 "벤더 락인 회피 전략"을 논의할 때 좋은 참고 사례가 된다.
