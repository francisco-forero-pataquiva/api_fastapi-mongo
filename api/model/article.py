from pydantic import BaseModel
from typing import Optional


class Events(BaseModel):
    id: str
    provider: str
    
class Launches(BaseModel):
    id: str
    provider: str

class Article(BaseModel):
    id: int
    title: str
    url: str
    imageUrl: str
    newsSite: str
    summary: str
    publishedAt: str
    updatedAt: str
    featured: bool = False
    launches: Optional[list[Launches]] = None
    events: Optional[list[Events]] = None
