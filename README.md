
# AI Agent 90 Days

> 从 Python 零基础出发，90 天系统学习 AI Agent 开发，逐步建立大模型应用开发和工程实践能力。

## 项目简介

本仓库用于记录个人 90 天 AI Agent 开发学习过程。

学习路线：

Python 基础 → Python 工程化 → LLM API → Agent 原理 → RAG → LangGraph → MCP → Multi-Agent → 后端部署 → 项目实战

学习方式：

- 每天投入 4–6 小时
- 理论学习与编程实践相结合
- 每天记录学习笔记
- 每天独立完成编程练习
- 定期进行项目验收与知识复盘

## 学习目标

通过 90 天学习，逐步掌握：

1. Python 语言与基本工程开发
2. LLM API 调用和 Prompt Engineering
3. Function Calling 与 Agent Loop
4. RAG 检索增强生成
5. LangGraph 工作流与状态管理
6. MCP 工具接入和多智能体协作
7. FastAPI、数据库和 Docker 部署
8. Agent 系统的测试、评估与优化

最终目标：独立开发、部署和讲解一个完整的 AI Agent 项目。

## 学习路线

| 阶段 | 天数 | 学习内容 |
|------|------|----------|
| 第一阶段 | Day 01–07 | Python 基础 |
| 第二阶段 | Day 08–14 | Python 工程开发 |
| 第三阶段 | Day 15–21 | LLM 基础与 API |
| 第四阶段 | Day 22–28 | Agent 原理与 Tool Calling |
| 第五阶段 | Day 29–37 | RAG 知识库 |
| 第六阶段 | Day 38–42 | LangGraph |
| 第七阶段 | Day 43–56 | MCP 与 Multi-Agent |
| 第八阶段 | Day 57–65 | 后端开发与部署 |
| 第九阶段 | Day 66–77 | 综合 Agent 项目 |
| 第十阶段 | Day 78–90 | 评测优化与求职准备 |

## 项目结构

```text
agent-90days/
├── README.md
├── .gitignore
├── 01_python_basics/
│   ├── day01/
│   │   ├── notes.md
│   │   └── code/
│   └── day02/
│       ├── notes.md
│       └── code/
├── 02_python_engineering/
├── 03_llm_basics/
├── 04_agent_fundamentals/
├── 05_rag/
├── 06_langgraph/
├── 07_mcp_multi_agent/
├── 08_backend_deployment/
└── projects/
    ├── react_agent/
    ├── rag_assistant/
    └── research_agent/
```

说明：

- `dayXX/notes.md`：当天的学习笔记
- `dayXX/code/`：当天的 Python 练习代码
- `projects/`：完整的综合实战项目
- `README.md`：仓库总说明
- `.gitignore`：Git 忽略规则

## 学习进度

### Python 基础

- [√] Day 01：Python 基础入门
- [√] Day 02：Python 条件判断与循环
- [√] Day 03：Python 数据结构与综合实践
- [√] Day 04: Python 函数与代码复用
- [ ] Day 05: Python 文件操作与异常处理

### Python 工程化

- [ ] Day 08–14：HTTP、Pydantic、异步编程、测试

### LLM 与 Agent

- [ ] Day 15–21：LLM API 开发
- [ ] Day 22–28：手写基础 Agent

### RAG 与 Agent 框架

- [ ] Day 29–37：RAG
- [ ] Day 38–42：LangGraph
- [ ] Day 43–56：MCP 与 Multi-Agent

### 工程化与求职项目

- [ ] Day 57–65：后端与部署
- [ ] Day 66–77：完整 Agent 项目
- [ ] Day 78–90：评测、优化与求职准备

## 实战项目

### 项目一：原生 Python Agent

目标：不依赖 Agent 框架，独立实现 Tool Calling 和 Agent Loop。

状态：未开始

### 项目二：RAG 知识库助手

目标：实现文档解析、向量检索、基于知识库的问答和来源引用。

状态：未开始

### 项目三：Research Agent

目标：结合 LangGraph、MCP、RAG 和 FastAPI，开发可部署的智能研究系统。

状态：未开始

## 如何运行代码

环境要求：

- Python 3
- Git
- VS Code（推荐）

以 Day 01 的 BMI 计算器为例：

```bash
python 01_python_basics/day01/code/bmi_calculator.py
```

Windows 下也可以使用：

```bash
py 01_python_basics/day01/code/bmi_calculator.py
```

## 学习规范

1. 每天建立独立的 `dayXX` 文件夹。
2. 当天代码统一放在 `code/` 目录。
3. 当天笔记统一命名为 `notes.md`。
4. 每天至少独立完成一个编程练习。
5. 记录遇到的问题、错误原因和解决方法。
6. 使用 Git 记录学习过程。
7. 不提交 API Key、密码、虚拟环境和缓存文件。

## 学习资源

- [Python 官方文档](https://docs.python.org/3/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [LangChain](https://docs.langchain.com/)
- [LangGraph](https://docs.langchain.com/oss/python/langgraph/overview)
- [MCP](https://modelcontextprotocol.io/)
- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course/)

## 当前状态

当前学习进度：Day 05

当前内容：Python 文件操作与异常处理

持续更新中。