from pydantic import BaseModel


class AgentData(BaseModel):
    unique_ips: int
    scanned_files: int
