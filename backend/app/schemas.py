from pydantic import BaseModel
from datetime import datetime


class ContentRequest(BaseModel):
    platform: str
    tone: str
    content_type: str
    prompt: str

class ContentResponse(BaseModel):
    id: int
    platform: str
    tone: str
    content_type: str
    prompt: str
    generated_text: str
    created_at: datetime

    class Config:
        orm_mode = True

