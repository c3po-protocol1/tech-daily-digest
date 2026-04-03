# Cog — 머신러닝 모델을 위한 컨테이너 도구

- **GitHub**: [https://github.com/replicate/cog](https://github.com/replicate/cog)
- **태그**: `ml-ops` `docker` `deployment` `python` `replicate`

## 상세 요약

Cog는 Replicate에서 만든 오픈소스 도구로, 머신러닝 모델을 표준화된 프로덕션 레디 Docker 컨테이너로 패키징한다.

### 핵심 특징
- **Docker 고통 해소**: 복잡한 Dockerfile 대신 `cog.yaml` 간단한 설정 파일로 환경 정의. Nvidia 베이스 이미지, 효율적 캐싱, Python 버전 지정 등을 자동 처리
- **CUDA Hell 해결**: CUDA/cuDNN/PyTorch/Tensorflow/Python 호환 조합을 자동으로 설정
- **표준 Python으로 입출력 정의**: 모델의 입력/출력 타입을 Python으로 정의하면 OpenAPI 스키마 자동 생성 및 유효성 검사
- **자동 HTTP 예측 서버**: 고성능 Rust/Axum 서버가 모델 타입에 기반해 RESTful HTTP API를 동적 생성
- **프로덕션 준비 완료**: Docker 이미지가 실행되는 어디서든 배포 가능

### 사용 예
```yaml
# cog.yaml
build:
  gpu: true
  system_packages: ["libgl1-mesa-glx", "libglib2.0-0"]
  python_version: "3.13"
  python_requirements: requirements.txt
predict: "predict.py:Predictor"
```

```python
# predict.py
class Predictor(BasePredictor):
    def setup(self):
        self.model = torch.load("./weights.pth")
    def predict(self, image: Path = Input(description="Grayscale input image")) -> Path:
        return postprocess(self.model(preprocess(image)))
```

## Soo에게 의미 있는 이유

ML 모델의 배포 표준화 도구. AI 프로젝트에서 모델을 프로덕션에 배포하는 것은 항상 큰 허들이며, Cog는 이 과정을 극적으로 단순화한다. AInD 컨설팅에서 모델 배포 전략을 수립할 때 추천할 수 있는 도구이다.
