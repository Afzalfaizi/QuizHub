from typing import Optional
from sqlmodel import SQLModel, Field

class Category(SQLModel, table=True):
    category_id: Optional[int] = Field(None, primary_key=True)
    category_name: str 
    category_description: str

class QuizLevel(SQLModel, table=True):
    quiz_id: Optional[int] = Field(None, primary_key=True)
    quiz_level : str
    

class Quiz(SQLModel, table=True):
    question_id : Optional[int] =  Field(None, primary_key=True)
    question: str