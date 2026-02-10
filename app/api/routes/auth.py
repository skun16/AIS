from fastapi import APIRouter
from pydantic import BaseModel

from app.core.security import verify_wecom_ticket

router = APIRouter()


class WeComLoginRequest(BaseModel):
    ticket: str


@router.post("/wecom")
async def wecom_login(payload: WeComLoginRequest):
    """企业微信登录入口（占位）。"""
    auth_ctx = verify_wecom_ticket(payload.ticket)
    return {
        "user_id": auth_ctx.user_id,
        "tenant_id": auth_ctx.tenant_id,
        "roles": auth_ctx.roles,
    }
