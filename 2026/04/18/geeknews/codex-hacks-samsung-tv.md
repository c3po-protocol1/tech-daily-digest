# Codex가 삼성 TV를 해킹 — AI의 실제 하드웨어 취약점 공격

- **출처**: [Calif 블로그](https://blog.calif.io/p/codex-hacked-a-samsung-tv)
- **GeekNews**: [topic/28617](https://news.hada.io/topic?id=28617) (3P)
- **태그**: `#보안` `#AI` `#해킹` `#IoT`

## 요약

OpenAI의 Codex가 실제 **삼성 스마트 TV**에서 브라우저 권한을 루트 권한으로 상승시키는 완전한 공격 체인을 자율적으로 수행한 실험 결과다.

### 실험 과정

1. **환경**: 삼성 KantS2 플랫폼 펌웨어 TV, 브라우저 셸 접근 가능 상태
2. **Codex에 제공된 것**: 펌웨어 소스 코드, 실시간 장치 접근, 컨트롤러 호스트
3. **목표**: 브라우저 사용자 권한 → 루트 권한 상승 (구체적 드라이버/경로 미지정)

### Codex의 자율적 공격 과정

- `/dev/ntksys`, `/dev/ntkhdma` 등 world-writable Novatek 디바이스 노드 발견
- `/proc/cmdline` 부팅 파라미터로 메모리 맵 재구성
- **물리 메모리 접근 원시 기능(physmap primitive)** 발견: 사용자 공간에서 임의 물리 메모리 접근 가능
- 커널의 **cred 구조체**를 찾아 UID/GID를 0으로 덮어쓰기 → 루트 셸 획득

### 취약점 근본 원인

- udev 규칙에서 `/dev/ntksys`를 0666(world-writable)로 설정
- 사용자 입력값 검증 부재
- 물리 주소 검증 누락
- mmap 단계에서 공격자 제어 PFN 사용

### 의의

AI가 단순 코드 분석을 넘어 **실제 하드웨어 보안 취약점 탐색과 공격 수행이 가능**함을 입증. 실험 중 Codex는 오류 대응과 명령 실행을 반복하며 **실시간 협업형 에이전트처럼 작동**했다.

## Soo에게 의미 있는 이유

AI 보안 에이전트의 공격 능력이 IoT/임베디드까지 확장되고 있다. 이는 Anthropic의 Mythos/Glasswing과 함께 **AI가 보안 분야를 근본적으로 변화시키고 있음**을 보여주며, 기업의 IoT 보안 전략 재검토가 필요하다는 시그널이다.
