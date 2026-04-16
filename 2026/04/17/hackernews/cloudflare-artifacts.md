# Cloudflare Artifacts: 에이전트를 위한 Git 호환 버전 관리 스토리지

- **출처**: [Cloudflare 블로그](https://blog.cloudflare.com/artifacts-git-for-agents-beta/)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47792374) (137 points)
- **태그**: `#Cloudflare` `#에이전트` `#Git` `#인프라` `#DevOps`

## 상세 요약

Cloudflare가 "Agents Week"의 일환으로 **Artifacts**를 발표했다. 에이전트 우선으로 설계된 분산형 버전 관리 파일시스템이다. 모든 Git 클라이언트와 호환되며, 수천만 개의 리포지토리를 프로그래밍적으로 생성할 수 있다.

### 핵심 기능
- **에이전트 세션마다 리포**: 에이전트 세션, 샌드박스 인스턴스마다 자동으로 Git 리포 생성
- **포크 지원**: 알려진 좋은 시작점에서 10,000개 포크 생성 가능
- **GitHub에서 Import**: 기존 리포를 Artifacts로 가져와 에이전트가 독립적으로 작업
- **REST API + Workers API**: Git 클라이언트가 적합하지 않은 서버리스 환경용
- **git-notes 네이티브 지원**: 에이전트가 Git 객체에 메타데이터(프롬프트, 에이전트 귀속 등) 추가 가능

### 기술적 구현
- **Durable Objects 기반**: 수백만~수천만 개의 상태 보유 격리 컴퓨팅 인스턴스
- **Zig로 작성된 Git 구현**: ~100KB WASM 바이너리로 컴파일. SHA-1, zlib, 델타 인코딩, git smart HTTP 프로토콜 전체 구현. 외부 의존성 제로
- **메모리 제한 내 동작**: 128MB 제한의 Durable Object에서 스트리밍 최적화

### ArtifactFS — 대형 리포 즉시 마운트
- 오픈소스로 공개된 파일시스템 드라이버
- blobless clone으로 파일 트리와 refs만 먼저 가져오고, 파일 내용은 백그라운드에서 비동기 하이드레이션
- 2.4GB 웹 프레임워크 리포를 2분 → ~10-15초로 단축
- package.json, go.mod 등 에이전트가 먼저 필요로 하는 파일 우선순위 지정
- 모든 Git 리모트와 호환 (GitHub, GitLab 등)

### 가격
- 작업: $0.15/1,000 건 (월 10k 무료)
- 스토리지: $0.50/GB-월 (1GB 무료)

## Soo에게 의미 있는 이유
에이전트가 코드를 생산하는 시대에 "에이전트용 소스 컨트롤"이라는 새로운 인프라 카테고리가 탄생하고 있다. AInD 컨설팅에서 에이전트 워크플로우 설계 시, 세션 격리, 포크 기반 병렬 작업, 시간 여행(rollback) 같은 패턴은 핵심 설계 원칙이 될 수 있다.
