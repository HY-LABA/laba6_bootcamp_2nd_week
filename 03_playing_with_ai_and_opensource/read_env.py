"""
read_env.py — .env 파일에서 값을 불러와 출력하는 예제

[이 코드를 외울 필요는 없어요]
이렇게 .env 값을 불러오는 코드는 어차피 AI(Claude, Codex, Copilot 등)가
필요할 때 대신 짜줍니다. 그러니 '문법을 외우는 것'보다 아래 개념을 이해하는 게 훨씬 중요합니다.

[핵심: 왜 .env 파일을 따로 두나요?]
- API key, TOKEN, 비밀번호, 개인정보(예: 생일)처럼 '남에게 보이면 안 되는 값'은
  코드 안에 직접 적지 않습니다.
- 대신 이런 값들을 .env 라는 별도 파일에 모아두고, .gitignore 에 등록해서
  GitHub 같은 공개 저장소에 '공유되지 않도록' 막습니다. (= 보안)
- .env 외에도 상황에 따라 아래 같은 파일들이 같은 목적으로 쓰입니다(모두 .gitignore 대상):
    .env.local / .env.development / .env.production / secrets.json / *.key 등

[보너스: AI도 .env 안의 값은 못 봐요]
대부분의 AI 코딩 도구는 보안을 위해 .env 파일 '내부의 실제 값'은 읽지 않도록 설정되어 있습니다.
즉 이 파일에 넣어둔 비밀값은 AI에게도 공유되지 않으니 안심하세요.
(AI는 '.env 를 불러오는 코드'는 짜주지만, 그 안의 실제 값은 보지 못합니다.)

[실행 명령어: python 03_playing_with_ai_and_opensource/read_env.py]
"""

import os
from pathlib import Path

from dotenv import load_dotenv  # 처음 한 번만: pip install python-dotenv

# 이 저장소의 .env 는 루트(이 스크립트보다 한 단계 위 폴더)에 있습니다.
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(ENV_PATH)

# .env 안의 MY_BIRTHDAY 값을 불러옵니다.
birthday = os.getenv("MY_BIRTHDAY")

print(f"불러온 생일(MY_BIRTHDAY): {birthday}")
