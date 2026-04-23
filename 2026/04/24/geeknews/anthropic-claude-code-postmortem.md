# Anthropic의 Claude Code 장애 포스트모템

> **출처:** [anthropic.com](https://www.anthropic.com/engineering/april-23-postmortem)
> **GeekNews:** [토론](https://news.hada.io/topic?id=28828) (2 points)
> **태그:** `#AI` `#ClaudeCode` `#Anthropic` `#Postmortem`

## 요약

HN에도 동시 게재된 기사. 지난 한 달간 Claude Code, Claude Agent SDK, Claude Cowork에서 응답 품질 저하 보고가 이어졌고, Anthropic이 3개의 별도 원인을 추적하여 해결했다.

### 3가지 원인
1. **추론 노력도 기본값 변경** (3/4): high→medium으로 낮춰 레이턴시를 줄이려 했으나 지능 저하 유발. 4/7 되돌림
2. **캐싱 최적화 버그** (3/26): 유휴 세션에서 이전 추론을 한 번만 정리해야 하는데 매 턴마다 삭제하는 버그. Claude가 건망증/반복/이상한 도구 선택을 보임. 4/10 수정
3. **시스템 프롬프트 변경** (4/16): "도구 호출 사이 ≤25단어" 제한 추가로 코딩 품질 3% 하락. 4/20 되돌림

### 주목할 점
- Opus 4.7이 코드 리뷰에서 이 버그를 찾았지만, Opus 4.6은 찾지 못했다
- 모든 구독자 사용량 한도 리셋
- @ClaudeDevs X 계정 개설하여 제품 결정 설명 채널 확보

### 교훈
- 더 넓은 평가 세트, soak 기간, 점진적 롤아웃 도입
- 모든 시스템 프롬프트 변경에 모델별 ablation 수행

## Soo에게 의미 있는 이유

"의도하지 않은 품질 저하"가 AI 도구에서 얼마나 복잡하게 나타나는지 보여주는 실전 사례. AInD 컨설팅에서 AI 도구 운영 프레임워크를 설계할 때, 이런 복합 장애 패턴과 카나리 배포의 중요성을 반드시 포함해야 한다.
