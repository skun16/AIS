from pydantic import BaseModel


class Settings(BaseModel):
    app_name: str = "企业级地理数据智能平台"
    version: str = "0.1.0"
    wecom_corp_id: str = ""
    wecom_agent_id: str = ""


settings = Settings()
