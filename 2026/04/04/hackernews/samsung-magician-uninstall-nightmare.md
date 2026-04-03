# Samsung Magician 디스크 유틸리티 — 삭제에 18단계와 두 번의 재부팅이 필요

- **출처**: [https://chalmovsky.com/2026/03/29/samsung-magician.html](https://chalmovsky.com/2026/03/29/samsung-magician.html)
- **HN 토론**: [https://news.ycombinator.com/item?id=47567222](https://news.ycombinator.com/item?id=47567222)
- **점수**: 378 points
- **태그**: `macos` `software-quality` `rant` `samsung`

## 상세 요약

Samsung Magician은 Samsung SSD의 상태를 확인하고 펌웨어를 업데이트하는 디스크 유틸리티 프로그램이다. 저자는 이 프로그램을 macOS에서 삭제하려는 과정에서 겪은 악몽 같은 경험을 상세히 기술한다.

문제의 핵심:
- **일반적인 삭제로는 제거 불가**: 앱을 휴지통에 넣어도 시스템 곳곳에 잔여 파일이 남음
- **커널 익스텐션 설치**: Samsung이 macOS 커널 레벨에 드라이버를 설치했으며, 이는 SIP(System Integrity Protection)으로 보호됨
- **18단계의 삭제 과정**: find 명령으로 잔여 파일 탐색 → Application Support, Launch Agents, Package Receipts, Cached Processes, Staged Extensions 등에서 파일 제거
- **두 번의 Recovery Mode 재부팅**: csrutil disable로 SIP 해제 → 커널 익스텐션 삭제 → csrutil enable으로 SIP 재활성화
- **150개 이상의 PNG 파일**: "Health: Good"을 표시하는 원형 스피닝 애니메이션에 frame-by-frame PNG 시퀀스 150장 이상이 포함

저자는 "디스크 유틸리티 하나가 왜 커널 익스텐션을 설치하는가?"라는 근본적 질문을 던지며, 소프트웨어 품질과 사용자 존중에 대한 강한 비판을 가한다.

## Soo에게 의미 있는 이유

소프트웨어 설계의 안티패턴을 극단적으로 보여주는 사례. 불필요한 권한 요구, 과도한 시스템 침투, 삭제 용이성 무시 등은 개발자가 반면교사로 삼아야 할 점이다. AInD 프로젝트에서도 에이전트가 시스템에 설치하는 컴포넌트의 clean uninstall을 반드시 고려해야 한다.
