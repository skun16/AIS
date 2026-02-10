from pydantic import BaseModel


class ProjectSummary(BaseModel):
    id: str
    name: str
    owner: str
    status: str
