# google-research/timesfm — Google의 시계열 예측 파운데이션 모델

- **GitHub**: [google-research/timesfm](https://github.com/google-research/timesfm)
- **언어**: Python, Jupyter Notebook
- **태그**: `#시계열` `#예측` `#파운데이션모델` `#Google` `#ML`

## 상세 요약

Google Research가 개발한 시계열 예측 전용 파운데이션 모델(TimesFM)이다. ICML 2024 논문 기반이며, 범용 시계열 예측에 활용 가능하다.

**TimesFM 2.5 (최신 버전) 주요 특징:**
- 200M 파라미터 (2.0의 500M에서 축소)
- 최대 16K 컨텍스트 길이 (2.0의 2048에서 대폭 확장)
- 선택적 30M 양자 헤드로 최대 1K 호라이즌의 연속 분위수 예측
- 주파수 표시자(frequency indicator) 제거
- PyTorch + Flax 양쪽 지원, uv로 패키지 관리
- Apple Silicon, GPU, TPU, CPU 지원

**코드 예시:**
```python
model = timesfm.TimesFM_2p5_200M_torch.from_pretrained("google/timesfm-2.5-200m-pytorch")
point_forecast, quantile_forecast = model.forecast(
    horizon=12, inputs=[np.linspace(0,1,100), np.sin(np.linspace(0,20,67))]
)
```
- 포인트 예측과 분위수 예측(10th~90th) 모두 제공
- XReg(공변량 지원) 다시 추가됨

**최근 업데이트:**
2026년 3월에 Claude Code Agent Skills로도 출시되어 에이전트 워크플로우에서 직접 활용 가능.

## Soo에게 의미 있는 이유

시계열 예측은 비즈니스 PoC에서 가장 흔한 유스케이스 중 하나다. 200M 파라미터로 가벼우면서 16K 컨텍스트를 지원하므로, 수요 예측, 이상 탐지, 재무 분석 등 AInD 컨설팅 PoC에 즉시 활용 가능하다.
