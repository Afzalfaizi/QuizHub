from typing import Optional
from sqlmodel import SQLModel, Field

class Category(SQLModel, table=True):
    category_id: Optional[int] = Field(None, primary_key=True)
    category_name: str 
    category_description: str

class Quiz(SQLModel, table=True):
    quiz_id: Optional[int] = Field(None, primary_key=True)