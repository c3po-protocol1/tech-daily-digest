# Rust WASM 파서를 TypeScript로 재작성했더니 3배 빨라졌다

**출처:** https://www.openui.com/blog/rust-wasm-parser

OpenUI 팀이 Rust로 작성된 WASM 파서를 TypeScript로 재작성한 결과, 오히려 3배 더 빨라졌다는 사례를 공유했다. WASM의 오버헤드와 네이티브 JS 엔진 최적화의 차이가 원인이었다.

**왜 중요한가:** Rust+WASM이 항상 최적의 선택이 아닐 수 있음을 보여주는 실증적 사례로, 기술 선택에서의 벤치마크 중요성을 강조한다.

**태그:** engineering, rust, wasm, typescript, performance
