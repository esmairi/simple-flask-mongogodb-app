import datetime
from typing import List
from pydantic import BaseModel, Field

from apps.books.models.author import Author


class AuthorSchema(BaseModel):
    """
    TODO
    """
    first_name: str = Field(max_length=20)
    last_name: str = Field(max_length=20)


class BookUpdateSchema(BaseModel):
    """
    TODO
    """
    first_name: str = Field(max_length=20)
    last_name: str = Field(max_length=20)
