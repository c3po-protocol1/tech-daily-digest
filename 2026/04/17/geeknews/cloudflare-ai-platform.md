# Cloudflare AI Platform: 에이전트를 위한 추론 레이어

- **출처**: [Cloudflare 블로그](https://blog.cloudflare.com/ai-platform/)
- **GeekNews 토론**: [HN](https://news.ycombinator.com/item?id=47792538) (221 points)
- **태그**: `#Cloudflare` `#AI` `#인프라` `#에이전트` `#API게이트웨이`

## 상세 요약

Cloudflare가 AI Gateway와 Workers AI를 **통합 추론 레이어**로 발전시켰다. 하나의 API로 모든 AI 모델, 모든 프로바이더에 접근할 수 있다.

### 핵심 발표
- **하나의 카탈로그, 하나의 엔드포인트**: AI.run() 바인딩으로 Workers AI 모델과 서드파티 모델을 동일하게 호출. 모델 전환은 한 줄 변경
- **70+ 모델, 12+ 프로바이더**: Alibaba Cloud, AssemblyAI, Bytedance, Google, MiniMax, OpenAI 등. 이미지, 비디오, 음성 모델까지 확대
- **통합 비용 관리**: 커스텀 메타데이터로 무료/유료 사용자별, 고객별, 워크플로우별 비용 분석
- **자체 모델 배포(BYOM)**: Replicate의 Cog 기술로 커스텀 ML 모델을 Workers AI에 배포. Cog YAML과 predict.py만으로 배포 가능
- **자동 페일오버**: 동일 모델이 여러 프로바이더에 있으면 장애 시 자동 라우팅
- **스트리밍 복원**: AI Gateway가 스트리밍 응답을 버퍼링. 에이전트 중단 시 재연결해서 응답 재취득 (이중 과금 방지)
- **Replicate 팀 합류**: Replicate 모델이 AI Gateway로 통합. Workers AI에도 배포 가능

### 에이전트 특화 설계
- 챗봇: 1 프롬프트 = 1 추론 호출
- 에이전트: 1 태스크 = 10+ 추론 호출 체인 → 느린 프로바이더 50ms 지연이 500ms로 누적
- 330개 도시의 데이터센터 네트워크로 first token 지연 최소화
- Agents SDK와 연계된 스트리밍 복원으로 안정적 에이전트 워크플로우

## Soo에게 의미 있는 이유
AI 인프라가 "단일 모델 API 호출"에서 "멀티 프로바이더, 멀티 모델 오케스트레이션"으로 진화하고 있다. AInD 컨설팅에서 에이전트 인프라 설계 시, 이런 통합 추론 레이어의 패턴을 이해하는 것이 중요하다. 특히 자동 페일오버와 스트리밍 복원은 프로덕션 에이전트 시스템의 핵심 요구사항이다.
