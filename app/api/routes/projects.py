from fastapi import APIRouter

from app.permissions.models import ProjectSummary

router = APIRouter()


@router.get("/", response_model=list[ProjectSummary])
async def list_projects():
    """返回当前用户可见的项目列表（占位）。"""
    return [
        ProjectSummary(id="proj-001", name="城市更新", owner="demo", status="active"),
        ProjectSummary(id="proj-002", name="轨迹分析", owner="demo", status="planning"),
    ]
