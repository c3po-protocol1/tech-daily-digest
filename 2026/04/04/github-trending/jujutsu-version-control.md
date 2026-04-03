# Jujutsu (jj) — 차세대 버전 관리 시스템

- **GitHub**: [https://github.com/jj-vcs/jj](https://github.com/jj-vcs/jj)
- **태그**: `vcs` `git` `rust` `developer-tools` `version-control`

## 상세 요약

Jujutsu(줒줒)는 Git의 스토리지 백엔드를 활용하면서도 사용성을 크게 개선한 차세대 버전 관리 시스템이다. Rust로 작성되었으며, 다양한 VCS의 장점을 하나의 도구에 통합했다.

### 설계 철학
- **스토리지와 UI 추상화**: 사용자 인터페이스와 VCS 알고리즘을 스토리지 시스템에서 분리
- **Git 호환**: 현재 Git 리포지토리를 스토리지 레이어로 사용하여 기존 Git 도구와 호환
- **다중 백엔드 지원**: Mercurial, Breezy, Google의 Piper/CitC 등 다양한 백엔드 가능

### 영감의 원천
- **Git**: 빠른 UX, 효율적 알고리즘, 올바른 데이터 구조
- **Mercurial**: 사용성
- **Breezy**: 유연성
- **Google Piper/CitC**: 클라우드 기반 설계

### 주요 특징
- 코어 개발자들이 Jujutsu로 Jujutsu를 개발 중 (GitHub에서)
- Git 포지(GitHub 등)와 호환
- 커밋과 파일은 Git에 저장, 브랜치와 메타데이터는 커스텀 스토리지

### 주의사항
- Git 기반이므로 기존 Git 워크플로와 자연스럽게 통합
- 초보자와 경험자 모두를 위해 설계

## Soo에게 의미 있는 이유

Git의 후계자로 주목받는 VCS. AI 코딩 에이전트들이 대규모로 브랜치를 생성하고 병합하는 환경에서, 더 나은 VCS는 에이전트의 효율성을 높일 수 있다. Claude Code의 Git Worktrees와 함께 사용할 수 있는 잠재력이 있다.
