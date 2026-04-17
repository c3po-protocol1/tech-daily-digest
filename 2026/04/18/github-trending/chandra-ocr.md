# Chandra OCR 2 — 복잡한 테이블·필기까지 처리하는 OCR 모델

- **GitHub**: [datalab-to/chandra](https://github.com/datalab-to/chandra)
- **스타**: ⭐ 9,056 | **언어**: Python
- **태그**: `#OCR` `#AI` `#문서처리` `#다국어`

## 요약

이미지와 PDF를 **구조화된 HTML/Markdown/JSON으로 변환**하면서 레이아웃 정보를 보존하는 최첨단 OCR 모델이다.

### 핵심 기능

- **90+ 언어 지원** (한국어 포함)
- 복잡한 **테이블, 수학 수식, 필기** 처리
- 체크박스 포함 **폼 재구성**
- 이미지·다이어그램 추출 및 캡션/구조화 데이터 추가
- 로컬(HuggingFace) 또는 원격(vLLM) 추론 모드

### 설치 및 사용

```bash
pip install chandra-ocr
chandra_vllm                    # vLLM 서버 시작
chandra input.pdf ./output      # OCR 실행
```

### Chandra 2의 개선점

- 수학, 테이블, 레이아웃, 다국어 OCR 대폭 개선
- 외부 olmocr 벤치마크 1위
- 호스팅 API와 무료 플레이그라운드 제공

## Soo에게 의미 있는 이유

문서 처리 자동화는 기업 AI 도입의 가장 일반적인 시작점이다. 한국어를 포함한 90+ 언어 지원과 복잡한 레이아웃 처리 능력은 **한국 기업의 문서 디지털화 프로젝트**에 직접 활용할 수 있다.
