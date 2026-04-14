# 월 $20 스택으로 월매출 $10K 회사를 여러 개 운영하는 법

- **출처**: [stevehanov.ca](https://stevehanov.ca/blog/how-i-run-multiple-10k-mrr-companies-on-a-20month-tech-stack)
- **GeekNews 토론**: [GeekNews](https://news.hada.io/topic?id=28457) (46P, 댓글 1개)
- **태그**: #부트스트래핑 #린스타트업 #Go #SQLite

## 상세 요약

단일 VPS, Go 언어, SQLite, 로컬 GPU를 활용해 월 $20 이하의 인프라 비용으로 MRR $10K 이상의 SaaS 회사를 복수 운영하는 전략을 상세히 공유했다.

**핵심 전략:**
- **VPS 하나로 충분**: Linode/DigitalOcean에서 월 $5~10짜리 서버. AWS의 EKS+RDS+NAT Gateway 구성 시 사용자 0명이어도 월 $300+ 지출 vs 이 방식은 $20 이하
- **Go 언어**: 단일 정적 바이너리로 컴파일 → `scp`로 서버에 전송하여 실행. pip 의존성 지옥 없음. 표준 라이브러리만으로 초당 수만 건 요청 처리
- **SQLite 전면 채택**: WAL 모드 활성화 시 수천 명 동시 사용자 처리 가능. Postgres보다 "수 자릿수 빠름" (동일 머신 기준)
- **로컬 GPU로 AI 비용 제로화**: RTX 3090($900)에서 VLLM 실행. Ollama로 시작 → VLLM으로 프로덕션 전환 (PagedAttention으로 배치 처리)
- **OpenRouter**: 프론티어 모델 접근 시 단일 통합 코드. Anthropic 장애 시 자동 폴백
- **GitHub Copilot**: 에이전트가 30분간 전체 코드베이스 분석해도 약 $0.04 (토큰 아닌 요청 단위 과금 활용)

**핵심 메시지**: 벤처 캐피털 없이도 비용을 거의 제로로 유지하면 사실상 무한한 런웨이를 확보할 수 있다.

## Soo에게 의미 있는 이유

"복잡한 인프라 없는 AI 제품 구축"의 실전 사례다. 특히 로컬 GPU + VLLM으로 AI 배치 비용을 제로화하는 전략과, SQLite의 실전 활용 사례는 소규모 AI 프로젝트 기획 시 직접 참고할 수 있다.
