from pydantic import BaseModel

class Request(BaseModel):
    channel: str