from typing import List
from pydantic import BaseModel, Field
from datetime import datetime
from apps.books.models import Author


class BookSchema(BaseModel):
    """
    TODO
    """
    title: str = Field(max_length=30)
    description: str = Field(max_length=100)
    pub_date: datetime
    author_id: Author
    tags: List[str] = []


class BookCreateSchema(BookSchema):
    pass


class BookUpdateSchema(BaseModel):
    """
    TODO
    """
    title: str = Field(max_length=30)
    description: str = Field(max_length=100)
