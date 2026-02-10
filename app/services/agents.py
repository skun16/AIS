from dataclasses import dataclass


@dataclass
class AgentPlan:
    name: str
    objective: str
    tools: list[str]


def build_multi_agent_plan() -> list[AgentPlan]:
    return [
        AgentPlan(
            name="数据治理智能体",
            objective="梳理数据血缘、权限与质量指标",
            tools=["metadata", "lineage", "audit"],
        ),
        AgentPlan(
            name="空间分析智能体",
            objective="完成区域热力分析与时空对比",
            tools=["map", "analytics", "notebook"],
        ),
        AgentPlan(
            name="问答协同智能体",
            objective="调用RAG与大模型输出结论与引用",
            tools=["rag", "llm", "report"],
        ),
    ]
