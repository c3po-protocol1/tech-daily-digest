# Claude Code 소스 코드가 npm 레지스트리 맵 파일을 통해 유출

- **출처:** [GeekNews](https://news.hada.io/topic?id=28059)
- **태그:** `#Security #NPM #Claude #SourceLeak`

---

## 핵심 요약

Anthropic의 Claude Code CLI 소스 코드가 npm 레지스트리의 .map 파일을 통해 통째로 복원 가능한 형태로 유출되었다. 소스맵 파일은 원래 번들링된 JavaScript를 원본 소스에 매핑하는 디버깅 용도인데, 빌드 파이프라인에서 제거하지 않고 npm에 배포한 것이 원인이다. 이 사건은 npm 패키지 배포 시 민감한 파일을 .npmignore나 files 필드로 명시적으로 제외해야 한다는 기본적인 보안 관행의 중요성을 다시 한번 상기시킨다.

## Soo에게 의미 있는 이유

AI 시대의 개발 생태계와 기술 트렌드를 파악하는 데 직접적으로 관련된 내용이다. AInD 컨설팅에서 참고할 만한 자료.
