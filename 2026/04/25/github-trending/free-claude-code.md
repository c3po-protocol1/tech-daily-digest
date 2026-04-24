# 🔥 free-claude-code — Claude Code를 무료로 사용하는 프록시 서버

- **GitHub**: [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)
- **스타**: 5,500+ ⭐ | **언어**: Python
- **태그**: `#ClaudeCode` `#프록시` `#무료` `#LLM` `#FastAPI`
- 🔥 2일 이상 연속 트렌딩

## 상세 요약

Claude Code의 터미널, VSCode 확장, Discord 인터페이스를 무료로 사용할 수 있게 해주는 프록시 서버 프로젝트다.

**동작 방식**: FastAPI 기반 서버가 Claude Code의 API 요청을 가로채, OpenAI 호환 프로바이더(OpenRouter, DeepSeek, LM Studio, llama.cpp 등)로 라우팅한다. Claude Code의 UI와 경험은 그대로 유지하면서 백엔드 모델만 교체하는 구조다.

**주요 기능**:
- **다중 프로바이더 지원**: OpenRouter, DeepSeek, NVIDIA NIM, LM Studio, llama.cpp 등
- **메시징 통합**: Discord, Telegram 봇을 통한 대화형 인터페이스
- **음성 노트**: Whisper 기반 음성 입력 지원
- **요청 최적화**: 네트워크 프로브, 제목 생성, 제안 모드 등 불필요한 요청을 로컬에서 처리하여 API 쿼터 절약
- **확장 가능한 아키텍처**: BaseProvider 또는 OpenAICompatibleProvider를 확장하여 새 프로바이더 추가 가능

**프로젝트 구조**:
```
server.py → api/ (라우트, 최적화) → providers/ (다중 LLM) → messaging/ (Discord/Telegram) → config/ → cli/
```

5,500개 이상의 스타와 936개의 포크가 이 프로젝트에 대한 높은 관심을 보여준다.

## Soo에게 의미 있는 이유

Claude Code의 개발 경험이 우수하지만 비용이 부담될 때, 오픈소스 모델로 백엔드를 교체하여 비용을 절감하는 패턴을 보여준다. 기업 고객에게 "AI 코딩 도구의 비용 최적화 전략"을 제안할 때 참고할 수 있다.
