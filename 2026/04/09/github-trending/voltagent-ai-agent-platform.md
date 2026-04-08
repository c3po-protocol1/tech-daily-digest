# VoltAgent/voltagent — AI 에이전트 엔지니어링 플랫폼

- **GitHub:** [VoltAgent/voltagent](https://github.com/VoltAgent/voltagent)
- **태그:** `#TypeScript` `#에이전트프레임워크` `#멀티에이전트` `#MCP` `#워크플로우`

## 상세 요약

엔드투엔드 AI 에이전트 엔지니어링 플랫폼. 오픈소스 TypeScript 프레임워크 + VoltOps 콘솔(클라우드/셀프호스팅).

### 프레임워크 핵심
- **Core Runtime (@voltagent/core):** 타입된 역할, 도구, 메모리, 모델 프로바이더를 한 곳에서 정의
- **Workflow Engine:** 선언적 멀티스텝 자동화
- **Supervisors & Sub-Agents:** 슈퍼바이저 런타임이 태스크 라우팅·동기화
- **Tool Registry & MCP:** Zod 타입 도구, 라이프사이클 훅, 취소, MCP 서버 연결
- **LLM 호환:** OpenAI, Anthropic, Google 등 설정만 바꾸면 전환
- **메모리:** 실행 간 컨텍스트 유지
- **Resumable Streaming:** 클라이언트 재연결 시 진행 중 스트림 이어받기

### VoltOps 콘솔
옵저버빌리티, 자동화, 배포, 평가, 가드레일, 프롬프트 관리 등 프로덕션 운영 도구.

## Soo에게 의미 있는 이유
TypeScript 기반 에이전트 프레임워크 중 가장 체계적인 아키텍처. MCP+워크플로우+슈퍼바이저 패턴은 우리 시스템 아키텍처와 직접 비교 가능.
