# mautrix-kakaotalk — Matrix 프로토콜로 카카오톡 브리지

> **출처**: [GitHub (bf-dev)](https://github.com/bf-dev/mautrix-kakaotalk) | [GeekNews 토론](https://news.hada.io/topic?id=28436)
> **점수**: 7점
> **태그**: `#오픈소스` `#메시징` `#카카오톡` `#Matrix` `#Go`

## 요약

공식 리눅스용 카카오톡 클라이언트가 없는 상황에서, Matrix 프로토콜과 mautrix/bridgev2를 사용해 구현한 **Matrix ↔ KakaoTalk 브리지**다.

**주요 기능:**
- Matrix ↔ KakaoTalk 텍스트 및 미디어 양방향 브리지
- KakaoTalk → Matrix 히스토리 동기화/백필
- Matrix → KakaoTalk 리액션, 삭제, 읽음 확인
- 답장(reply) 지원 (양방향)
- 카카오톡 스티커/이모티콘을 미디어로 렌더링
- 통화 로그를 사람이 읽을 수 있는 공지로 변환
- 프로필 사진 지원

**macOS 자격증명 추출:**
`scripts/extract-macos-credentials.sh` 스크립트로 macOS KakaoTalk Desktop의 캐시 DB에서 user_id, oauth_token, device_uuid 등을 자동 추출할 수 있다.

기술 스택: Go 언어, Docker 지원, AGPL v3 라이선스. 비공식 구현이므로 계정 제한 리스크가 있다는 경고가 있다.

## Soo에게 의미 있는 이유

한국 개발자에게 실용적인 프로젝트. OpenClaw 같은 멀티플랫폼 메시징 브리지 아키텍처의 참고 사례가 될 수 있다. 특히 mautrix bridgev2 프레임워크 위에 구축한 방식은 다른 메시징 플랫폼 브리지를 만들 때 참고할 만하다.
