from typing import Optional
from sqlmodel import SQLModel,Field

class Admin(SQLModel, table=True):
    admin_id: Optional[int] = Field(None, primary_key=True)
    admin_emain: str
    admin_name: str
    admin_password: str

class AdminToken(SQLModel, table=True):
    