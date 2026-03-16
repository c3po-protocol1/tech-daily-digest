# Wayland 컴포지터와 윈도 관리자 분리

- **출처**: [https://news.hada.io/topic?id=27561](https://news.hada.io/topic?id=27561)

river 0.4.0이 기존 Wayland의 컴포지터-윈도 관리자 일체형 구조를 분리하여, 윈도 관리자를 별도 프로세스로 독립시켰다. 새로운 river-window-management-v1 프로토콜로 창 배치, 키 바인딩 등의 정책을 윈도 관리자에 위임한다.

**왜 중요한가:** Linux 데스크톱 아키텍처의 중요한 진화로, 관심사 분리(SoC) 원칙이 시스템 소프트웨어에서도 적용되는 사례다.

**태그:** Wayland, Linux, 윈도관리자, 아키텍처, 데스크톱
