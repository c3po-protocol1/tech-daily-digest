# claw-code — Claude Code 유출 소스 기반 Python 클린룸 재작성 프로젝트

- **출처**: [GitHub](https://github.com/instructkr/claw-code)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28061)
- **태그**: `#ClaudeCode` `#Python` `#클린룸` `#오픈소스` `#에이전트`

## 상세 요약

Claude Code 소스 유출 직후, 한국 개발자 Sigrid Jin(@instructkr)이 4시간 만에 핵심 기능을 Python으로 클린룸(clean-room) 재작성한 프로젝트다. **역사상 가장 빠르게 50K 스타를 달성한 저장소**로, 공개 후 단 2시간 만에 50,000 스타를 기록했다.

**개발 과정:**
oh-my-codex(OmX) 워크플로우 레이어를 활용하여 전체 포팅 세션을 진행했다. $team 모드로 병렬 코드 리뷰, $ralph 모드로 지속적 실행 루프와 아키텍트 수준 검증을 수행했다. Anthropic의 독점 소스를 복사하지 않고 아키텍처 패턴만 캡처한 클린룸 방식이다.

**현재 상태:**
- Python 기반 `src/` 디렉토리에 port_manifest, models, commands, tools, query_engine, main 등 구현
- Rust 포트가 dev/rust 브랜치에서 진행 중이며, 더 빠르고 메모리 안전한 하네스 런타임 목표
- 아직 원본 TypeScript 시스템의 완전한 런타임 동등성은 달성하지 못함

**WSJ 피처:**
제작자 Sigrid Jin은 Wall Street Journal에 "지난해 Claude Code 토큰 250억 개를 혼자 사용한 사람"으로 소개된 바 있다.

## Soo에게 의미 있는 이유

AI 에이전트 하네스 엔지니어링의 구체적 구현체를 Python으로 학습할 수 있는 좋은 리소스다. 또한 "AI 도구로 AI 도구를 재구축"한 메타적 사례로, AInD 생산성의 극단적 예시이기도 하다.
