# GitHub, Copilot SDK 퍼블릭 프리뷰 공개

- **출처**: [https://github.blog/changelog/2026-04-02-copilot-sdk-in-public-preview/](https://github.blog/changelog/2026-04-02-copilot-sdk-in-public-preview/)
- **GeekNews**: [https://news.hada.io/topic?id=28149](https://news.hada.io/topic?id=28149)
- **점수**: 7 points
- **태그**: `github` `copilot` `sdk` `ai-agents` `developer-tools`

## 상세 요약

GitHub Copilot SDK가 퍼블릭 프리뷰로 공개되었다. Copilot 클라우드 에이전트와 Copilot CLI에서 사용하는 동일한 에이전트 런타임을 개발자가 직접 활용할 수 있게 되었다.

### 지원 언어 (5개)
- TypeScript/JavaScript: `@anthropic-ai/sdk` 스타일 패키지
- Python: pip install
- C#: NuGet
- Go: go module
- Java: Maven (신규)

### 핵심 기능
- **커스텀 도구 및 에이전트**: 도메인 특화 도구를 핸들러와 함께 정의, 에이전트가 언제 호출할지 자율 결정
- **세밀한 시스템 프롬프트 커스터마이징**: replace, append, prepend, dynamic transform 콜백으로 Copilot 시스템 프롬프트 일부분만 수정 가능 (전체 재작성 불필요)
- **스트리밍 & 실시간 응답**: 토큰 단위 스트리밍으로 반응형 UX 구현
- **Blob 첨부**: 이미지, 스크린샷, 바이너리 데이터를 디스크 쓰기 없이 인라인 전송
- **OpenTelemetry 지원**: W3C trace context 전파를 포함한 분산 추적 내장
- **권한 프레임워크**: 민감한 작업에 승인 핸들러 게이트, 읽기 전용 도구는 권한 스킵
- **BYOK(Bring Your Own Key)**: OpenAI, Azure AI Foundry, Anthropic 등 자체 API 키 사용 가능

### 가격
- Copilot 구독자: 프리미엄 요청 할당량에서 차감
- 비구독자: Copilot Free 또는 BYOK로 이용 가능

## Soo에게 의미 있는 이유

GitHub이 Copilot을 SDK 수준에서 개방한 것은 AI 코딩 도구 시장의 중대한 전환점이다. 개발자가 자체 에이전트를 Copilot 런타임 위에 구축할 수 있게 되면서, AI 개발 도구의 생태계가 플랫폼화되고 있다. AInD 컨설팅에서 기업의 AI 코딩 도구 전략을 수립할 때 핵심 참고 자료가 된다.
