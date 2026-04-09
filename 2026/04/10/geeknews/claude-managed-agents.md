# Claude Managed Agents — 프로덕션 속도 10배 가속

- **출처**: [claude.com](https://claude.com/blog/claude-managed-agents)
- **GeekNews**: [토론](https://news.hada.io/topic?id=28326) (15 points)
- **태그**: `#anthropic` `#claude` `#ai-agents` `#platform`

## 상세 요약

Anthropic이 클라우드 호스팅 에이전트를 대규모로 구축·배포할 수 있는 Managed Agents API 제품군을 공개 베타로 출시했다.

**핵심 구성:**
- **프로덕션급 에이전트**: 보안 샌드박싱, 인증, 도구 실행을 자동 처리
- **장기 실행 세션**: 수 시간 자율 운영, 연결 끊김에도 진행/출력 유지
- **멀티 에이전트 조율**: 에이전트가 다른 에이전트를 스핀업하여 병렬 작업 (리서치 프리뷰)
- **거버넌스**: 스코프 권한, ID 관리, 실행 추적

**내부 테스트에서** 구조화 파일 생성 시 일반 프롬프팅 루프 대비 작업 성공률 최대 10포인트 향상, 어려운 문제일수록 효과 커짐.

**고객 사례:** Notion(Custom Agents), Rakuten(슬랙/Teams 통합 전문가 에이전트를 일주일 내 배포), Asana(AI Teammates), Sentry(Seer 디버깅 → PR 자동 오픈), Atlassian(Jira 내 에이전트 직접 태스크 할당) 등.

**가격:** 표준 토큰 요금 + 활성 런타임 시간당 $0.08.

## Soo에게 의미 있는 이유

에이전트 플랫폼 경쟁의 최전선. Anthropic이 "에이전트 인프라를 직접 관리해드리겠다"는 포지션을 잡은 것은 AInD 컨설팅에서 "Build vs Buy" 의사결정에 직접적 영향.
