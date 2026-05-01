# Hitch v4

Hitch v4는 사랑의 언어를 단발성 테스트로 끝내지 않고, 관계의 맥락과 반복 패턴을 장기적으로 이해하는 **relationship understanding system**을 목표로 하는 실험 레포다.

이 레포는 최종 `hitch` 제품으로 바로 들어가기 전,
`hitch-test-v4`에서 먼저 구조를 검증하고 제품 철학, 위키 구조, 시뮬레이션 방식, 운영 방식을 다듬기 위한 독립 구현 공간이다.

## 이 레포가 하려는 것
Hitch v4는 다음을 함께 다루려 한다.
- Telegram 기반 관계 코칭 경험
- relationship space 단위의 독립 운영
- daily / weekly 관계 질문 루프
- 관계별 LLM wiki 축적
- raw 대화 데이터 기반 구조화
- partner perspective simulation
- graph/visualization 가능한 ontology 구조
- Mac mini 기반 운영과 remote control

즉 단순 챗봇이 아니라,
**질문 → 해석 → 관계 위키 축적 → 시뮬레이션 → 리포트/시각화**로 이어지는 관계 운영 시스템을 만들려는 시도다.

## 서비스 철학
### 1. Hitch는 generic chatbot이 아니다
Hitch는 아무 말이나 잘 받아주는 범용 챗봇이 아니라,
관계를 더 잘 이해하고 해석하는 데 초점을 둔 제품이어야 한다.

### 2. 핵심 단위는 relationship space다
관계마다 독립적인 Hitch가 존재한다고 본다.
각 relationship space는 daily, weekly, memory, summary, interpretation을 독립적으로 가진다.
다만 아래 LLM wiki 층은 연결될 수 있다.

### 3. 관계 이해는 장기 축적형이어야 한다
한 번의 테스트나 reveal로 끝나는 게 아니라,
반복되는 질문과 대화, raw 데이터, signal/pattern 축적을 통해 관계를 점점 더 잘 이해해야 한다.

### 4. simulation은 흉내가 아니라 perspective estimation이다
시뮬레이션의 목적은 상대를 연기하는 것이 아니라,
상대가 이 관계를 어떻게 느끼고 받아들이는지 추정하는 것이다.

### 5. LLM wiki가 자라는 것이 핵심 가치다
이 시스템의 중요한 데모 가치이자 제품 가치는,
관계 이해가 위키처럼 쌓이고 구조화되며 시각화 가능해지는 데 있다.

### 6. private boundary는 강하게 지킨다
실제 여자친구/가족 대화 원문, private wiki, 민감한 관계 데이터는 원격 git에 올리지 않는다.
보여줄 수 있는 것은 sanitized artifact와 구조, 코드, 문서다.

## 현재 구조
- `spec/`: 구현용 구조화 스펙
- `ops/`: 운영 문서, 경계, 데모 흐름, 실행 루프
- `raw/`: 향후 raw 입력 위치 (git ignore 대상)
- `data/`: 구조화/생성 데이터 위치 (git ignore 대상)

## 먼저 읽을 문서
추천 순서:
1. `spec/README.md`
2. `spec/product.md`
3. `spec/relationship-space.md`
4. `spec/wiki.md`
5. `spec/simulation.md`
6. `spec/ontology.md`
7. `spec/ingest.md`
8. `spec/demo.md`
9. `spec/ops.md`
10. `spec/iteration-2.md`

## 실행/구현 방식
이 레포는 보통 아래 루프로 운영한다.
1. Atlas가 scope와 spec 경계를 정리한다
2. `omx ralph` 기반 Codex 실행이 구현을 진행하고 commit을 남긴다
3. Atlas가 제품 맥락, private boundary, drift를 검수한다
4. 필요하면 iteration을 다시 돌린다
5. push는 검수 후 진행한다

즉:
- **`omx ralph` = 기본 구현 실행 경로**
- **Codex = 1차 구현자**
- **Atlas = 배경 의식 기반 reviewer + operator + controller**

## Atlas의 역할
Atlas는 단순 사후 리뷰어가 아니다.
필요하면 중간에 개입해서:
- 잘못된 하위 작업을 끊고
- 더 중요한 경로로 우회시키고
- private boundary 사고를 막고
- product drift를 교정하고
- 다음 iteration이 더 잘 이어지도록 관제한다.

특히 raw 대화 파싱, simulation, wiki 구조화처럼
실수 비용이 큰 작업에서는 Atlas의 적극 개입이 전제된다.

## 설치 및 실행
### 기본 전제
- Mac mini가 실행 허브
- MacBook이 원격 operator 역할
- Telegram이 사용자-facing 진입점
- 데모에서는 Telegram 시작 → 질문/답변 → simulation → wiki 성장 → artifact 확인 흐름을 중시한다

### 현재 권장 실행 경로
이 레포의 기본 구현 실행 경로는 `omx ralph` 기준이다.

예시:
```bash
cd /Users/taaeyong/projects/hitch-test-v4
omx ralph --prd "Implement iteration 2 for Hitch v4 using ops/ralph-prompt-iteration-2.md and the current spec/ + ops/ documents"
```

또는 `ops/ralph-prompt-iteration-2.md` 내용을 직접 참고해 실행한다.

### 실행 전 먼저 볼 문서
- `spec/iteration-2.md`
- `ops/runbook.md`
- `ops/execution.md`
- `ops/boundaries.md`
- `ops/ralph-prompt-iteration-2.md`

## private 데이터 경계
다음은 원격 push 금지다.
- 실제 여자친구/가족 raw 대화 데이터
- private wiki
- 민감한 관계 요약
- raw grounding evidence

대신 repo에는 다음이 들어갈 수 있다.
- spec
- ops 문서
- 코드
- 테스트
- ontology/schema 예시
- sanitized wiki/report/graph artifact

자세한 경계는 `ops/boundaries.md` 참고.

## 현재 상태
이 레포는 현재 Hitch v4의 iteration 2 core 단계다.
완성품은 아니지만, relationship space / ingest / wiki / simulation / daily-weekly flow가 서로 연결되는 최소 실제 구조를 갖췄다.

## 다음 목표
- iteration 3에서 parser/segmenter 깊이 확장
- wiki signal/pattern induction 강화
- grounded simulation prompt/runtime 연결
- Telegram-facing flow 연결
- sanitized demo artifact 생성 경로 정리

---

이 레포는 한 번에 완성하려는 프로젝트가 아니라,
작은 iteration을 통해 제품 철학과 구현 구조를 함께 다듬어가는 공간이다.
