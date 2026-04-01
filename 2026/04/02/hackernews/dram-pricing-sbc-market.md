# DRAM 가격 폭등이 취미용 SBC 시장을 죽이고 있다

- **출처**: [Jeff Geerling Blog](https://www.jeffgeerling.com/blog/2026/dram-pricing-is-killing-the-hobbyist-sbc-market/)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47606840)
- **점수**: 153 points
- **태그**: `#하드웨어` `#RaspberryPi` `#DRAM` `#SBC` `#메이커`

## 상세 요약

Raspberry Pi가 LPDDR4 RAM 탑재 모든 제품의 가격 인상을 발표했다. 16GB Pi 5는 $299.99까지 올랐고, 새로 출시된 "적정 크기" 3GB Pi 4도 $83.75이다. Jeff Geerling에 따르면 이것은 만우절 농담이 아니다.

**핵심 문제:**
LPDDR 칩이 보드 원가의 대부분을 차지하게 되면서, 취미용 SBC 시장 전체가 위기에 처했다. 라즈베리 파이만의 문제가 아니라 모든 SBC 벤더에 해당한다. Radxa 정도만 꾸준히 신제품을 출시하고 있으며, 나머지 소규모 벤더들은 생존이 어려워지고 있다.

**가격 영향:**
4GB 이상 RAM을 탑재한 보드는 대부분의 취미 사용자가 감당하기 어려운 가격대로 올라갔다. 미니 PC도 8GB 모델이 $250 이상, 중고 PC 역시 4GB 초과 모델의 가격이 상승했다.

**Jeff Geerling의 대응:**
$100 이하로 프로젝트를 복제할 수 있도록 설계해왔으나, 이제는 더 오래된 SBC와 마이크로컨트롤러 위주로 작업 방향을 전환하고 있다. 라즈베리 파이는 마이크로컨트롤러 생태계와 산업용 기반이 있어 버틸 수 있지만, 소규모 벤더들에겐 치명적이다.

**전망:**
Eben Upton(Raspberry Pi CEO)은 "메모리 가격이 현재 수준에 영원히 머물지는 않을 것"이라 했지만, 시장이 회복될 때까지 취미용 SBC 시장이 살아남을 수 있을지는 불확실하다.

## Soo에게 의미 있는 이유

AI/ML 엣지 디바이스 개발에 라즈베리 파이 등 SBC가 널리 쓰이고 있다. DRAM 가격 상승은 온디바이스 AI 프로토타이핑 비용에 직접 영향을 미치며, AInD PoC 진행 시 하드웨어 선택 전략에 참고해야 할 시장 상황이다.
