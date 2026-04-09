# Gemini SynthID 워터마크 리버스 엔지니어링

- **출처**: [GitHub](https://github.com/aloshdenny/reverse-SynthID)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47709130) (78 points, 36 comments)
- **태그**: `#ai-watermark` `#reverse-engineering` `#security` `#google`

## 상세 요약

Google Gemini가 생성한 모든 이미지에 삽입하는 SynthID 워터마크를 신호 처리와 스펙트럼 분석만으로(독점 인코더/디코더 접근 없이) 리버스 엔지니어링한 프로젝트.

**핵심 발견:**
1. **워터마크는 해상도 의존적**: SynthID는 이미지 해상도에 따라 완전히 다른 주파수 위치에 캐리어를 삽입. 1024x1024에서 만든 코드북으로 1536x2816 이미지의 워터마크를 제거할 수 없음
2. **탐지기 구축**: 90% 정확도로 SynthID 워터마크 식별 가능
3. **V3 멀티 해상도 스펙트럼 바이패스**: 75% 캐리어 에너지 감소, 91% 위상 코히런스 감소, 43+ dB PSNR 유지

JPEG 압축이나 노이즈 주입 같은 무차별 접근과 달리, 주파수 빈 수준의 정밀 제거를 수행하는 SpectralCodebook 방식. 해상도별 워터마크 핑거프린트를 저장하고, 바이패스 시 자동으로 매칭 프로파일을 선택.

**기여 요청:** 순수 검정/흰색 이미지를 Gemini Nano Banana Pro로 생성하여 PR로 제출해달라고 요청 중.

## Soo에게 의미 있는 이유

AI 생성 콘텐츠의 식별/추적이라는 보안 주제. AI 워터마킹의 강건성과 한계를 이해하는 것은 AInD 컨설팅에서 "AI 거버넌스" 논의에 필수적.
