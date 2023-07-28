import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Request(BaseModel):
    id : int
