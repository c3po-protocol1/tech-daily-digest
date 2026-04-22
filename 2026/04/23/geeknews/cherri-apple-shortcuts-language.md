# Cherri — Apple 단축어를 코드로 작성하는 프로그래밍 언어

- **출처**: [GitHub](https://github.com/electrikmilk/cherri)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28732)
- **점수**: 10점 | 댓글 0개
- **태그**: `#Apple` `#단축어` `#DSL` `#자동화`

## 상세 요약

Siri Shortcuts를 텍스트 코드로 작성하면 실행 가능한 Shortcut 파일로 직접 컴파일해주는 **도메인 특화 언어(DSL)** Cherri가 공개되었다.

**핵심 특징:**
- 단축어의 액션과 **1:1 매핑**으로, 컴파일된 결과물이 예측 가능
- GUI 드래그앤드롭 대신 텍스트 에디터로 단축어 작성
- 버전 관리(Git) 가능
- 프로그래밍 언어의 장점(변수, 조건문, 루프)을 단축어에 적용
- 복잡한 단축어를 코드로 표현하면 가독성과 유지보수성 향상

Apple 단축어는 강력하지만 GUI 기반이라 복잡한 로직 구현 시 관리가 어려운 한계가 있었다. Cherri는 이를 텍스트 기반 개발로 전환하여, **프로그래머의 워크플로우에 단축어를 통합**한다.

## Soo에게 의미 있는 이유

OpenClaw 에이전트들이 macOS 환경에서 동작하므로, Apple Shortcuts와의 연동 가능성이 있다. Cherri를 통해 에이전트가 프로그래밍 방식으로 Shortcuts를 생성/관리할 수 있다면, macOS 자동화의 범위가 크게 확장된다.
