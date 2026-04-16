# openai-oauth - ChatGPT 계정으로 OpenAI API를 무료로 사용하기

- **출처**: [GitHub](https://github.com/EvanZhouDev/openai-oauth)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28569) (18 points)
- **태그**: `#OpenAI` `#API` `#해킹` `#오픈소스`

## 상세 요약

ChatGPT 계정의 OAuth 토큰을 활용해 **별도 API 크레딧 구매 없이** OpenAI API를 사용할 수 있는 오픈소스 도구다.

### 핵심 특징
- `npx openai-oauth` 한 줄로 로컬 프록시 서버 실행
- ChatGPT Plus/Free 계정의 OAuth 토큰을 활용
- OpenAI API 호환 엔드포인트 제공
- 기존 OpenAI SDK와 호환 가능
- 별도 API 키나 크레딧 불필요

### 주의사항
- OpenAI ToS 위반 가능성
- Rate limit이 존재할 수 있음
- 프로덕션 용도로는 부적합
- 언제든 차단될 수 있음

## Soo에게 의미 있는 이유
기술적으로 흥미롭지만, 실제 업무에서는 사용을 권장하지 않는다. 다만 OAuth 프록시 패턴 자체는 API 게이트웨이 설계에서 참고할 만한 아이디어다.
