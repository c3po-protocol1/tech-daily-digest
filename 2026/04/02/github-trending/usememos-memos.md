# usememos/memos — 오픈소스 셀프호스팅 노트 앱

- **GitHub**: [usememos/memos](https://github.com/usememos/memos)
- **언어**: Go, TypeScript
- **태그**: `#노트` `#셀프호스팅` `#오픈소스` `#마크다운` `#생산성`

## 상세 요약

빠른 메모 캡처에 최적화된 오픈소스, 셀프호스팅 노트 앱이다. Markdown 네이티브이며 극도로 가볍다.

**핵심 특징:**
- **즉시 캡처** — 타임라인 우선 UI. 열고, 쓰고, 끝. 폴더 탐색 불필요
- **완전한 데이터 소유** — 자체 인프라에 셀프호스팅, Markdown으로 저장, 텔레메트리 제로
- **극단적 단순함** — Go 단일 바이너리, ~20MB Docker 이미지, SQLite/MySQL/PostgreSQL 지원
- **MIT 라이선스** — REST + gRPC API로 확장 가능

**설치 (Docker):**
```bash
docker run -d --name memos -p 5230:5230 -v ~/.memos:/var/opt/memos neosmemo/memos:stable
```

다양한 설치 옵션: Docker Compose, 프리빌트 바이너리, Kubernetes Helm, 소스 빌드 지원.

## Soo에게 의미 있는 이유

개인 지식 관리(PKM)에 관심 있다면 주목할 만한 프로젝트. 특히 AI 에이전트와의 연동(REST/gRPC API)이 쉽고, 20MB Docker 이미지로 어디서든 배포 가능하여 에이전트의 메모리/노트 백엔드로 활용하기 좋다.
