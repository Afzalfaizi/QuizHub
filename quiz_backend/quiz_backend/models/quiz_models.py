from typing import Optional
from sqlmodel import SQLModel, Field


class Category(SQLModel, table=True):
    category_id: Optional[int] = Field(None, primary_key=True)
    category_name: str 
    category_description: str


class QuizLevel(SQLModel, table=True):
    quiz_level_id: Optional[int] = Field(None, primary_key=True)
    quiz_level : str
    category_id: int = Field(int, foreign_key="category.category_id")




class Quiz(SQLModel, table=True):
    question_id : Optional[int] =  Field(None, primary_key=True)
    question: str
    quizlevel_id:int = Field(int, foreign_key="quizlevel.quiz_level_id")
    choice1: str
    choice2: str
    choice3: str
    choice4: str

class Choices(SQLModel, table=True):
    choice_id: Optional[int] = Field(None, primary_key=True)
    quiz_id:int = Field(int, foreign_key="quiz.question_id")
    choice: str
    status: bool = False

