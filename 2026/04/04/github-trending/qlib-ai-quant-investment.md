# Qlib — Microsoft의 AI 기반 퀀트 투자 플랫폼

- **GitHub**: [https://github.com/microsoft/qlib](https://github.com/microsoft/qlib)
- **태그**: `quant` `finance` `ai` `ml` `microsoft` `trading`

## 상세 요약

Qlib는 Microsoft에서 개발한 AI 기반 퀀트 투자(양적 투자) 연구 플랫폼으로, 데이터 처리, 모델 학습, 백테스팅을 위한 완전한 ML 파이프라인을 제공한다.

### 핵심 기능
- **End-to-End ML 파이프라인**: 데이터 수집 → 전처리 → 모델 학습 → 백테스팅 → 배포
- **다양한 모델**: KRNN, Sandwich, HIST, IGMTF 등 최신 시계열/금융 모델 내장
- **강화학습 프레임워크**: RL 기반 트레이딩 전략 학습
- **Point-in-Time 데이터베이스**: 미래 정보 유출(lookahead bias) 방지
- **메타 러닝**: DDG-DA 등 메타 러닝 기반 프레임워크
- **포트폴리오 최적화**: 계획 기반(planning-based) 포트폴리오 최적화

### RD-Agent (신규)
Microsoft의 **RD-Agent**와 연동하여 LLM 기반 자율 진화 에이전트가 팩터 마이닝과 모델 최적화를 자동으로 수행:
- 퀀트 팩터 마이닝
- 보고서 기반 팩터 마이닝
- 퀀트 모델 최적화
- 논문: "R&D-Agent-Quant: A Multi-Agent Framework for Data-Centric Factors and Model Joint Optimization" (arXiv:2505.15155)

### 데이터 지원
- 미국, 중국, 브라질(Ibovespa) 등 주요 시장 데이터
- Arctic Provider Backend, Orderbook 데이터

## Soo에게 의미 있는 이유

AI + 금융의 최전선을 보여주는 Microsoft의 연구 프로젝트. 특히 RD-Agent와의 연동은 LLM이 자동으로 투자 팩터를 발견하고 모델을 최적화하는 자율 AI 연구의 실례이다. 멀티 에이전트 + 도메인 전문 지식의 결합 패턴은 다른 산업에도 적용 가능하다.
