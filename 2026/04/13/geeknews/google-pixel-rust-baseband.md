# Google, Pixel 10 베이스밴드 펌웨어에 Rust 도입

> **출처**: [Google Security Blog](https://security.googleblog.com/2026/04/bringing-rust-to-pixel-baseband.html) | [GeekNews 토론](https://news.hada.io/topic?id=28454)
> **점수**: 1점
> **태그**: `#Rust` `#보안` `#Google` `#임베디드` `#펌웨어`

## 요약

Google이 Pixel 10의 셀룰러 베이스밴드(모뎀) 펌웨어에 메모리 안전 언어인 **Rust 기반 DNS 파서**를 도입했다.

**왜 모뎀인가:**
- 모뎀 펌웨어는 수십 MB의 실행 코드를 가진 복잡한 소프트웨어
- 원격 공격 표면이 큰 인터넷 노출 영역
- Google Project Zero가 인터넷을 통한 원격 코드 실행을 시연한 전력
- 대부분 메모리 안전하지 않은 언어로 작성됨

**왜 DNS인가:**
- 현대 셀룰러 통신은 데이터 네트워크 기반 → 전화 포워딩까지 DNS 의존
- 신뢰할 수 없는 데이터 파싱 필요 → 메모리 안전 취약점 위험 (예: CVE-2024-27227)
- 오픈소스 Rust DNS 라이브러리 **hickory-proto** 선택 (75% 이상 테스트 커버리지)

**기술적 도전:**
- `no_std` 지원 필요 (베어메탈 환경) → 업스트림에 no_std PR 기여
- 코드 크기: Rust 코어 17KB + hickory-proto 350KB = 총 371KB
- cargo 대신 rustc를 직접 빌드 시스템에 통합하는 방식 채택
- hickory-proto가 임베디드 최적화되지 않아 코드 크기가 큰 편이나, Pixel 모뎀은 메모리 제약이 적어 코드 품질을 우선시

**오픈소스 기여:**
- hickory-dns에 no_std 지원 PR
- rust-url에 no_std 파서 PR
- ipnet에 no_std 지원 PR

## Soo에게 의미 있는 이유

Rust의 저수준 임베디드 영역 침투가 가속화되고 있음을 보여주는 사례. 특히 Google이 오픈소스 생태계에 직접 기여하면서 Rust를 도입하는 패턴은, 기업의 Rust 채택 전략을 이해하는 데 좋은 참고.
