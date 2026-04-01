# 🔥 oven-sh/bun — JavaScript/TypeScript 올인원 툴킷

- **GitHub**: [oven-sh/bun](https://github.com/oven-sh/bun)
- **언어**: Zig, C++
- **태그**: `#JavaScript` `#TypeScript` `#런타임` `#패키지매니저` `#번들러`

## 상세 요약

Bun은 단일 실행 파일로 제공되는 JavaScript/TypeScript 올인원 툴킷이다. Node.js의 드롭인 대체품으로 설계되었으며, Zig로 작성되고 JavaScriptCore 엔진을 사용하여 시작 시간과 메모리 사용량을 극적으로 줄였다.

**올인원 기능:**
- 런타임: `bun run` — TS, JSX 기본 지원
- 테스트 러너: `bun test`
- 패키지 매니저: `bun install`, `bun add`
- 번들러: `Bun.build` — CSS, HTML HMR 지원
- 스크립트 러너: `bun run start`

**지원 플랫폼:**
Linux (x64 & arm64), macOS (x64 & Apple Silicon), Windows (x64 & arm64)

**Anthropic 인수와 Claude Code:**
Anthropic이 2025년 말 Bun을 인수했으며, Claude Code가 Bun 위에 구축되었다. 이번 Claude Code 소스 유출의 원인이 된 Bun의 source map 버그(oven-sh/bun#28001)로 인해 다시 주목받고 있다.

## Soo에게 의미 있는 이유

Claude Code의 기반 런타임이자 Anthropic이 인수한 핵심 인프라 기술. JS/TS 생태계의 패러다임 전환(Node.js → Bun)의 중심에 있으며, AI 에이전트 도구의 성능 최적화에 Zig 수준의 네이티브 코드가 어떻게 활용되는지 보여주는 사례.
