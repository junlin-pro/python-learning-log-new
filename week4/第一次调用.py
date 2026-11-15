import sys
from pathlib import Path

import requests

# 让 Python 能找到上一级目录里的 key.py（密钥永远只放那一个文件，且已被 .gitignore 忽略）
sys.path.append(str(Path(__file__).resolve().parent.parent))

from key import API_KEY  # noqa: E402

url = "https://api.deepseek.com/chat/completions"
headers = {"Authorization": f"Bearer {API_KEY}"}
data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "用一句话解释什么是摩尔浓度"}]
}
resp = requests.post(url, json=data, headers=headers)
print(resp.status_code)                          # 200 才是成功
answer = resp.json()["choices"][0]["message"]["content"]
print(answer)