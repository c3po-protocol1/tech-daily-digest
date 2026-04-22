# Apple, 경찰이 삭제된 메시지를 추출하던 버그 수정

- **출처**: [TechCrunch](https://techcrunch.com/2026/04/22/apple-fixes-bug-that-cops-used-to-extract-deleted-chat-messages-from-iphones/)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47868867)
- **점수**: 210점 | 댓글 61개
- **태그**: `#보안` `#프라이버시` `#Apple` `#Signal`

## 상세 요약

Apple이 iPhone과 iPad의 소프트웨어 업데이트를 통해, **삭제된 메시지를 법 집행기관이 포렌식 도구로 추출할 수 있었던 버그**를 수정했다. 이 버그는 알림(notification)에 표시된 메시지 내용이 최대 한 달간 기기 내부 데이터베이스에 캐싱되어 남아있던 문제였다.

사건의 경위:
1. 404 Media가 FBI가 Signal 앱에서 삭제된 메시지를 iPhone에서 추출한 사실을 보도
2. Signal 앱 내에서 메시지를 삭제했더라도, **알림으로 표시된 내용은 OS 알림 DB에 잔존**
3. 포렌식 도구(Cellebrite 등)로 이 DB에서 삭제된 메시지 내용 복구 가능
4. Signal 대표 Meredith Whittaker가 Apple에 수정 요청
5. Apple이 "삭제 표시된 알림이 예상치 못하게 기기에 보존되었다"고 인정하고 패치

Apple은 iOS 18 구버전 사용자에게도 이 수정을 백포팅했다. Signal, WhatsApp 등의 "자동 삭제" 기능을 사용하는 고위험 사용자(기자, 활동가 등)에게 특히 중요한 보안 패치다.

핵심 교훈: **앱 레벨의 보안은 OS 레벨의 동작에 의해 무력화될 수 있다.** 알림 시스템이라는 전혀 예상치 못한 경로로 민감 데이터가 유출된 사례.

## Soo에게 의미 있는 이유

AI 시스템의 보안 설계 시 "데이터가 어디에 캐싱되는가"는 항상 사각지대다. LLM 에이전트가 처리하는 민감 데이터가 로그, 캐시, 알림 등 예상치 못한 경로로 잔존할 수 있으며, AInD 컨설팅에서 보안 아키텍처 리뷰 시 반드시 점검해야 할 항목이다.
