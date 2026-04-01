# 반품랩탑 — AI가 다나와+오픈마켓 반품 특가를 매핑해 가성비 노트북을 찾아주는 서비스

- **출처**: [GeekNews (Show GN)](https://news.hada.io/topic?id=28099)
- **링크**: [banpoomlaptop.com](https://banpoomlaptop.com)
- **태그**: `#AI` `#커머스` `#LLM` `#크롤링` `#사이드프로젝트`

## 상세 요약

오픈마켓의 반품 노트북 특가와 다나와 데이터를 AI로 통합하여 진짜 가성비 반품 노트북을 찾아주는 서비스다.

**기술 스택:**
- Frontend: Next.js 16 (App Router), React 19, Tailwind CSS v4, Zustand
- Backend: Node.js, MongoDB (Aggregation Pipeline), Redis
- Crawling: Python (curl_cffi), Puppeteer, PM2 (백그라운드 데몬)
- AI: OpenRouter API (Qwen 3.5), BM25 유사도 검색

**핵심 기술적 도전:**
1) **비정형 데이터 크로스 매핑**: 오픈마켓의 제각각인 반품 노트북 제목과 다나와의 복잡한 스펙명을 매칭하는 것이 가장 큰 난관. BM25로 1차 후보 추출 후, Qwen 3.5 LLM으로 정확한 모델을 매칭하는 2-Step AI 파이프라인을 구축.
2) **히든 스코어 랭킹**: 단순 할인율이 아닌, 성능/가격 비율과 연식 페널티를 결합한 스코어링. 22년식 이전 -50점, 25~26년식 +20점 가중치로 진짜 가성비 제품만 상단 노출.

**LLM 활용 포인트:**
LLM을 챗봇이 아닌 "백그라운드 파이프라인 내 비정형 데이터 정규화 파서"로 활용한 점이 특징이다. 다나와의 긴 텍스트 스펙을 실시간 JSON으로 구조화하는 작업을 백그라운드 워커에 위임.

## Soo에게 의미 있는 이유

LLM을 챗봇이 아닌 데이터 파이프라인의 "정규화 엔진"으로 활용한 실전 사례다. BM25 + LLM 2단계 매칭, 비정형→정형 변환은 AInD 컨설팅에서 흔히 마주칠 패턴이며, 기술 선택(Qwen 3.5 via OpenRouter)도 비용 효율적 접근의 좋은 참고가 된다.
