# Gemma 4 멀티모달 Fine-Tuner for Apple Silicon

- **출처:** https://github.com/mattmireles/gemma-tuner-multimodal
- **HN 토론:** https://news.ycombinator.com/item?id=47680309
- **점수:** 95 points | 8 comments
- **태그:** `#AI` `#파인튜닝` `#Apple Silicon` `#오픈소스`

## 상세 요약

Apple Silicon에서 Gemma 4 및 Gemma 3n을 오디오, 이미지, 텍스트로 **멀티모달 파인튜닝**할 수 있는 도구가 Show HN으로 공개되었다. PyTorch와 Metal Performance Shaders를 사용하여 Mac에서 직접 파인튜닝이 가능하다.

이 프로젝트는 Google의 최신 Gemma 4 모델 패밀리를 로컬 Apple Silicon 하드웨어에서 사용자 지정 데이터로 학습시킬 수 있게 해준다. 특히 멀티모달(오디오+이미지+텍스트)을 지원한다는 점이 차별화 요소다.

Metal Performance Shaders를 통한 GPU 가속으로 M1/M2/M3/M4 칩에서도 실용적인 수준의 파인튜닝 성능을 제공한다. 클라우드 GPU 없이도 개인 워크스테이션에서 커스텀 멀티모달 모델을 만들 수 있다는 것이 핵심 가치다.

## Soo에게 의미 있는 이유

로컬 AI 개발의 민주화를 보여주는 프로젝트. MacBook에서 멀티모달 파인튜닝이 가능하다는 것은 개발자들이 클라우드 비용 없이도 맞춤형 AI 모델을 만들 수 있음을 의미한다. AInD PoC에서 로컬 파인튜닝 데모로 활용 가능.
