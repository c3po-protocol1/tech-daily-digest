# Qwen3.5-Omni: 텍스트·이미지·오디오·영상 완전 옴니모달 LLM

- **출처:** [GeekNews](https://news.hada.io/topic?id=28027)
- **태그:** `#AI` `#MultiModal` `#Qwen` `#OpenSource` `#LLM` `#Alibaba`

---

## 핵심 요약

Alibaba Qwen 팀이 텍스트, 이미지, 오디오, 영상을 **모두 이해하고 생성**하는 완전 옴니모달 모델을 공개했다.

### 아키텍처

- **Thinker-Talker 아키텍처**: 사고(Thinker)와 표현(Talker) 모듈을 분리하여, 깊은 추론을 하면서도 자연스러운 음성 출력 가능
- **Hybrid-Attention MoE**: 전 모달리티 처리를 위한 혼합 어텐션 Mixture-of-Experts 구조
- **3가지 크기**: Plus, Flash, Light Instruct 버전 제공

### 핵심 스펙

- **256k 롱컨텍스트** 입력 지원
- **10시간 이상** 오디오 처리 가능
- GPT-4o/Gemini와 경쟁하는 **오픈소스** 옴니모달 모델
- 텍스트 → 이미지 생성, 음성 합성, 영상 이해 모두 단일 모델에서

### 오픈소스의 의미

GPT-4o나 Gemini는 클로즈드 소스이지만, Qwen3.5-Omni는 오픈소스. 기업이 자체 인프라에서 멀티모달 AI를 운영할 수 있는 선택지가 추가됨.

## Soo에게 의미 있는 이유

오픈소스 멀티모달 모델의 급격한 발전. AI 에이전트가 텍스트뿐 아니라 이미지와 오디오까지 처리하는 미래에서, 이런 모델이 harness의 도구로 활용될 수 있다. AInD 컨설팅에서 "어떤 모델을 선택해야 하는가"의 옵션 확대.
