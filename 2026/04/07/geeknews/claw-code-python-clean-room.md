# claw-code — Claude Code 유출 소스 기반 Python 클린룸 재작성

- **출처**: [GitHub/instructkr](https://github.com/instructkr/claw-code)
- **GeekNews**: [topic/28061](https://news.hada.io/topic?id=28061) — 43pts
- **태그**: `#ClaudeCode` `#오픈소스` `#Python` `#에이전트프레임워크`

## 요약

2026년 3월 31일 Claude Code 소스코드 노출 직후, 한국 개발자 Sigrid Jin(@instructkr)이 법적 리스크를 피하기 위해 원본을 보관하는 대신 핵심 기능을 Python으로 처음부터 재작성해 공개한 프로젝트.

### 핵심 특징

- **클린룸 재구현**: 원본 소스를 직접 복사하지 않고, 에이전트 하네스 구조를 독립적으로 재작성
- **구현 범위**: 툴 와이어링, 태스크 오케스트레이션, 런타임 컨텍스트 관리
- **작업 도구**: oh-my-codex(OmX) — $team 모드(병렬 코드 리뷰)와 $ralph 모드(지속 실행 루프) 활용
- **Rust 포트**: dev/rust 브랜치에서 메모리 안전성 + 고성능 목표로 진행 중

### 프로젝트 성과

- GitHub 역사상 가장 빠르게 **30K 스타 돌파** (현재 33.1K⭐, 44.9K🍴)
- WSJ 2026년 3월 기사에서 "연간 250억 토큰 사용 헤비유저"로 소개된 저자
- Anthropic과 무관한 독립 프로젝트

## Soo에게 의미 있는 이유

AI 에이전트의 핵심 아키텍처를 Python으로 접근 가능하게 만든 프로젝트. 에이전트 내부 구조를 학습하고 커스텀 에이전트를 구축하려는 개발자에게 최고의 교재. AInD 컨설팅에서 "에이전트 아키텍처 이해"를 위한 핵즈온 자료로 활용 가능.
