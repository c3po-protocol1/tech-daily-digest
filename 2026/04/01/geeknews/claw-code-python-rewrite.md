# claw-code: Claude Code 유출 소스 기반 Python 클린룸 재작성

- **출처:** [GeekNews](https://news.hada.io/topic?id=28061)
- **GitHub:** [instructkr/claw-code](https://github.com/instructkr/claw-code) · ★ 54,988
- **태그:** `#AI` `#ClaudeCode` `#OpenSource` `#Python` `#CleanRoom`

---

## 핵심 요약

한국 개발자 Sigrid Jin이 Claude Code 소스 유출 직후 **새벽 4시에 일어나** Python으로 클린룸 재작성을 시작한 프로젝트. 법적 리스크를 피하기 위해 유출된 소스를 직접 참조하지 않고, 아키텍처 패턴만 참고하여 처음부터 재구현.

### 개발 과정

Wall Street Journal이 보도한 바에 따르면 Sigrid Jin은 작년 한 해 **250억 토큰**의 Claude Code를 사용한 가장 활발한 파워 유저 중 한 명. OpenAI의 Codex 위에 구축된 **oh-my-codex(OmX)** 워크플로우 레이어를 사용하여 전체 포팅 세션을 오케스트레이션.

- `$team` 모드로 병렬 코드 리뷰
- `$ralph` 모드로 아키텍트 레벨 검증이 포함된 지속적 실행 루프
- 원본 harness 구조 읽기부터 테스트 포함 Python 트리 생성까지 OmX 오케스트레이션으로 진행

### 프로젝트 구조

```
src/
├── commands.py
├── main.py
├── models.py
├── port_manifest.py
├── query_engine.py
├── task.py
└── tools.py
tests/
assets/omx/     # OmX 워크플로우 스크린샷
```

**역사상 가장 빠르게 50K 스타를 달성한 리포지토리** — 공개 후 2시간 만에 돌파.

## Soo에게 의미 있는 이유

한국 개발자의 글로벌 영향력을 보여주는 사례. 클린룸 재구현이라는 법적/기술적 접근, OmX를 활용한 AI 오케스트레이션 워크플로우, 그리고 "harness의 아키텍처 패턴"을 학습하고 재구현하는 과정 모두 AInD에서 참고할 만하다.
