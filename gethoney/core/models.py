from pydantic import BaseModel, HttpUrl


class Honeypot(BaseModel):
    name: str
    url: HttpUrl
    description: str = ""

class Log(BaseModel):
    name: str
    log_id: int
    honeypot_id: int