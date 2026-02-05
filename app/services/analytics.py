from pydantic import BaseModel


class DataInsight(BaseModel):
    title: str
    description: str


def generate_dashboard_metrics() -> dict[str, int]:
    return {
        "projects": 12,
        "datasets": 58,
        "users": 340,
        "agents": 6,
    }
