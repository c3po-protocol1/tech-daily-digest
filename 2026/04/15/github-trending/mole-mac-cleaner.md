# tw93/Mole — macOS 딥 클린 & 최적화 도구

- **레포**: [github.com/tw93/Mole](https://github.com/tw93/Mole)
- **태그**: #macOS #시스템도구 #클리너 #CLI

## 상세 요약

CleanMyMac, AppCleaner, DaisyDisk, iStat Menus의 기능을 **단일 바이너리**로 결합한 macOS 딥 클린 & 최적화 도구다.

**주요 기능:**
- `mo clean`: 캐시, 로그, 브라우저 잔여물, 고아 앱 데이터 제거로 기가바이트 단위 공간 회수
- `mo uninstall`: 앱 + 런치 에이전트 + 환경설정 + 숨겨진 잔여물까지 완전 제거
- `mo analyze`: 시각적 디스크 탐색, 대용량 파일 찾기
- `mo status`: 실시간 CPU/GPU/메모리/디스크/네트워크 모니터링
- `mo purge`: 프로젝트 빌드 아티팩트 정리
- `mo touchid`: sudo에 Touch ID 설정

Homebrew(`brew install mole`) 또는 스크립트로 설치. MIT 라이선스. Windows 실험 버전도 있음.

## Soo에게 의미 있는 이유

개발 환경 관리를 위한 실용적인 CLI 도구다. 특히 `mo purge`(빌드 아티팩트 정리)와 `mo analyze`(디스크 분석)는 개발 머신 유지보수에 유용하다.
