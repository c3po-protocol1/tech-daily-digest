# Spinel: Ruby AOT 네이티브 컴파일러 (Matz 본인 제작)

- **출처**: [GitHub - matz/spinel](https://github.com/matz/spinel)
- **HN 토론**: [Hacker News](https://news.ycombinator.com/item?id=47887334) (296점, 80개 댓글)
- **태그**: `#Ruby` `#컴파일러` `#AOT` `#Matz` `#프로그래밍언어`

## 상세 요약

Ruby의 창시자 마츠모토 유키히로(Matz)가 직접 만든 Ruby AOT(Ahead-of-Time) 네이티브 컴파일러 Spinel이 공개되었다. 296점이라는 높은 관심도는 이 프로젝트의 의미를 잘 보여준다.

**동작 방식**:
```
Ruby (.rb) → spinel_parse (Prism 기반 AST 파싱) → AST 텍스트 → spinel_codegen (타입 추론 + C 코드 생성) → C 소스 → cc -O2 컴파일 → 네이티브 바이너리
```

**핵심 특징**:
- **전체 프로그램 타입 추론(Whole-program type inference)**: Ruby 소스를 분석하여 타입을 추론하고 최적화된 C 코드를 생성
- **셀프 호스팅**: 컴파일러 백엔드가 Ruby로 작성되어 있으며, 자기 자신을 네이티브 바이너리로 컴파일 가능
- **독립 실행**: 런타임 의존성 없는 독립 실행 바이너리 생성
- **Prism 파서 활용**: Ruby의 공식 파서인 Prism(libprism)을 사용하여 AST 파싱
- **CRuby 대비 유의미한 속도 향상**: 벤치마크에서 상당한 성능 개선을 보여줌

**기술적 접근**:
- C 코드 생성 방식을 채택하여 기존 C 컴파일러의 최적화 파이프라인 활용
- 455개의 커밋으로 활발하게 개발 중
- .claude 폴더가 존재하며, AI 코딩 에이전트를 활용한 개발 흔적
- MIT 라이선스

Ruby 커뮤니티에서는 오랫동안 성능 문제가 거론되어 왔는데, Matz 본인이 직접 AOT 컴파일러를 만들었다는 것은 Ruby의 성능 문제에 대한 근본적 해결을 모색하고 있음을 시사한다.

## Soo에게 의미 있는 이유

프로그래밍 언어의 진화 방향을 이해하는 것은 기술 컨설턴트에게 중요하다. 특히 AI 시대에 코드 생성이 폭발적으로 늘어나면, 생성된 코드의 실행 성능이 더 중요해진다. Matz가 .claude 폴더를 두고 AI 에이전트로 개발했다는 점도 AInD의 실제 사례로 흥미롭다.
