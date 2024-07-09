from typing import Optional
from pydantic import BaseModel


class Update(BaseModel):
    message: Optional[dict] = None
