from fastapi import APIRouter

from app.services.analytics import DataInsight

router = APIRouter()


@router.get("/insights", response_model=list[DataInsight])
async def list_insights():
    """返回空间数据洞察（占位）。"""
    return [
        DataInsight(title="新增项目热区", description="本周新增项目集中在北部核心区"),
        DataInsight(title="数据覆盖率", description="POI 数据覆盖率提升到 92%"),
    ]
