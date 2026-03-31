# ChinaSiro/claude-code-sourcemap — Claude Code 소스맵 추출 도구

- **출처:** [GitHub](https://github.com/ChinaSiro/claude-code-sourcemap)
- **스타:** ★ 4,272
- **언어:** TypeScript
- **태그:** `#ClaudeCode` `#SourceMap` `#ReverseEngineering` `#NPM`

---

## 핵심 요약

Claude Code NPM 패키지에서 `.map`(소스맵) 파일을 추출하여 원본 TypeScript 소스코드를 복원하는 도구. 4,272★로 유출 관련 프로젝트 중 두 번째.

소스맵은 번들링된 JavaScript를 원본 소스에 매핑하는 디버깅 파일. 이 도구는 npm 패키지에서 소스맵을 추출하고 원본 파일 트리를 재구성하는 과정을 자동화. 원래 소스맵이 npm에서 제거되기 전에 추출된 데이터를 기반으로 함.

**교훈:** npm 배포 시 `.npmignore`에 `*.map`을 포함하거나 `package.json`의 `files` 필드에서 소스맵을 제외해야 한다. `source-map` npm 패키지로 소스맵에서 원본 파일을 복원하는 것은 몇 줄의 코드로 가능.

## Soo에게 의미 있는 이유

빌드 파이프라인 보안의 구체적 교훈. 소스맵 유출이 어떻게 발생하고 어떻게 방지하는지의 실전 사례.
