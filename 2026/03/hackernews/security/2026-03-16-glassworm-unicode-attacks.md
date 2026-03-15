# Glassworm 재등장: 보이지 않는 유니코드 공격이 저장소를 공격한다

- **출처:** [aikido.dev](https://www.aikido.dev/blog/glassworm-returns-unicode-attack-github-npm-vscode)
- **점수:** 192 | **댓글:** 113

Glassworm이라 불리는 유니코드 기반의 보이지 않는 코드 공격이 GitHub, npm, VS Code 등 주요 개발 플랫폼에서 다시 발견되었다. 눈에 보이지 않는 유니코드 문자를 코드에 삽입하여 악성 동작을 숨기는 기법으로, 코드 리뷰만으로는 탐지가 어렵다.

**왜 중요한가:** 공급망 보안 위협이 더욱 교묘해지고 있으며, 코드 리뷰와 CI/CD 파이프라인에서 유니코드 검증 단계를 추가하는 것이 필수적이 되고 있다.

`tags: #보안 #공급망보안 #유니코드 #GitHub #npm`
