import uuid
from typing import Optional
from pydantic import BaseModel, Field

class Request(BaseModel):
    id : int
    username : str 
    no_rekening : str
    nama : str
    no_hp : str
    email : str
