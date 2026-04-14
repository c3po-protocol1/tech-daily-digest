# pascalorg/editor — 3D 건축 프로젝트 에디터

- **레포**: [github.com/pascalorg/editor](https://github.com/pascalorg/editor)
- **태그**: #3D #건축 #WebGPU #ReactThreeFiber

## 상세 요약

React Three Fiber와 WebGPU로 구축된 3D 건축 에디터다. 건축 프로젝트를 생성하고 공유할 수 있다.

**아키텍처:**
- Turborepo 모노레포 구조: apps/editor(Next.js), packages/core(스키마·상태관리·시스템), packages/viewer(3D 렌더링)
- 상태 관리: Zustand 기반 3개 스토어 — useScene(씬 데이터, IndexedDB 영속화, Zundo 언두/리두), useViewer(뷰어 상태, 선택/카메라), useEditor(에디터 상태, 도구/패널)
- 렌더링: React Three Fiber + 포스트 프로세싱

**설계 원칙:** core는 노드 스키마, 씬 상태, 지오메트리 생성, 공간 쿼리 담당. viewer는 기본 카메라/컨트롤과 3D 렌더링. editor는 인터랙티브 도구와 편집 기능 확장.

MIT 라이선스. npm 패키지(@pascal-app/core, @pascal-app/viewer)로 배포.

## Soo에게 의미 있는 이유

WebGPU + React Three Fiber 조합의 실전 사례로, 브라우저 기반 3D 앱의 아키텍처 패턴을 보여준다.
