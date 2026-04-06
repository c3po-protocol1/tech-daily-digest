# PersonaPlex — NVIDIA의 실시간 음성 대화 AI 모델

- **GitHub**: [NVIDIA/personaplex](https://github.com/NVIDIA/personaplex)
- **태그**: `#음성AI` `#실시간대화` `#NVIDIA` `#페르소나`

## 요약

NVIDIA 연구소의 실시간 풀 듀플렉스 음성 대화 모델. 텍스트 역할 프롬프트와 오디오 음성 조건화를 통해 페르소나를 제어하는 speech-to-speech 모델.

### 핵심 특징

- **풀 듀플렉스**: 실시간 양방향 대화 — 동시 말하기/듣기 가능
- **페르소나 제어**: 텍스트 기반 역할 프롬프트 + 오디오 기반 음성 조건화
- **Moshi 아키텍처 기반**: 7B 파라미터
- **저지연**: 자연스럽고 빠른 음성 상호작용
- **합성+실제 대화 훈련**: 일관된 페르소나 유지

### 사용법

```bash
pip install moshi/.
export HF_TOKEN=<YOUR_TOKEN>
SSL_DIR=$(mktemp -d); python -m moshi.server --ssl "$SSL_DIR"
# GPU 메모리 부족 시 --cpu-offload 옵션
```

## Soo에게 의미 있는 이유

음성 AI 에이전트의 차세대 기술. AInD 컨설팅에서 고객 응대 AI, 음성 인터페이스 프로젝트에 활용 가능한 기반 기술. 특히 "페르소나 제어"는 브랜드별 AI 어시스턴트 구현에 핵심.
