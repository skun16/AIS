from dataclasses import dataclass


@dataclass
class AuthContext:
    user_id: str
    tenant_id: str
    roles: list[str]


def verify_wecom_ticket(ticket: str) -> AuthContext:
    """占位实现：企业微信票据校验。"""
    return AuthContext(user_id="demo", tenant_id="tenant-demo", roles=["admin"])
