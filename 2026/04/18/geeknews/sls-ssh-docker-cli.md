# sls — SSH와 Docker 컨테이너를 한 화면에서 관리하는 CLI

- **출처**: [GitHub - jinmugo/sls](https://github.com/jinmugo/sls)
- **GeekNews**: [topic/28626](https://news.hada.io/topic?id=28626) (2P)
- **태그**: `#CLI` `#SSH` `#Docker` `#DevOps`

## 요약

관리할 서버가 늘면서 `~/.ssh/config`의 호스트와 Docker 컨테이너를 한 인터페이스에서 관리하기 위해 만든 CLI 도구다.

### 핵심 기능

- **SSH 호스트 퍼지 검색** 후 바로 접속
- 호스트에 SSH 접속 후 `docker ps` 자동 실행, 컨테이너를 트리 형태로 표시
- 컨테이너 선택 시 `docker exec`로 바로 접속
- 쉘 감지 결과 캐시 (매번 probe 불필요)
- 자주 쓰는 호스트 즐겨찾기 상단 고정

### 개발 배경

Coolify로 개인 홈서버를 운영하면서 fzf로 임시방편 사용하다가, Docker 컨테이너까지 같은 인터페이스에서 처리하고 싶어서 개발.

## Soo에게 의미 있는 이유

홈서버나 개인 인프라를 운영하는 개발자에게 유용한 도구. 특히 여러 서버에 분산된 AI 에이전트 환경을 관리할 때 참고할 만한 UX 패턴이다.
