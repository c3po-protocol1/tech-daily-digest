# Claude Desktop for Linux — 비공식 Linux 빌드 스크립트

- **출처**: [GitHub](https://github.com/aaddrick/claude-desktop-debian)
- **태그**: `#Claude` `#Linux` `#desktop` `#packaging`

## 상세 요약

Anthropic의 Claude Desktop을 Linux에서 네이티브로 실행할 수 있게 해주는 비공식 빌드 스크립트 프로젝트다.

**지원 패키지:**
- `.deb` (Debian/Ubuntu)
- `.rpm` (Fedora/RHEL)
- AppImage (배포판 무관)
- AUR 패키지 (Arch Linux)
- Nix flake (NixOS)

**주요 기능:**
- **네이티브 Linux 지원**: 가상화나 Wine 없이 실행
- **MCP 지원**: 완전한 Model Context Protocol 통합
- **시스템 통합**: 글로벌 핫키(Ctrl+Alt+Space), 시스템 트레이, 데스크톱 환경 통합
- **Cowork Mode**: bubblewrap 기반 샌드박스 격리 (기본 활성화)
  - 홈 디렉토리는 읽기 전용, 작업 디렉토리만 쓰기 가능
  - host 모드(격리 없음) 폴백 지원

**설치 방법:**
- APT 저장소 추가 후 `apt install claude-desktop` (권장)
- 자동 업데이트 지원

공식 앱이 아니므로 빌드 스크립트 관련 이슈는 이 레포에, 앱 자체 이슈는 Anthropic에 문의해야 한다.

## Soo에게 의미 있는 이유

Linux 서버/워크스테이션에서 Claude Desktop을 사용해야 하는 상황에서 유용한 도구다. 특히 MCP 통합이 완전히 지원되므로, Linux 환경에서 Claude Code와 Claude Desktop을 함께 활용하는 워크플로 구성이 가능하다.
