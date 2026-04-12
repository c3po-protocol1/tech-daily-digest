# JVM Options Explorer — 모든 JDK의 VM 옵션을 한눈에

- **출처**: [chriswhocodes.com](https://chriswhocodes.com/vm-options-explorer.html)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47738094)
- **점수**: 93 points | 45 comments
- **태그**: `#java` `#jvm` `#developer-tools` `#performance`

## 상세 요약

Chris Sheridan이 만든 **JVM Options Explorer**는 OpenJDK 6부터 27까지, 그리고 다양한 JDK 배포판의 모든 VM 옵션을 탐색할 수 있는 웹 도구다.

### 지원 JDK 배포판:
- **OpenJDK HotSpot**: 6~27 버전
- **Alibaba Dragonwell**: 8, 11, 17, 21, 25
- **Amazon Corretto**: 8, 11, 17, 19~26
- **Azul Systems Zulu**: 8~26
- **BellSoft Liberica**: 8~26
- **Eclipse Temurin**: 8~25
- **GraalVM**: CE/EE 및 JDK-based, native-image 포함
- **JetBrains Runtime**: 11, 17, 21
- **Microsoft**: 11, 16, 17, 21, 25
- **Oracle**: 6~26
- **SAP SapMachine**: 11~21

### 주요 기능:
- 각 VM 옵션의 이름, 도입 버전, 폐기 상태, 타입, OS/CPU 요구사항, 컴포넌트, 기본값, 설명을 표시
- **JDK 간 옵션 추가/제거 비교**: 업그레이드 시 어떤 옵션이 변경되었는지 한눈에 확인 가능
- VM Intrinsics Explorer, GC Explorer 등 관련 도구도 함께 제공
- foojay.io에도 동일 데이터가 호스팅됨

같은 제작자의 JITWatch, JaCoLine, hsdis 등의 도구와 함께, JVM 성능 튜닝에 필수적인 레퍼런스다.

## Soo에게 의미 있는 이유

Java/JVM 기반 엔터프라이즈 환경에서의 AI 통합 작업 시, JVM 튜닝은 성능 최적화의 핵심이다. 특히 ML 모델 서빙이나 데이터 파이프라인에서 JVM 옵션이 처리량과 지연시간에 큰 영향을 미친다. JDK 업그레이드 시 변경된 옵션을 빠르게 파악할 수 있는 이 도구는 컨설팅 과정에서도 유용하다.
