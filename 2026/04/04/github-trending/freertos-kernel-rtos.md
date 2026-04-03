# FreeRTOS Kernel — 임베디드 시스템용 실시간 운영체제 커널

- **GitHub**: [https://github.com/FreeRTOS/FreeRTOS-Kernel](https://github.com/FreeRTOS/FreeRTOS-Kernel)
- **태그**: `rtos` `embedded` `iot` `c` `real-time`

## 상세 요약

FreeRTOS는 마이크로컨트롤러 및 소형 마이크로프로세서를 위한 세계에서 가장 널리 사용되는 실시간 운영체제(RTOS) 커널이다.

### 핵심 특징
- **커널 소스 및 포트 전용**: 이 저장소는 FreeRTOS 커널 소스/헤더 파일과 커널 포트만 포함
- **FreeRTOS V11.1.0**: FreeRTOS 202406.00 LTS 릴리스의 일부
- **크로스 플랫폼**: Cortex-M, Cortex-A, RISC-V, Xtensa 등 다양한 아키텍처 지원
- **CMake 지원**: FetchContent 또는 git submodule로 프로젝트에 통합
- **커뮤니티 포럼**: 활발한 지원 커뮤니티 제공

### 사용 방법
```cmake
FetchContent_Declare( freertos_kernel
  GIT_REPOSITORY https://github.com/FreeRTOS/FreeRTOS-Kernel.git
  GIT_TAG main
)
```

데모 애플리케이션에서 시작하여 올바른 소스 파일과 include 경로를 설정한 후, 자체 애플리케이션 코드로 교체하는 방식이 권장됨.

## Soo에게 의미 있는 이유

IoT와 임베디드 AI의 기반 인프라. Edge AI가 확산되면서 RTOS 위에서 AI 추론을 실행하는 패턴이 중요해지고 있다. AI 에이전트가 하드웨어와 직접 상호작용하는 시나리오에서 FreeRTOS는 핵심 인프라이다.
