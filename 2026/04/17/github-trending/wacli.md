# wacli — WhatsApp CLI: 동기화, 검색, 전송

- **리포**: [steipete/wacli](https://github.com/steipete/wacli)
- **언어**: Go
- **⭐ Today**: 354 stars
- **태그**: `#WhatsApp` `#CLI` `#Go` `#메시징`

## 상세 요약

WhatsApp Web 프로토콜(whatsmeow)을 활용한 **명령줄 WhatsApp 클라이언트**. 메시지 히스토리 동기화, 오프라인 검색, 메시지 전송을 지원한다.

### 핵심 기능
- 로컬 메시지 히스토리 동기화 + 지속적 캡처
- FTS5 기반 빠른 오프라인 검색
- 텍스트/파일 메시지 전송
- 연락처 및 그룹 관리
- Homebrew로 설치 가능 (`brew install steipete/tap/wacli`)
- 미디어 다운로드, 히스토리 백필 지원

### 사용 예시
```bash
wacli auth              # QR 인증
wacli sync --follow     # 지속 동기화
wacli messages search "meeting"
wacli send text --to 1234567890 --message "hello"
```

## Soo에게 의미 있는 이유
메시징 앱 자동화는 에이전트 시스템의 중요한 채널. WhatsApp CLI가 있으면 에이전트가 WhatsApp을 통해 알림, 리포트, 대화를 자동화할 수 있다.
