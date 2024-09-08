from sqlmodel import SQLModel, create_engine, Session
from quiz_backend.settings import db_test_url, db_url


engine = create_engine(db_url)

def get_session():
    with Session(engine) as session:
        yield session



# def create_tables():
#     SQLModel.metadata.create_all(engine)