# USB for Software Developers — 소프트웨어 개발자를 위한 USB 입문

- **출처:** [werwolv.net](https://werwolv.net/posts/usb_for_sw_devs/)
- **HN 토론:** [Hacker News](https://news.ycombinator.com/item?id=47695012) (121 points / 21 comments)
- **태그:** `#USB` `#하드웨어` `#드라이버` `#C++` `#libusb`

## 상세 요약

USB 디바이스 드라이버 작성이 커널 레벨 저수준 작업이라는 선입견을 깨는 입문 가이드. 실제로 USB 드라이버 작성은 소켓 프로그래밍과 크게 다르지 않다는 관점에서 출발한다.

### 실습 디바이스
안드로이드 폰의 Bootloader 모드(fastboot)를 사용. 이유: 쉽게 구할 수 있고, 프로토콜이 간단하며, OS에 기본 드라이버가 없어 실험에 적합.

### 핵심 개념 흐름
1. **Enumeration:** `lsusb`로 VID(Vendor ID, 예: 18d1=Google)와 PID(Product ID) 확인
2. **USB Class:** Vendor Specific Class → OS가 기본 드라이버를 로드하지 않음
3. **libusb를 활용한 열거:** 프로그래밍적으로 디바이스 정보 질의
4. **Descriptor:** Configuration → Interface → Endpoint 계층 구조
5. **Transfer Types:** Control(설정/질의), Bulk(대량 데이터), Interrupt(주기적 소량), Isochronous(실시간 스트림)
6. **Endpoint 방향:** IN(디바이스→호스트) / OUT(호스트→디바이스)
7. **Fastboot 프로토콜 구현:** 실제로 안드로이드 폰과 통신

### 핵심 메시지
네트워크 전문가가 아니어도 소켓을 사용할 수 있듯, 임베디드 전문가가 아니어도 USB를 사용할 수 있다. 유저스페이스에서 libusb만으로 충분.

## Soo에게 의미 있는 이유
AI 에이전트가 물리 디바이스와 상호작용해야 하는 IoT/로보틱스 시나리오에서 USB 통신 이해가 필수. 하드웨어-소프트웨어 인터페이스 기본기를 다지는 양질의 자료.
