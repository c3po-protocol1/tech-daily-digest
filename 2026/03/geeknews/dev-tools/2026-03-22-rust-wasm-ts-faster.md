# Rust WASM 파서를 TypeScript로 다시 작성했더니 3배 빨라졌다

- **출처**: [GeekNews](https://news.hada.io/topic?id=27688)

Rust로 작성된 WASM 파서는 구조적으로 빠르지만, JS-WASM 경계에서의 데이터 복사와 직렬화 오버헤드가 성능 병목으로 드러났다. serde-wasm-bindgen을 통한 직접 객체 반환은 JSON 직렬화보다 9~29% 느렸으며, TypeScript로 재작성했을 때 오히려 3배 빠른 결과를 보였다.

**왜 중요한가**: "Rust가 항상 빠르다"는 가정에 도전하는 사례. 언어 간 경계(boundary)의 오버헤드가 언어 자체의 성능 차이를 압도할 수 있다는 교훈이다.

`#rust` `#wasm` `#typescript` `#performance` `#optimization`
