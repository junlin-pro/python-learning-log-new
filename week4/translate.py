import requests

from key import API_KEY

API_URL = "https://api.deepseek.com/chat/completions"
MODEL = "deepseek-chat"


# ========== 一、文件读写（复用上周的写法，只是从"按行分割"换成"整段读"）==========
def read_text(path):
    """把整个 txt 读成一个字符串。Windows 上的 txt 可能是 utf-8 也可能是 gbk，两个都试。"""
    for enc in ("utf-8", "gbk"):
        try:
            with open(path, encoding=enc) as f:
                return f.read().strip()
        except UnicodeDecodeError:
            continue
    raise ValueError(f"{path} 编码识别失败，另存为 UTF-8 再试")


def save_text(path, text):
    """把字符串整个写进文件。"""
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


# ========== 二、把"调 API"封装成一个函数，以后所有工具都复用它 ==========
def chat(messages):
    """传进完整的 messages 列表，返回模型的这一句回答（字符串）。"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    data = {"model": MODEL, "messages": messages, "temperature": 0.3}
    resp = requests.post(API_URL, json=data, headers=headers, timeout=120)

    try:
        body = resp.json()
    except ValueError:
        raise RuntimeError(f"返回的不是 JSON（状态码 {resp.status_code}）：{resp.text[:200]}")

    if "choices" not in body:
        raise RuntimeError(f"请求失败（状态码 {resp.status_code}）：{body}")

    return body["choices"][0]["message"]["content"]


# ========== 三、主流程 ==========
def main():
    # 第 1 步：读文件
    source = read_text("abstract.txt")
    print(f"读入原文 {len(source)} 个字符")
    print("-" * 50)

    # 第 2 步：搭好多轮对话的骨架子 —— 这就是 messages 的真面目
    messages = [
        {
            "role": "system",
            "content": (
                "你是一名生物医药领域的专业译者。"
                "把英文文献摘要译成准确、通顺的中文学术语言。"
                "不要添油加醋，不要省略数据。"
            ),
        },
        {"role": "user", "content": f"请翻译以下摘要：\n\n{source}"},
    ]

    # 第 3 步：第一轮 —— 翻译
    print("【第 1 轮】正在翻译……")
    translation = chat(messages)
    print(translation)
    print("-" * 50)

    # 第 4 步：把模型的回答追加进对话，再加一个新问题 —— 这就是"多轮"的全部秘密
    messages.append({"role": "assistant", "content": translation})
    messages.append(
        {
            "role": "user",
            "content": "基于上面这篇摘要，整理 5 条要点（每条一行），再列出 5 个核心专业术语的中英对照。",
        }
    )

    print("【第 2 轮】正在提取要点……")
    summary = chat(messages)
    print(summary)

    # 第 5 步：写文件
    result = (
        "===== 中文译文 =====\n"
        + translation
        + "\n\n===== 要点与术语 =====\n"
        + summary
        + f"\n\n（原文 {len(source)} 字符 / 共 {len(messages)} 条对话消息）\n"
    )
    save_text("translation_result.txt", result)
    print("-" * 50)
    print("已写入 translation_result.txt")


main()
