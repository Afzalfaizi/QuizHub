from fastapi import FastAPI,Request 
from quiz_backend.db.db_connector import get_session, create_tables
from contextlib import asynccontextmanager
import quiz_backend.models.admin_models
import quiz_backend.models.user_models
import quiz_backend.models.quiz_models
from quiz_backend.utils.exception import NotFoundException, InvalidInputException, ConflictException
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

@app.exception_handler(InvalidInputException)
def invalid_input(request:Request, exception: InvalidInputException):
   return JSONResponse(status_code=404, content=f"{exception.invalid_input}" )


@app.exception_handler(ConflictException)
def conflict_input(request:Request, exception: ConflictException):
   return JSONResponse(status_code=404, content=f"{exception.conflict_input} already registerd" )


@app.get("/")
def home():
    return {"Welcome to Quiz App Project"}

@app.get("/api/getUser")
def getUser(user:str):
    if user=="faizi":
        raise NotFoundException("User")
    return "user has found"

@app.get("/api/validateUser")
def validate_user(user: str):
    # Example validations
    if not user.isalpha():  # Only alphabetic characters allowed
        raise InvalidInputException("Invalid input: Only alphabetic characters are allowed.")
    if len(user) < 3 or len(user) > 20:  # Username length should be between 3 and 20 characters
        raise InvalidInputException("Invalid input: Username must be between 3 and 20 characters.")
    return {"message": "User input is valid"}



# Simulated list of registered emails
registered_emails = ["faizidev@gmail.com", "haroon@gmail.com","being@gmail.com"]

@app.get("/api/register")
def register_user(email: str):
    if email in registered_emails:
        raise ConflictException("User")
    return {"message": "User has been registered successfully."}









# def start():
#     create_tables()
#     uvicorn.run("quiz_backend.route:app", host="127.0.0.1", port=8080, reload=True)


# poetry run uvicorn quiz_backend.route:app --reload