# Chrome DevTools MCP — 코딩 에이전트에게 Chrome 디버깅 능력을 부여

- **GitHub**: [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)
- **스타**: ⭐ 35,819 | **언어**: TypeScript
- **태그**: `#MCP` `#Chrome` `#디버깅` `#AI에이전트` 🔥

## 요약

코딩 에이전트(Gemini, Claude, Cursor, Copilot)가 **실시간 Chrome 브라우저를 제어하고 검사**할 수 있게 해주는 MCP 서버다. 35K+ 스타로 가장 인기 있는 MCP 서버 중 하나.

### 핵심 기능

- **성능 인사이트**: Chrome DevTools로 트레이스 녹화 후 성능 인사이트 추출
- **브라우저 디버깅**: 네트워크 요청 분석, 스크린샷, 콘솔 메시지 확인 (소스맵 스택 트레이스)
- **자동화**: Puppeteer로 Chrome 액션 자동화, 결과 자동 대기

### 설정

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

Node.js v20.19+, Chrome 최신 버전 필요.

## Soo에게 의미 있는 이유

AI 에이전트가 실제 브라우저를 디버깅하고 테스트하는 능력은 **프론트엔드 개발 자동화의 핵심**이다. 35K 스타는 이 도구가 에이전트 개발 생태계의 표준이 되어가고 있음을 보여준다.
