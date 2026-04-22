# Qwen3.6-27B: 플래그십급 코딩 성능의 27B Dense 모델

- **출처**: [Qwen Blog](https://qwen.ai/blog?id=qwen3.6-27b)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47863217)
- **점수**: 595점 | 댓글 301개
- **태그**: `#AI` `#LLM` `#코딩에이전트` `#오픈소스모델`

## 상세 요약

Alibaba의 Qwen 팀이 **Qwen3.6-27B**를 공개했다. 2월 Qwen3.5 시리즈 출시 이후 첫 오픈 웨이트 변형으로, 커뮤니티 피드백을 기반으로 안정성과 실제 유용성에 초점을 맞춘 모델이다.

**주요 개선사항:**
1. **에이전틱 코딩(Agentic Coding)**: 프론트엔드 워크플로우와 레포지토리 수준 추론을 더 유창하고 정밀하게 처리
2. **Thinking Preservation**: 이전 메시지의 추론 컨텍스트를 유지하는 새 옵션으로 반복적 개발의 오버헤드 감소

**벤치마크 성능 (핵심 수치):**
- SWE-bench Verified: **77.2** (Qwen3.5-27B: 75.0, Qwen3.5-397B-A17B: 76.2)
- SWE-bench Pro: **53.5** (Qwen3.5-27B: 51.2)
- Terminal-Bench 2.0: **59.3** (Claude 4.5 Opus와 동등!)
- SkillsBench Avg5: **48.2** (Claude 4.5 Opus: 45.3를 초과!)
- QwenWebBench: **1487** (Claude 4.5 Opus: 1536에 근접)

**모델 아키텍처:**
- 27B 파라미터, Dense 모델 (비전 인코더 포함)
- **Gated DeltaNet + Gated Attention 하이브리드 구조**: 16 × (3 × GatedDeltaNet→FFN → 1 × GatedAttention→FFN)
- 네이티브 262K 컨텍스트, 최대 1,010,000 토큰까지 확장 가능
- Apache 2.0 라이선스

27B Dense 모델이 훨씬 큰 MoE 모델(397B-A17B)과 Claude 4.5 Opus 같은 최상위 상용 모델에 필적하는 코딩 성능을 보여주는 것은 놀라운 결과다. 특히 SkillsBench에서 Claude 4.5 Opus를 능가한 점이 HN에서 큰 주목을 받았다.

## Soo에게 의미 있는 이유

오픈소스 코딩 모델이 상용 모델과 대등한 수준에 도달하고 있다는 강력한 신호. AInD 컨설팅에서 "상용 API vs. 자체 호스팅" 의사결정에 직접적 영향을 미치며, 27B 규모는 고사양 단일 GPU(80GB)에서도 구동 가능하여 **온프레미스 코딩 에이전트** 구축의 현실적 선택지가 된다.
