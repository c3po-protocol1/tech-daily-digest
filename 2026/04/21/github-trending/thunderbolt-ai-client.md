# Thunderbolt — Thunderbird의 오픈소스 AI 클라이언트

- **GitHub**: [thunderbird/thunderbolt](https://github.com/thunderbird/thunderbolt)
- **태그**: `#AI클라이언트` `#오픈소스` `#크로스플랫폼` `#엔터프라이즈`

## 요약

Mozilla/Thunderbird 팀이 만든 오픈소스 크로스플랫폼 AI 클라이언트. 벤더 락인 없이 원하는 모델을 선택하고 데이터를 소유할 수 있음.

**핵심 특징:**
- **모든 플랫폼**: Web, iOS, Android, Mac, Linux, Windows
- **모델 호환**: 프론티어 모델, 로컬 모델, 온프레미스 모델 모두 지원
- Ollama, llama.cpp로 무료 로컬 추론, 또는 OpenAI 호환 API 키 사용
- 엔터프라이즈 기능, 지원, FDE 제공
- Docker Compose 또는 Kubernetes로 셀프 호스팅 가능
- Mozilla Public License 2.0

**현재 상태:**
- 초기 개발 단계, 보안 감사 진행 중
- 온프레미스 배포 기업 고객 대상
- 인증과 검색 기능에 아직 외부 의존성 있음 (자체 백엔드 Docker 배포로 해결 가능)

## Soo에게 의미 있는 이유

기업이 AI 도구를 도입할 때 가장 우려하는 것이 데이터 프라이버시와 벤더 락인. Thunderbolt는 이 문제를 직접 해결하는 오픈소스 대안으로, AInD 온프레미스 배포 시나리오의 참고 아키텍처.
