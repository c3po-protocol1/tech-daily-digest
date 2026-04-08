# Mac OS X를 닌텐도 Wii에 포팅하다

- **출처:** [bryankeller.github.io](https://bryankeller.github.io/2026/04/08/porting-mac-os-x-nintendo-wii.html)
- **HN 토론:** [Hacker News](https://news.ycombinator.com/item?id=47691730) (1,091 points / 201 comments)
- **태그:** `#OS` `#하드웨어` `#리버스엔지니어링` `#PowerPC`

## 상세 요약

Bryan Keller가 Mac OS X 10.0 Cheetah를 닌텐도 Wii에서 네이티브로 실행하는 데 성공한 과정을 상세히 기술한 블로그 포스트이다.

### 하드웨어 호환성 분석
Wii는 PowerPC 750CL 프로세서를 사용하는데, 이는 G3 iBook과 일부 G3 iMac에 탑재되었던 PowerPC 750CXe의 진화형이다. CPU 호환성은 확보된 셈. RAM은 88MB로 (24MB 1T-SRAM + 64MB GDDR3), Mac OS X Cheetah 공식 요구사양 128MB에 못 미치지만, QEMU로 64MB에서 부팅 테스트를 미리 통과시켰다.

### 소프트웨어 접근 전략
Mac OS X의 오픈소스 코어인 Darwin(XNU 커널 + IOKit 드라이버 모델)을 수정해 부팅하면, Quartz/Dock/Finder 등 클로즈드소스 컴포넌트는 추가 패치 없이 돌아갈 것이라는 가설을 세웠다. 부팅 방식으로는 Open Firmware 포팅, BootX 수정, 커스텀 부트로더 3가지를 검토한 끝에, Wii Linux 프로젝트 선례를 따라 **커스텀 부트로더를 처음부터 새로 작성**하기로 결정했다.

### 구현 과정
- Wii의 Homebrew Channel과 BootMii를 활용해 커스텀 코드를 실행
- 부트로더에서 디바이스 트리 구성, 커널 로딩, 드라이버 작성까지 전 과정을 담당
- USB Gecko를 통한 시리얼 디버그, SD 카드 부팅, 인터럽트 컨트롤러, 프레임버퍼 비디오 출력, USB 마우스/키보드 지원

### 핵심 교훈
"불가능해 보이는" 프로젝트도 하드웨어 호환성을 체계적으로 분석하고, 불필요한 복잡도를 줄이는 접근(Open Firmware 대신 커스텀 부트로더)을 택하면 실현 가능하다.

## Soo에게 의미 있는 이유
OS 내부 구조, 부트 프로세스, 커널-드라이버 아키텍처를 실전으로 이해할 수 있는 교과서적 사례. 저수준 시스템 지식이 AI/에이전트 인프라 설계에도 통찰을 준다.
