from sqlmodel import SQLModel, create_engine, Session
from quiz_backend.settings import db_test_url, db_url

connection_string = str(db_url).replace("postgresql", "postgresql+psycopg2")
engine = create_engine(connection_string, echo=True)
def get_session():
    with Session(engine) as session:
        yield session

def create_tables():
    SQLModel.metadata.create_all(engine)