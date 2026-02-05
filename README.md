# 企业级地理数据智能平台（FastAPI + Dash）

本项目基于 **FastAPI + Dash + feffery-maplibre/FAC/FUC** 技术栈，目标是构建一个面向未来扩展的企业级平台，覆盖：

- 企业微信登录与单点验证
- 数据与项目权限管理
- 地理空间数据可视化与分析
- 数据看板
- 大模型问答 / RAG（检索增强生成）
- 多智能体编排

## 目录结构

```
app/
  api/
    routes/           # REST API
  core/               # 配置与安全
  permissions/        # 权限与模型
  services/           # 业务能力（RAG / 智能体 / 分析等）
  dash_app.py          # Dash UI
  main.py              # FastAPI 入口
```

## 本地启动（示例）

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

访问：`http://localhost:8000`，Dash 页面挂载在 `/dash`。
