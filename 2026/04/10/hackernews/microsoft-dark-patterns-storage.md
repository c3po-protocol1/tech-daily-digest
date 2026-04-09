# Microsoft가 다크 패턴으로 사용자를 유료 저장소로 유도하는 방법

- **출처**: [lzon.ca](https://lzon.ca/posts/other/microsoft-user-abuse/)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47710149) (120 points, 61 comments)
- **태그**: `#microsoft` `#dark-patterns` `#ux` `#windows`

## 상세 요약

IT 서비스 업체 운영자가 이웃의 남편이 겪은 실제 사례를 통해 Microsoft의 적대적 사용자 경험을 고발한다.

**사건 경위:** 비기술 사용자가 Outlook에서 "저장 공간 부족" 오류를 받았다. 이메일을 거의 사용하지 않음에도 불구하고. 원인: Windows 11이 사용자 동의나 충분한 설명 없이 개인 파일을 OneDrive에 기본 저장하도록 설정. 5GB 무료 공간이 데스크탑 파일로 가득 찬 것. Outlook의 오류 메시지는 친절하게도 "유료 저장소 구독"을 해결책으로 제시.

**더 심각한 문제:** 사용자가 오류를 해결하려고 파일(가족 사진 포함)을 삭제했을 가능성. OneDrive 휴지통의 파일도 저장 공간에 포함되는 또 다른 다크 패턴.

**해결:** Chris Titus의 winutil을 사용하여 OneDrive 완전 제거. 파일을 로컬 홈 폴더로 복구.

저자의 핵심 메시지: Microsoft는 무의미한 KPI 추구가 제품 품질과 사용자 존중보다 중요해진 조직이 되었으며, 이는 모든 대형 소비자 기술 기업에 해당.

## Soo에게 의미 있는 이유

"좋은 UX"와 "다크 패턴"의 경계. AI 서비스를 설계할 때 사용자 신뢰를 해치지 않는 UX가 얼마나 중요한지를 보여주는 반면교사.
