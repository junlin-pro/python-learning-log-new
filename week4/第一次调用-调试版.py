import json
import sys
from pathlib import Path

import requests

# 让 Python 能找到上一级目录里的 key.py（密钥永远只放那一个文件，且已被 .gitignore 忽略）
sys.path.append(str(Path(__file__).resolve().parent.parent))

from key import API_KEY  # noqa: E402

url = "https://api.deepseek.com/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
}
data = {
    "model": "deepseek-chat",
    "messages": [{"role": "user", "content": "用一句话解释什么是摩尔浓度"}],
}

resp = requests.post(url, json=data, headers=headers, timeout=60)

# ========== 2. 先看清到底返回了什么，再谈取值 ==========
print("状态码:", resp.status_code)
print("原始返回（前 500 字符）:")
print(resp.text[:500])
print("-" * 40)

# ========== 3. 取不到 JSON 就说明不是接口的正常返回 ==========
try:
    body = resp.json()
except ValueError:
    print("返回的不是 JSON，多半是网络/代理/域名问题，看上面的原始返回")
    raise SystemExit

# ========== 4. 没有 choices 就把错误信息翻译成人话 ==========
if "choices" not in body:
    print("没有 choices 字段，请求没成功。平台原话：")
    print(json.dumps(body, ensure_ascii=False, indent=2))

    code = resp.status_code
    if code == 401:
        print(">>> 401：key 不对。检查有没有空格、有没有复制全、是不是已经删除了")
    elif code == 402:
        print(">>> 402：余额不足，去平台充值（10 块够学几周）")
    elif code == 400:
        print(">>> 400：参数有问题，最常见是 model 名字打错")
    elif code == 404:
        print(">>> 404：url 路径错了，正确是 https://api.deepseek.com/chat/completions")
    elif code == 429:
        print(">>> 429：请求太频繁，等一分钟再试")
    else:
        print(f">>> 状态码 {code}，对照上面的平台原话判断")
    raise SystemExit

# ========== 5. 走到这里才是真正成功 ==========
answer = body["choices"][0]["message"]["content"]
print("模型回答：")
print(answer)
