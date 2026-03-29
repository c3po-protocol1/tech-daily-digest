# ChatGPT Won't Let You Type Until Cloudflare Reads Your React State

- **출처:** [buchodi.com](https://www.buchodi.com/chatgpt-wont-let-you-type-until-cloudflare-reads-your-react-state-i-decrypted-the-program-that-does-it/)
- **HN 토론:** [Hacker News](https://news.ycombinator.com/item?id=47566865) · ⬆️ 254
- **태그:** `#Security` `#Privacy` `#Cloudflare` `#ChatGPT`

---

## 핵심 요약

ChatGPT 웹사이트가 사용자가 타이핑을 시작하기 전에 Cloudflare의 봇 감지 스크립트가 React 컴포넌트의 내부 상태(state)를 읽는다는 사실을 발견하고 이를 역공학한 기술적 분석 글이다.

저자는 Cloudflare의 난독화된 JavaScript를 해독하여, 봇 감지 시스템이 단순히 네트워크 요청을 모니터링하는 것을 넘어서 React의 Fiber 트리를 직접 탐색하고 컴포넌트 상태를 수집한다는 것을 밝혀냈다.

이는 사용자 프라이버시에 대한 심각한 우려를 제기한다. 봇 감지라는 명목 하에 애플리케이션의 내부 상태가 제3자에게 전송되고 있기 때문이다.

HN 커뮤니티에서는 이러한 관행이 정당한 보안 조치인지, 아니면 과도한 감시인지에 대한 활발한 논쟁이 벌어지고 있다. 254점의 높은 점수가 이 주제에 대한 커뮤니티의 관심을 반영한다.

## Soo에게 의미 있는 이유

웹 애플리케이션 보안과 프라이버시의 경계에 대한 중요한 사례 연구다. AI 서비스들이 점점 더 복잡한 봇 감지를 도입하면서 발생하는 부작용을 이해하는 것은 개발자로서 중요하다.
