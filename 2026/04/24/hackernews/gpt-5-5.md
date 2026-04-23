# OpenAI GPT-5.5 발표

> **출처:** [openai.com](https://openai.com/index/introducing-gpt-5-5/)
> **HN 토론:** [Hacker News](https://news.ycombinator.com/item?id=47879092) (936 points)
> **태그:** `#AI` `#LLM` `#OpenAI` `#GPT`

## 요약

OpenAI가 GPT-5.5를 발표했다. "실제 업무를 위한 새로운 차원의 지능"이라는 부제를 달고, 이전 모델 GPT-5.4 대비 전방위적 성능 향상을 보여주는 모델이다.

### 핵심 성능 수치
- **Terminal-Bench 2.0** (복잡한 CLI 워크플로우): 82.7% (GPT-5.4: 75.1%, Claude Opus 4.7: 69.4%)
- **SWE-Bench Pro**: 58.6% (Claude Opus 4.7: 64.3%)
- **OSWorld-Verified** (컴퓨터 사용): 78.7% (Claude Opus 4.7: 78.0%)
- **FrontierMath Tier 4**: 35.4% (GPT-5.4: 27.1%, Claude Opus 4.7: 22.9%)
- **BrowseComp**: 84.4% (GPT-5.5 Pro: 90.1%)
- **GDPval** (지식 작업): 84.9%

### 에이전틱 코딩의 새로운 기준
GPT-5.5는 단순히 더 똑똑한 것이 아니라 **더 효율적**이다. 같은 Codex 태스크를 완료하면서 토큰 사용량이 현저히 줄었다. Artificial Analysis의 코딩 인덱스 기준으로, 경쟁 프론티어 코딩 모델의 **절반 비용**으로 SOTA 지능을 제공한다. Cursor CEO는 "GPT-5.5는 5.4보다 눈에 띄게 똑똑하고 끈기 있다"고 평가했다.

### 과학 연구 역량
- **GeneBench** (유전학/정량 생물학): GPT-5.4 대비 명확한 향상
- Ramsey 수에 대한 **새로운 수학적 증명** 발견 (Lean으로 검증 완료)
- 한 면역학 교수가 62개 샘플, 28,000개 유전자 데이터셋 분석에 활용 → "팀이 몇 달 걸릴 작업"을 완료

### 추론 효율성 혁신
NVIDIA GB200/GB300 NVL72 시스템 위에서 공동 설계되었으며, **GPT-5.4와 동일한 레이턴시**를 유지하면서 더 높은 지능을 제공한다. Codex와 GPT-5.5 자체가 인프라 개선에 기여 — 로드 밸런싱 최적화로 토큰 생성 속도 20% 이상 향상.

### 가격
- API: 입력 $5/1M 토큰, 출력 $30/1M 토큰 (1M 컨텍스트 윈도우)
- GPT-5.5 Pro: 입력 $30/1M, 출력 $180/1M

### 사이버보안 강화
사이버보안 및 생물/화학 능력을 Preparedness Framework 기준 **High**로 분류. Trusted Access for Cyber 프로그램 확대, 정부 파트너와 협력하여 중요 인프라 방어 지원.

## Soo에게 의미 있는 이유

GPT-5.5는 AInD 컨설팅에서 핵심 벤치마크가 된다. 특히 **에이전틱 코딩에서의 토큰 효율성 향상**은 기업 고객에게 비용 대비 효과를 설득할 때 결정적이다. Terminal-Bench 82.7%로 CLI 기반 자동화에서 Claude를 크게 앞서며, 반면 SWE-Bench에서는 Claude가 여전히 우위. 모델별 강점을 정확히 파악하고 적재적소에 배치하는 것이 AInD 컨설턴트의 핵심 역량이 된다.
