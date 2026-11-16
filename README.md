# Python 学习日志 · Python Learning Log

生物医药硕士背景，2026 年 10 月起系统自学 Python，目标转向 **AI 应用 / 计算方向**（AI 制药、前向部署工程师 FDE、AI 产品经理）。

本仓库记录每日练习代码、每周小项目与完整提交历史，作为学习过程的可验证证据。

## 学习路线（6-8 周加速版）

| 周次 | 主题 | 关键技能 | 产出 |
|---|---|---|---|
| Week 1 | 基础语法 | 变量 / 字符串 / 列表 / 字典 | 实验浓度换算器 |
| Week 2 | 流程控制 | if / for / while / 嵌套组合 | 样本质量分类统计器 |
| Week 3 | 函数与数据 | 函数 / 文件读写 / 异常调试 | 实验记录汇总器（txt → CSV） |
| Week 4 | 工具链与 API | venv / pip / requests / git / 大模型 API | 文献摘要批量翻译器 |
| Week 5 | 数据处理 | pandas / 正则表达式 | 文献信息结构化提取 |
| Week 6 | 综合项目 | RAG 雏形（检索 + 大模型调用） | 文献问答工具 v0 |

## 目录结构

```
.
├── README.md
├── .gitignore              # 密钥与虚拟环境排除规则
├── key.example.py          # 密钥配置模板（复制为 key.py 后填写）
├── week1/ ~ week4/         # 各周练习与小项目
└── playground/             # 随手写的小玩意
```

## 如何运行

```bash
# 1. 创建并激活虚拟环境
python -m venv myenv
myenv\Scripts\activate        # Windows PowerShell / CMD
# source myenv/bin/activate   # macOS / Linux

# 2. 安装依赖
pip install requests

# 3. 配置 API 密钥（key.py 已在 .gitignore 中排除，不会上传）
copy key.example.py key.py    # 然后把 key.py 里的值换成你自己的

# 4. 运行示例
python week4/translate.py
```

## 说明

- **密钥管理**：所有 API Key 统一从 `key.py` 读取，该文件被 `.gitignore` 排除，代码中不出现任何明文密钥。
- **提交习惯**：一天一提交，提交信息描述当天实际完成的内容，便于回溯学习轨迹。
- **练习素材**：多数练习以生物医药实验数据为对象（酶活值统计、样本质控、文献摘要处理），保持与专业背景的衔接。
