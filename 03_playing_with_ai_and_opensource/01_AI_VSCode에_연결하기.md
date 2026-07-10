# 🤖 AI를 VSCode에 연결하기

VSCode 안에서 바로 AI에게 코드를 물어보고, 짜고, 고칠 수 있습니다.
여기서는 대표적인 **Claude · Codex · Copilot** 3가지를 중심으로 설명합니다.

---

## 1. Claude (Anthropic)

- **설치**: VSCode 확장 마켓플레이스에서 `Claude Code` 검색 → 설치
  (또는 터미널에서 `npm install -g @anthropic-ai/claude-code`)
- **로그인**: Claude 계정(Pro/Max 구독) 또는 API Key
- **특징**: 긴 문맥 이해와 여러 파일에 걸친 작업(리팩터링, 문서 작성)에 강함.

## 2. Codex (OpenAI)

- **설치**: 마켓플레이스에서 `Codex` 검색 → 설치
  (또는 터미널에서 `npm install -g @openai/codex`)
- **로그인**: ChatGPT 계정(Plus/Pro) 또는 OpenAI API Key
- **특징**: 터미널/에디터에서 대화형으로 코드를 생성·수정. 빠른 프로토타이핑에 유용.

## 3. GitHub Copilot

- **설치**: 마켓플레이스에서 `GitHub Copilot` + `GitHub Copilot Chat` 설치
- **로그인**: GitHub 계정으로 로그인
- 💡 **학생은 무료!** 루트의 [`깃허브_학생플랜_가입가이드.md`](../깃허브_학생플랜_가입가이드.md) 를 따라
  학생 인증을 하면 Copilot을 무료로 사용할 수 있습니다.
- **특징**: 타이핑 중 실시간 자동완성이 강력. 코드 문맥을 이어서 제안해 줌.

---

## 📁 각 도구는 서로 '다른 규칙 파일'을 읽는다

AI에게 "이 프로젝트에선 이렇게 답해"라고 규칙을 정해줄 수 있는데,
**도구마다 자동으로 읽는 파일 이름이 다릅니다.**

| 도구 | 자동으로 읽는 규칙 파일 |
| ---- | ---- |
| **Claude Code** | `CLAUDE.md` (→ `@파일명` 으로 다른 파일도 불러올 수 있음) |
| **OpenAI Codex** | `AGENTS.md` (⚠️ 복수형, 끝에 **S**) |
| **GitHub Copilot** | `.github/copilot-instructions.md` |

⚠️ **자주 하는 실수**
- 표준 이름은 `AGENTS.md`(복수)입니다. `AGENT.md`(단수)로 만들면 Codex가 **못 찾습니다.**
- `CLAUDE.md` 안의 `@AGENTS.md` 같은 **import 문법은 Claude Code 전용**입니다.
  Codex·Copilot은 `CLAUDE.md` 자체를 읽지 않으니, 그 import도 따라가지 않습니다.

💡 **세 도구에서 똑같이 동작시키려면?**
각 도구가 각자의 파일을 보므로, 규칙 문구를 아래 세 곳에 **각각** 넣어줘야 합니다.
- `CLAUDE.md` (또는 `@AGENTS.md` 로 연결) — Claude용
- `AGENTS.md` — Codex용
- `.github/copilot-instructions.md` — Copilot용

> 이 저장소는 `CLAUDE.md → @AGENTS.md` 로 Claude와 Codex가 **같은 파일**(`AGENTS.md`)을
> 공유하도록 해뒀습니다. Copilot까지 맞추려면 `.github/copilot-instructions.md` 만 추가하면 됩니다.

---

## 그 외에도 선택지는 많습니다

위 3가지 외에도 원하는 도구를 자유롭게 써도 됩니다.

- **Cursor AI** — VSCode를 통째로 대체하는 AI 전용 에디터
- **Windsurf** — AI 에이전트 중심의 에디터
- **Cline / Roo Code** — VSCode 확장형 AI 에이전트
- **Gemini Code Assist**, **Amazon Q** 등

> 도구마다 조작법은 조금씩 다르지만 **개념은 똑같습니다**:
> "에디터 안에서 AI에게 자연어로 요청 → AI가 코드를 읽고/짜고/고친다".
> 하나에 익숙해지면 다른 도구도 금방 적응할 수 있어요.
