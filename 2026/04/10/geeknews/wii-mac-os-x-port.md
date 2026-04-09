# 닌텐도 Wii에서 Mac OS X 10.0(Cheetah) 구동 성공

- **출처**: [bryankeller.github.io](https://bryankeller.github.io/2026/04/08/porting-mac-os-x-nintendo-wii.html)
- **GeekNews**: [토론](https://news.hada.io/topic?id=28325) (8 points)
- **태그**: `#os-porting` `#reverse-engineering` `#hardware` `#fun`

## 상세 요약

Wii의 PowerPC 750CL CPU(G3 iBook의 PowerPC 750CXe의 후속)가 Mac OS X과 호환 가능하다는 점에 착안한 포팅 프로젝트. Reddit에서 "성공 확률 0%"라는 댓글에 용기를 얻어 시작.

**과정:**
1. **부트로더 개발**: ppcskel 기반으로 SD 카드에서 XNU 커널 로드, 디바이스 트리 구성
2. **커널 패칭**: BAT(Block Address Translation) 설정이 Wii의 메모리 레이아웃(24MB 1T-SRAM + 64MB GDDR3)과 충돌하는 문제 수정
3. **디바이스 드라이버**: IOKit 드라이버 모델을 활용하여 Hollywood SoC(Wii의 커스텀 칩)용 드라이버 스택 구축 — SD 카드, 인터럽트 컨트롤러, 프레임버퍼, USB 등

Mach-O 로더, 디바이스 트리 구성, 커널 LED 패칭(디버깅용 Wii 전면 LED 점등) 등 저수준 시스템 프로그래밍의 교과서적 과정.

## Soo에게 의미 있는 이유

순수 기술적 호기심과 도전의 사례. 시스템 프로그래밍의 깊이를 맛볼 수 있는 재미있는 프로젝트.
