# B-52 폭격기의 별 추적기 내부 전자기계식 각도 컴퓨터

- **출처**: [Ken Shirriff's Blog](https://www.righto.com/2026/04/B-52-star-tracker-angle-computer.html)
- **토론**: [Hacker News](https://news.ycombinator.com/item?id=47817132) (333 points)
- **태그**: `#retrocomputing` `#hardware` `#navigation` `#military`

## 상세 요약

컴퓨터 역사 복원으로 유명한 Ken Shirriff가 B-52 폭격기에 탑재된 1960년대 자동 천체 항법 시스템의 핵심 부품인 "Angle Computer"를 분해·분석한 글이다.

GPS가 없던 시대, B-52는 별의 위치로 항법을 수행해야 했다. 수동 천체 항법은 정확하지만 느리고 어려운 과정이었기에, Kollsman사가 만든 자동 Astro Compass 시스템이 도입되었다.

**Angle Computer의 작동 원리:**
- 이것은 자이로스코프나 IMU가 아니라, "천구(celestial sphere)"를 물리적으로 모델링하는 전자기계식 아날로그 컴퓨터
- 복잡한 내부 메커니즘이 별의 위치를 나타내는 포인터를 움직임
- 방위각(azimuth)과 고도(altitude)를 synchro라는 장치를 통해 전기 신호로 출력
- 구면 삼각법(spherical trigonometry)을 기계적으로 수행하여 "항법 삼각형" 계산

**시스템 구성:**
- Astro Tracker: 항공기 상부에 장착, 광전자증배관으로 별빛 감지, 자이로 안정화 플랫폼
- 프리즘이 회전·기울어져 특정 별을 조준
- Air Almanac(항공 연감): 10분 간격으로 태양·행성·달의 위치 데이터 제공 (현재도 온라인 제공)
- 19개 구성품으로 이루어진 복잡한 시스템

흥미로운 UI 설계: Master Control Panel의 각 노브는 서로 다른 기하학적 형태로, 조종사가 촉감으로 구분 가능하도록 설계되었다.

## Soo에게 의미 있는 이유

디지털 컴퓨터 이전 시대의 '아날로그 컴퓨팅' 사례는 현재 뉴로모픽 컴퓨팅이나 아날로그 AI 가속기 연구의 영감원이 되고 있다. 또한 복잡한 시스템의 물리적 모델링이라는 접근법은 디지털 트윈 개념의 원형이며, UI/UX 측면에서 "촉감으로 구분 가능한 컨트롤"은 접근성 디자인의 원칙과 맞닿아 있다.
