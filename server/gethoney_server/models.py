from pydantic import BaseModel, HttpUrl


class Honeypot(BaseModel):
    name: str
    url: HttpUrl
    description: str = ""


class HoneypotResponse(Honeypot):
    id: int
    name: str
    url: HttpUrl
    description: str = ""
