# Korean Law MCP — 대한민국 법령 검색·조회·분석 89개 도구

- **출처**: [https://github.com/chrisryugj/korean-law-mcp](https://github.com/chrisryugj/korean-law-mcp)
- **GeekNews**: [https://news.hada.io/topic?id=27995](https://news.hada.io/topic?id=27995)
- **점수**: 91 points
- **태그**: `mcp` `legal-tech` `korean` `ai-tools` `claude`

## 상세 요약

대한민국의 전체 법령 시스템을 AI 어시스턴트에서 바로 호출할 수 있도록 도구화한 MCP(Model Context Protocol) 서버 + CLI 프로젝트이다.

### 규모와 범위
- **89개 도구**: 법령, 판례, 행정규칙, 자치법규, 조약, 해석례를 포괄
- **법제처 Open API 기반**: 공식 데이터 소스 활용
- **호환 클라이언트**: Claude Desktop, Cursor, Windsurf, Zed, Claude.ai 등에서 바로 사용 가능

### 핵심 기술 특징
- **도구 프로필 시스템 (lite/full)**: 89개 도구를 14개로 자동 축소하는 lite 모드 제공. 체인 도구가 내부에서 하위 도구를 직접 호출하므로 기능 손실 없음
- **URL 쿼리 API 키**: `?oc=your-key`로 세션 전체에 API 키 자동 적용 (커스텀 헤더 설정이 어려운 웹 클라이언트에서 필수)
- **체인 자동 전문 조회**: 예를 들어 `chain_ordinance_compare`가 자치법규 검색 후 상위 1건의 전문을 자동 조회
- **원격 MCP 주소**: Fly.io에 배포되어 별도 설치 없이 URL만으로 사용 가능

### 사용 예
```
예시: 발급받은 인증키가 honggildong이면
→ https://korean-law-mcp.fly.dev/mcp?profile=lite&oc=honggildong
```

## Soo에게 의미 있는 이유

MCP의 실용적 활용 사례로, 도메인 특화 AI 도구의 교과서적 구현이다. 89개 도구를 14개로 자동 축소하는 프로필 시스템은 MCP 서버 설계의 모범 사례이며, AInD 컨설팅에서 기업의 내부 데이터를 AI에 연결하는 패턴을 보여줄 때 강력한 레퍼런스가 된다.
