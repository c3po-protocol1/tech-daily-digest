# Gemma Gem: 브라우저에 내장된 AI 모델 — API 키도 클라우드도 불필요

- **출처**: [GitHub - kessler/gemma-gem](https://github.com/kessler/gemma-gem)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47655367) (88 points, 15 comments)
- **태그**: `#Gemma4` `#브라우저확장` `#WebGPU` `#온디바이스` `#에이전트`

## 요약

Gemma Gem은 Google의 Gemma 4 모델을 **브라우저 확장 프로그램 내에서 완전히 온디바이스로 실행**하는 개인 AI 어시스턴트다. API 키, 클라우드, 데이터 유출 없이 WebGPU를 통해 동작한다.

### 핵심 기능

- **페이지 읽기**: 현재 탐색 중인 웹페이지의 콘텐츠를 읽고 질문에 답변
- **DOM 조작**: 버튼 클릭, 폼 입력, 페이지 스크롤 등 브라우저 자동화
- **JavaScript 실행**: 서비스 워커를 통해 JS 코드 실행
- **스크린샷 캡처**: 현재 페이지의 시각적 분석

### 아키텍처

```
Offscreen Document          Service Worker          Content Script
(Gemma 4 + Agent Loop) ↔ (메시지 라우터) ↔ (Chat UI + DOM 도구)
     |                                           |
 WebGPU 추론                              스크린샷 캡처
 토큰 스트리밍                            JS 실행
```

- **Offscreen Document**: `@huggingface/transformers` + WebGPU로 모델 호스팅 및 에이전트 루프 실행
- **Service Worker**: 콘텐츠 스크립트와 오프스크린 문서 간 메시지 라우팅
- **Content Script**: 섀도우 DOM 채팅 오버레이 주입, DOM 도구 실행

### 요구사항

- WebGPU 지원 Chrome
- E2B 모델 ~500MB, E4B 모델 ~1.5GB (최초 실행 후 캐시)

## Soo에게 의미 있는 이유

브라우저 확장 프로그램 안에서 LLM이 에이전트로 동작한다는 것은 AI 네이티브 개발의 새로운 패러다임이다. 별도 서버 인프라 없이 클라이언트 사이드에서 AI 에이전트를 배포할 수 있다는 것은, 보안이 중요한 엔터프라이즈 환경에서 특히 주목할 만하다. AInD 컨설팅에서 "제로 인프라 AI 에이전트" 데모로 활용 가능하다.
