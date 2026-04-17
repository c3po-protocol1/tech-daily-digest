# SmolVM — 서브세컨드 콜드스타트 경량 가상 머신

- **출처**: [GitHub - smol-machines/smolvm](https://github.com/smol-machines/smolvm)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47808268) (181점, 78댓글)
- **태그**: `#VM` `#인프라` `#Rust` `#오픈소스`

## 요약

SmolVM은 **서브세컨드(1초 미만) 콜드스타트**로 경량 Linux 가상 머신을 빌드하고 실행할 수 있는 CLI 도구다. Show HN으로 공개되었으며, 773스타를 획득했다.

### 핵심 기능

- **서브세컨드 콜드스타트**: VM이 1초 이내에 부팅되어 즉시 사용 가능
- **크로스 플랫폼**: macOS와 Linux 모두 지원
- **탄력적 메모리 사용**: 필요한 만큼만 메모리를 사용하는 효율적인 설계
- **이식 가능한 패키징**: 상태를 포함한 VM을 단일 `.smolmachine` 파일로 패킹하여 다른 플랫폼에서 재수화(rehydrate) 가능
- **격리 기본**: 소프트웨어를 격리된 환경에서 기본 실행

### 기술 스택

- **Rust** 기반으로 작성
- **libkrun**과 **libkrunfw** 서브모듈 사용 (경량 KVM 기반 VM 런타임)
- macOS에서는 Seatbelt, Linux에서는 KVM 기반
- Rust SDK와 TypeScript SDK 제공

### 설치 방법

```bash
curl -sSL https://smolmachines.com/install.sh | bash
```

### 사용 사례

AI 에이전트의 코드 실행 샌드박스, CI/CD 격리 환경, 개발자 로컬 테스트 환경 등에 활용 가능. 특히 OpenAI Codex 같은 AI 코딩 에이전트가 코드를 실행할 격리된 환경이 필요한 상황에서 Docker보다 가벼운 대안으로 주목받고 있다.

## Soo에게 의미 있는 이유

AI 에이전트 시대에 **안전한 코드 실행 환경**은 필수 인프라다. SmolVM의 서브세컨드 부팅은 에이전트가 코드를 생성하고 즉시 실행·검증하는 워크플로우를 가능하게 한다. Zerobox(GeekNews에서 별도 소개)와 함께 AI 에이전트 보안 인프라의 핵심 레이어가 될 수 있다.
