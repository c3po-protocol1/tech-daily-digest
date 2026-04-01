# Claude Code (유출본) 소스 코드 분석서

- **출처**: [WikiDocs](https://wikidocs.net/338204)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28080)
- **점수**: 38 points
- **태그**: `#ClaudeCode` `#Anthropic` `#소스분석` `#AI에이전트` `#코딩도구`

## 상세 요약

Anthropic의 Claude Code 전체 소스 코드 구조가 NPM 레지스트리의 source map 파일을 통해 유출되었다. 이 분석서는 유출된 소스의 전체 구조를 한국어로 상세히 분석한 문서다.

**유출 경위:**
Anthropic이 Bun을 인수한 후 Claude Code를 Bun 위에 구축했는데, Bun의 버그(oven-sh/bun#28001)로 인해 프로덕션 모드에서도 소스맵이 포함되어 NPM에 배포되었다. "AI가 작성한 코드의 상당 부분이 자기 제품의 소스를 노출시킨 버그를 만들었다"는 아이러니한 상황.

**주요 발견사항:**
- **Anti-distillation**: 가짜 도구 정의를 시스템 프롬프트에 주입해 API 트래픽 기록을 통한 모델 증류를 방해
- **Undercover Mode**: 외부 오픈소스 프로젝트에서 Anthropic 내부 코드명("Capybara", "Tengu" 등) 언급을 숨기는 모드. 끄는 방법이 없음
- **욕설 감지 정규식**: LLM 대신 정규식으로 사용자 불만을 감지 (비용 효율적)
- **Native Client Attestation**: Zig로 구현된 HTTP 수준 DRM으로 진짜 Claude Code 바이너리인지 검증
- **KAIROS**: 미공개 자율 에이전트 모드 — /dream 스킬, 일일 로그, GitHub 웹훅, 백그라운드 데몬, 5분 주기 크론 포함
- **하루 25만 건 API 낭비**: autocompact 연속 실패로 하루 25만 건 API 호출이 낭비되던 것을 3줄 코드로 수정

## Soo에게 의미 있는 이유

AI 코딩 도구의 내부 아키텍처를 볼 수 있는 드문 기회다. Anti-distillation, client attestation 같은 보안 기법과 KAIROS 자율 에이전트 모드는 향후 AI 에이전트 제품 설계에 직접 참고할 수 있는 패턴이다. GeekNews에서 Claude Code 관련 글이 대거 상위를 차지했다.
