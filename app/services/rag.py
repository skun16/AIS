from dataclasses import dataclass


@dataclass
class RetrievalResult:
    chunk_id: str
    source: str
    content: str


def retrieve_knowledge(query: str) -> list[RetrievalResult]:
    return [
        RetrievalResult(
            chunk_id="demo-001",
            source="企业知识库",
            content=f"针对问题“{query}”，建议先核验数据权限与时空范围。",
        )
    ]
