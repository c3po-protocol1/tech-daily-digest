# Claude Code $100/월 구독을 Zed + OpenRouter로 재배치하기

- **출처**: [braw.dev](https://braw.dev/blog/2026-04-06-reallocating-100-month-claude-spend/)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47700972) (272 points, 185 comments)
- **태그**: `#ai` `#claude-code` `#developer-tools` `#cost-optimization`

## 상세 요약

저자는 Claude Code에 월 $100을 지불하면서도 사용량 한도에 자주 걸리는 문제를 경험했다. AMD의 시니어 AI 디렉터도 같은 문제를 GitHub 이슈로 제기할 정도로 광범위한 불만이다. 핵심 문제는 "버스트" 패턴의 사용 — 코딩 세션 중간에 한도에 걸리면 작업 흐름이 끊기고, 사용하지 않는 시간에는 크레딧이 낭비된다.

**대안 구성:**
- **Zed Editor** ($10/월): Rust 기반으로 VSCode보다 체감 속도가 빠르며, Agent Client Protocol(ACP)을 통해 Claude Code 등 외부 에이전트를 직접 에디터에 통합. OpenRouter 연동 시 Gemini 3.1의 전체 1M 컨텍스트 윈도우를 활용 가능
- **OpenRouter** ($90/월 충전): 365일 만료되는 크레딧 롤오버 방식. ZDR(Zero Data Retention) 엔드포인트만 사용하도록 설정 가능. 5.5% 수수료 부과
- **Cursor** ($20/월): 파일 경로 정규식 기반 룰 적용이 가능한 유일한 도구. Cursor 3.0은 Rust 재작성 + Agent 오케스트레이션 강화

Claude Code 자체도 OpenRouter 경유로 사용 가능하며, `ANTHROPIC_BASE_URL`을 `https://openrouter.ai/api`로 설정하면 된다. 단, Anthropic 모델에 최적화되어 있어 다른 프로바이더에서는 정상 동작을 보장하지 않는다.

## Soo에게 의미 있는 이유

AInD 컨설팅에서 "AI 도구의 비용 최적화"는 반드시 다뤄야 할 주제. 고객사 개발자들이 Claude Code 구독 비용에 불만을 가지고 있을 때, OpenRouter를 통한 모델 유연성 + 비용 통제 전략을 제안할 수 있다. Zed의 ACP 통합도 에이전트 하네스 생태계 이해에 중요한 사례.
