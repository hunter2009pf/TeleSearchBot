from typing import Optional
from pydantic import BaseModel


class VersionResponse(BaseModel):
    service_name: str
    version: str


class SimpleResponse(BaseModel):
    code: int
    message: str
    data: dict = None
