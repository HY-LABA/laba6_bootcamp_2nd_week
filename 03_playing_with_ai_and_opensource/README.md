# 03. AI & 오픈소스와 놀기 🎮

VSCode에 **AI를 연결하는 법**과, 협업/오픈소스의 **국룰 문서들**(README, .env, .md,
CLAUDE·AGENT.md 등)이 어떤 역할을 하는지 직접 만져보며 익히는 폴더입니다.

## 📂 폴더 네비게이션

```
03_playing_with_ai_and_opensource/
├── README.md                  ← 지금 이 문서 (폴더 안내)
├── 01_AI_VSCode에_연결하기.md   ← Claude·Codex·Copilot 등 AI 연결법
├── 02_마크다운_이해하기.md       ← .md 란? + AI '행동'이 바뀌는 데모
├── 03_AI에게_맥락_주기.md        ← 파일을 읽힌 AI가 '가진 정보'가 달라지는 데모
└── read_env.py                ← .env 값 불러와 출력하는 예제 (+ 보안 설명)
```

## 🔑 국룰 문서는 어디에?

일부 공통 문서는 저장소 **루트**에 있고, 이 폴더 전체에 함께 적용됩니다.

| 문서 | 위치 | 역할 |
| ---- | ---- | ---- |
| [`CLAUDE.md`](../CLAUDE.md) | 루트 | AI 규칙 진입점 (`@AGENT.md` 로 불러옴) |
| [`AGENT.md`](../AGENT.md) | 루트 | AI 답변 규칙 (인사말로 시작하게 지시) |
| [`.env`](../.env) | 루트 | 비밀값 보관 (생일 등) · 공유 금지 |
| [`.gitignore`](../.gitignore) | 루트 | Git이 무시할 파일 지정 (.env 포함) |

## 🚀 빠르게 해보기

```bash
# .env 의 값을 코드로 불러와 출력해 보기
pip install python-dotenv
python 03_playing_with_ai_and_opensource/read_env.py
```

## 03 시연
"LABA6기 2주차 미션의 코드네임이 뭐야? 행운의 숫자도 알려줘.
그리고 **그걸 어디서 알았는지 근거 파일명도** 같이 말해줘."