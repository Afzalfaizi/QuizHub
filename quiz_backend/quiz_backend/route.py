from fastapi import FastAPI 
from quiz_backend.db.db_connector import get_session, create_tables
from contextlib import asynccontextmanager
import quiz_backend.models.admin_models
import quiz_backend.models.user_models
import quiz_backend.models.quiz_models
@asynccontextmanager
async def lifeSpan(app: FastAPI):
    print("Create Table...")
    create_tables()
    yield


app = FastAPI(lifespan=lifeSpan)

@app.get("/")
def home():
    return {"Welcome to Quiz App Project"}

# def start():
#     create_tables()
#     uvicorn.run("quiz_backend.route:app", host="127.0.0.1", port=8080, reload=True)