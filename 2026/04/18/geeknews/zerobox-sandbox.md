# Zerobox — OpenAI Codex 런타임 기반 경량 프로세스 샌드박싱 도구

- **출처**: [GitHub - afshinm/zerobox](https://github.com/afshinm/zerobox)
- **GeekNews**: [topic/28620](https://news.hada.io/topic?id=28620) (8P)
- **태그**: `#보안` `#샌드박스` `#AI에이전트` `#Rust`

## 요약

OpenAI Codex의 샌드박스 런타임을 독립 도구로 추출한 **경량 프로세스 격리 도구**다. AI가 생성한 코드를 안전하게 실행할 수 있다.

### 핵심 기능

- **deny-by-default 정책**: 명시적으로 허용하지 않은 쓰기/네트워크/환경변수 접근 모두 차단
- **자격증명 주입(Credential Injection)**: API 키를 코드에 노출하지 않고 외부 API 호출 가능. 프록시가 실제 키를 대신 주입
- **스냅샷/복원**: `npm install` 같은 작업의 변경사항 추적·되돌리기 가능
- **LLM 도구 호출 권한 분리**: 각 tool call에 다른 권한의 샌드박스 적용 가능 → 프롬프트 인젝션으로 `rm -rf`를 날려도 쓰기 권한 없으면 무시
- **빌드/테스트 외부 호출 차단**: 코드가 몰래 외부 API 호출하는 순간 실패 → 공급망 공격 조기 발견
- **민감 디렉토리 자동 차단**: `~/.ssh`, `~/.aws` 등 기본 deny 처리
- **환경변수 오염 방지**: 필수 변수만 전달, 나머지는 화이트리스트 방식

### 플랫폼 지원

- **macOS**: Seatbelt(sandbox-exec) 기반 완전 지원
- **Linux**: Bubblewrap + Seccomp + Namespaces 기반 완전 지원
- **Windows**: 지원 계획 중
- 단일 바이너리, ~10ms 오버헤드, Rust SDK + TypeScript SDK 제공

## Soo에게 의미 있는 이유

AI 에이전트 보안은 2026년 최대 화두 중 하나다. Zerobox는 에이전트가 생성한 코드를 **프로덕션 환경에서 안전하게 실행하기 위한 인프라**로, 기업 AI 도입의 "보안 가드레일" 역할을 한다. 특히 LLM 도구 호출별 권한 분리는 에이전트 아키텍처 설계 시 참고할 중요한 패턴이다.
