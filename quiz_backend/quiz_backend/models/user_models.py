from sqlmodel import SQLModel,Field
from typing import Optional

class User(SQLModel, table=True):
    user_id: Optional[int] = Field(None, primary_key=True)
    user_name: str
    user_email: str
    # TODO:
    # phone_number: int
    user_password: str

class Token(SQLModel, table=True):
    token_id: Optional[int] = Field(None, primary_key=True)
    refresh_token: str
