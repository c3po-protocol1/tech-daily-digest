# 📦 pip install torch 한 줄로 끝낸다 — Python 패키징의 오랜 숙제, Wheel Next

- **출처**: [GeekNews](https://news.hada.io/topic?id=28490) | [wheelnext.dev](https://wheelnext.dev)
- **태그**: `#Python` `#패키징` `#NVIDIA` `#PyTorch` `#uv`

## 상세 요약

NVIDIA·Astral·Quansight 연합이 추진하는 **Wheel Next** 이니셔티브가 Python 패키징의 가장 오래된 숙제를 해결하려 한다. Talk Python To Me Episode #544의 내용을 정리한 글이다.

**문제의 본질 — 2009년에 멈춰버린 바퀴:**
- 현재 x86-64용 휠은 2009년 이전 CPU 기능만 사용 가능
- SSE4, AVX2 등 최신 SIMD 명령어는 인스톨러가 지원 여부를 알 수 없어 사용 불가
- **2009년 vs 2023년 기능의 성능 차이: 10~20배**
- ARM도 마찬가지 — M4 Max MacBook Pro에서 라즈베리 파이용 바이너리 실행
- PyTorch 휠은 ~900MB (5~6개 GPU 아키텍처의 CUDA가 하나에 묶여 있기 때문)

**Wheel Next의 해결 방안:**
- 패키지가 하드웨어 요구사항을 **변형(variant) 메타데이터**로 선언
- 플러그인 인터페이스로 인스톨러(uv 등)가 동적으로 하드웨어 감지 후 최적 휠 선택
- `uv pip install torch` 한 줄이면 GPU 감지 → CUDA 버전 파악 → 200~250MB 슬림 휠 다운로드
- Astral이 이미 uv의 변형 지원 프로토타입 구축 완료

**참여 기업·프로젝트:** NVIDIA, Astral, Quansight, Meta, AMD, Intel, Google, Red Hat, Anaconda, Huawei 등 14개 기업 + NumPy, SciPy, PyTorch, scikit-learn, JAX 등

**PEP 현황:** PEP 817 (Wheel Variants Beyond Platform Tags), PEP 825 (Wheel Variants Package Format) — 역대 가장 긴 PEP.
**일정:** 2026년 내 PEP 검토 + 프로토타입, 생태계 전반 준비는 2026년 이후 전망.

## Soo에게 의미 있는 이유

AI/ML 개발의 가장 큰 고통점 중 하나인 환경 설정 문제가 근본적으로 해결될 수 있다. 특히 PyTorch 900MB 설치, CUDA 버전 호환성 지옥이 사라진다면 AI 개발 온보딩이 극적으로 개선된다. AInD 컨설팅에서 "개발 환경 표준화"를 제안할 때 Wheel Next의 진행 상황을 추적할 필요가 있다.
