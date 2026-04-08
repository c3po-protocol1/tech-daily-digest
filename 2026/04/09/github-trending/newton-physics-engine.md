# newton-physics/newton — GPU 가속 물리 시뮬레이션 엔진

- **GitHub:** [newton-physics/newton](https://github.com/newton-physics/newton)
- **태그:** `#물리시뮬레이션` `#로보틱스` `#GPU` `#NVIDIA` `#OpenUSD`

## 상세 요약

Disney Research, Google DeepMind, NVIDIA가 공동으로 시작한 GPU 가속 물리 시뮬레이션 엔진. Linux Foundation 프로젝트로 Apache-2.0 라이선스.

### 기술 스택
- **NVIDIA Warp** 기반, warp.sim(deprecated) 확장·일반화
- **MuJoCo Warp**를 주요 백엔드로 통합
- GPU 기반 계산, OpenUSD 지원, 미분 가능(differentiable), 사용자 확장 가능

### 핵심 특징
- Python 3.10+, NVIDIA GPU (Maxwell 이상), 로컬 CUDA 설치 불필요
- macOS는 CPU 모드만 지원
- `pip install "newton[examples]"` 한 줄로 시작 가능

### 예제
진자 시뮬레이션, URDF 로봇 로딩, 뷰어, 형상 시뮬레이션 등 다양한 기본 예제 제공.

### 설계 목표
빠른 이터레이션과 확장 가능한 로보틱스 시뮬레이션. 강화학습 기반 로봇 훈련에 최적화.

## Soo에게 의미 있는 이유
로보틱스 AI의 핵심 인프라. Disney Research+DeepMind+NVIDIA 조합이 만든 오픈소스라는 점에서 산업 표준이 될 가능성.
