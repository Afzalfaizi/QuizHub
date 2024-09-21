from fastapi import FastAPI, Request  
from quiz_backend.db.db_connector import get_session, create_tables  
from contextlib import asynccontextmanager  
import quiz_backend.models.admin_models  
import quiz_backend.models.user_models  
import quiz_backend.models.quiz_models  
from quiz_backend.utils.exception import NotFoundException, InvalidInputException, ConflictException 
from fastapi.responses import JSONResponse  
from fastapi import Depends

# Lifespan function to manage app startup tasks
@asynccontextmanager
async def lifeSpan(app: FastAPI):
    print("Create Table...")
    create_tables()  # Initialize and create tables
    yield

app = FastAPI(lifespan=lifeSpan)  # Create FastAPI app with lifespan handler

# Custom handler for "NotFoundException"
@app.exception_handler(NotFoundException)
def not_found(request: Request, exception: NotFoundException):
    return JSONResponse(status_code=404, content=f"{exception.not_found} Not found")

# Custom handler for "InvalidInputException"
@app.exception_handler(InvalidInputException)
def invalid_input(request: Request, exception: InvalidInputException):
    return JSONResponse(status_code=404, content=f"{exception.invalid_input}")

# Custom handler for "ConflictException"
@app.exception_handler(ConflictException)
def conflict_input(request: Request, exception: ConflictException):
    return JSONResponse(status_code=404, content=f"This {exception.conflict_input} already registered")

# Default route for the home page
@app.get("/")
def home():
    return {"Welcome to Quiz App Project"}

# Route to get a user by username, raises NotFoundException if not found
@app.get("/api/getUser")
def getUser(user: str):
    if user == "faizi":
        raise NotFoundException("User")
    return "User has been found"

# Route to validate user input
@app.get("/api/validateUser")
def validate_user(user: str):
    # Check if the user input contains only alphabetic characters
    if not user.isalpha():
        raise InvalidInputException("Invalid input: Only alphabetic characters are allowed.")
    # Ensure username length is between 3 and 20 characters
    if len(user) < 3 or len(user) > 20:
        raise InvalidInputException("Invalid input: Username must be between 3 and 20 characters.")
    return {"message": "User input is valid"}

# Predefined list of registered emails
registered_emails = ["faizidev@gmail.com", "haroon@gmail.com", "being@gmail.com"]

# Route to register a new user, raises ConflictException if email is already registered
@app.get("/api/register")
def register_user(email: str):
    if email in registered_emails:
        raise ConflictException("User")
    return {"message": "User has been registered successfully."}


# Note: Uncomment the following lines to run the app manually
# def start():
#     create_tables()
#     uvicorn.run("quiz_backend.route:app", host="127.0.0.1", port=8080, reload=True)

# Command to run the app with Poetry
# poetry run uvicorn quiz_backend.route:app --reload
