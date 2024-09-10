from fastapi import FastAPI,Request 
from quiz_backend.db.db_connector import get_session, create_tables
from contextlib import asynccontextmanager
import quiz_backend.models.admin_models
import quiz_backend.models.user_models
import quiz_backend.models.quiz_models
from quiz_backend.utils.exception import NotFoundException
from fastapi.responses import JSONResponse

@asynccontextmanager
async def lifeSpan(app: FastAPI):
    print("Create Table...")
    create_tables()
    yield


app = FastAPI(lifespan=lifeSpan)


@app.exception_handler(NotFoundException)
def not_found(request:Request, exception: NotFoundException):
   return JSONResponse(status_code=404, content=f"{exception.not_found} Not found" )

@app.get("/")
def home():
    return {"Welcome to Quiz App Project"}

@app.get("/api/getUser")
def getUser(user:str):
    if user=="faizi":
        raise NotFoundException("User")
    return "user has found"

# def start():
#     create_tables()
#     uvicorn.run("quiz_backend.route:app", host="127.0.0.1", port=8080, reload=True)


# poetry run uvicorn quiz_backend.route:app --reload