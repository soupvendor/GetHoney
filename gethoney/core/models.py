from pydantic import BaseModel, HttpUrl

class Honeypot(BaseModel):
    name: str
    url: HttpUrl
    description: str

