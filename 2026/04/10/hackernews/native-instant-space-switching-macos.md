# macOS에서 네이티브 즉시 Space 전환하기

- **출처**: [arhan.sh](https://arhan.sh/blog/native-instant-space-switching-on-macos/)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47708818) (210 points, 108 comments)
- **태그**: `#macos` `#productivity` `#window-management`

## 상세 요약

macOS의 가장 큰 불만 중 하나인 Space 전환 애니메이션을 완전히 제거하는 방법을 소개한다. Apple이 지속적으로 사용자 요청을 무시해온 문제.

**기존 대안들의 한계:**
1. "모션 줄이기" 설정 → 페이드 애니메이션으로 대체될 뿐, `prefers-reduced-motion` 미디어 쿼리도 활성화되는 부작용
2. yabai 타일링 WM → SIP 비활성화 필요, 다른 WM과 호환 불가
3. FlashSpace/AeroSpace → 네이티브가 아닌 가상 Space 관리
4. BetterTouchTool → 유료

**해결책: [InstantSpaceSwitcher](https://github.com/jurplel/InstantSpaceSwitcher)** — 트랙패드 스와이프를 매우 큰 속도로 시뮬레이션하는 방식으로 즉시 전환 실현. SIP 비활성화 불필요, 기존 WM과 호환, CLI 인터페이스 제공. 저장소에 별 1개밖에 없는 숨겨진 보석.

## Soo에게 의미 있는 이유

macOS 사용자로서 일상 생산성에 직접 영향. 개발자 도구 생태계에서 "작지만 핵심적인 UX 개선"의 가치를 보여주는 사례.
