# A2A Protocol v1.0 — 핵심 변경사항과 마이그레이션 가이드

- **출처:** [neocode24 블로그](https://blog.neocode24.com/blog/a2a-protocol-v1-spec-migration)
- **날짜:** 2026-03-26 (수정: 2026-03-29)
- **태그:** `#A2A` `#Protocol` `#AgentToAgent` `#Google` `#MultiAgent` `#MCP`

---

## A2A가 해결하는 문제

MCP(Model Context Protocol)가 에이전트와 도구 사이의 연결을 담당한다면, **A2A(Agent-to-Agent)는 에이전트와 에이전트 사이의 통신을 정의하는 프로토콜**이다. Google이 주도하며, 2025년 4월 초안 이후 약 1년 만에 v1.0 도달. 서로 다른 프레임워크로 만들어진 에이전트가 A2A 인터페이스만 맞추면 상호운용이 가능하다.

## v1.0 변경 분류

| 분류 | 항목 | 대응 난이도 |
|------|------|------------|
| **네이밍 변경** | Enum(SCREAMING_SNAKE_CASE), Operation(PascalCase), 필드명 | 검색/치환 기계적 대응 |
| **구조적 변경** | Part 통합, 스트림 이벤트 래퍼, 에러 형식 | 파싱 로직 전면 수정 |
| **설계 변경** | AgentCard supportedInterfaces[], 멀티 바인딩, 버전 협상 | 아키텍처 수준 검토 |

## 핵심 변경사항

### 1. Proto 파일이 정규 스펙으로 격상
- v0.3: `a2a.proto`는 gRPC 바인딩용 구현 파일 중 하나
- v1.0: proto 파일이 **진실의 원천(source of truth)**, JSON Schema나 문서가 아닌 proto가 스펙
- 코드 생성으로 타입 안전성 + 멀티 언어 지원 자동화

### 2. 멀티 바인딩 (3가지 1급 지원)
| 바인딩 | 전송 | 스트리밍 | 적합한 환경 |
|--------|------|---------|------------|
| JSON+HTTP | HTTP POST | SSE | 웹, 범용, 디버깅 용이 |
| gRPC | HTTP/2 | gRPC stream | 마이크로서비스 내부, 성능 |
| JSON-RPC | HTTP POST | 폴링/웹훅 | 레거시 호환, 0.3 호환 |

대부분의 경우 **JSON+HTTP 하나로 시작** 권장.

### 3. Part 구조 통합
- v0.3: TextPart, FilePart, DataPart 각각 독립 타입 + `kind` 판별자
- v1.0: **통합 Part**, 필드 존재 여부로 타입 결정 (proto의 `oneof` 패턴)

```
// v0.3: {"kind": "text", "text": "안녕하세요"}
// v1.0: {"text": "안녕하세요"}
```

### 4. AgentCard 재설계
- `supportedInterfaces[]` 배열 도입 — 하나의 에이전트가 여러 바인딩/버전 동시 광고
- 점진적 마이그레이션의 핵심: v0.3과 v1.0 인터페이스 동시 광고 가능
- Discovery 경로: `.well-known/agent-card.json` (동일)
- `A2A-Version` 헤더로 버전 협상

### 5. 스트리밍 이벤트 래퍼 변경
- v0.3: `kind` 문자열 + `final` boolean
- v1.0: 래퍼 객체 키 존재로 분기, 스트림 닫힘 = 완료

### 6. 신규 기능
- **Multi-Tenancy**: 모든 요청에 `tenant` 필드 — SaaS 에이전트 서비스 필수
- **Agent Card 서명**: JWS + RFC 8785로 무결성 검증
- **DeviceCodeOAuthFlow**: CLI/IoT 환경 에이전트 인증
- **ListTasks**: 커서 기반 페이지네이션

## 마이그레이션 6단계

1. Enum 전부 SCREAMING_SNAKE_CASE로 변경
2. Part 통합 (kind 판별 → 필드 존재 판별)
3. Operation 이름 PascalCase로 변경
4. 스트리밍 이벤트 래퍼 구조 수정
5. AgentCard에 supportedInterfaces[] 적용
6. 에러 형식 google.rpc.Status로 전환

## Soo에게 의미 있는 이유

멀티 에이전트 시스템의 표준이 안정화되는 것은 AInD의 핵심 이정표다. MCP + A2A 조합은 "에이전트가 도구를 사용하고, 에이전트끼리 소통하는" 완전한 에이전트 생태계의 기반이 된다. OpenClaw 같은 멀티 에이전트 오케스트레이터에서 A2A 지원은 중요한 차별화 포인트가 될 수 있다.
