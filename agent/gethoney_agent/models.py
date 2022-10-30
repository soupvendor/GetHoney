from pydantic import BaseModel


class AgentData(BaseModel):
    total_connections: int
    files_scanned: list
