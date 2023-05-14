from pydantic import BaseModel, Field


class Author(BaseModel):
    first_name: str = Field(max_length=20)
    last_name: str = Field(max_length=20)
    ref: str
