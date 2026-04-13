# 📋 winclipshot — Windows 터미널에서 스크린샷 붙여넣기를 가능하게

- **출처**: [GeekNews](https://news.hada.io/topic?id=28472)
- **태그**: `#Windows` `#개발도구` `#ClaudeCode` `#CLI`

## 상세 요약

Windows 터미널에서 Ctrl+V로 스크린샷을 붙여넣을 수 없는 문제를 해결하는 오픈소스 도구다.

**동작 원리:**
- 클립보드 변경 이벤트를 구독 (이벤트 기반, CPU 거의 0%, 메모리 ~15MB)
- 새 이미지가 클립보드에 들어오면 현재 포커스된 창을 확인
- **터미널이면** → PNG로 저장 → 클립보드를 파일 경로로 교체 → Ctrl+V로 경로가 붙여넣기됨
- **비터미널이면** → 이미지 그대로 유지 (기존 동작 보존)
- Chrome에서 스크린샷 → 터미널로 이동하면 60초 내에 자동 변환

**지원 터미널:** Windows Terminal, cmd, PowerShell, Alacritty, WezTerm 등

Claude Code는 Ctrl+V 스크린샷 붙여넣기를 지원하지만 간헐적 실패가 있고, 다른 CLI(ssh, TUI)에서는 지원 자체가 안 될 수 있다. winclipshot은 CLI 종류와 무관하게 "스크린샷 → Ctrl+V" 워크플로우를 통일한다.

## Soo에게 의미 있는 이유

AI 코딩 에이전트에게 시각적 컨텍스트를 전달하는 것은 점점 중요해지고 있다. 이런 작은 UX 개선 도구가 개발자의 일상적 워크플로우에 큰 차이를 만든다.
