from quiz_backend.utils.imports import User, Token, UserModel,LoginModel, Session, select, Annotated,Depends, verfiyPassword, generateToken,decodeToken, ConflictException
from quiz_backend.utils.exception import ConflictException, NotFoundException, InvalidInputException
from quiz_backend.settings import access_expiry_time, refresh_expriy_time
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from quiz_backend.controller.auth_controller import generateAccessAndRefreshToken

def signUp(user_form: UserModel, session: Session):
    # Retrieve all users from the database
    users = session.exec(select(User))
    # Check if email or password already exists in the database
    for user in users:
        is_email_exist = user.user_email == user_form.user_email
        is_password_exist = verfiyPassword(user.user_password, user.user_password)
        # Raise exception if email and password both match
        if is_email_exist and is_password_exist:
            raise ConflictException("email and password")
        # Raise exception if only email exists
        elif is_email_exist:
            raise ConflictException("email")
        # Raise exception if only password exists
        elif is_password_exist:
            raise ConflictException("password")

    # Hash the user's password and create a new user record
    hashed_password = passwordIntoHash(user_form.user_password)
    #create a new user
    user = User(user_name=user_form.user_name,
                user_email=user_form.user_email, user_password=hashed_password)
    # Add and commit the new user to the database
    session.add(user)
    session.commit()
    session.refresh(user)

    # Prepare token data with user's name and email
    data = {
        "user_name": user.user_name,
        "user_email": user.user_email,}
    access_token = generateToken(data=data, expiry_time=access_expiry_time)
    refresh_token = generateToken(data=data, expiry_time=refresh_expriy_time)
    token = Token(refresh_token=refresh_token)
    session.add(token)
    session.commit()  
    # Return the generated tokens
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }


# Login Function

def login(login_form: OAuth2PasswordRequestForm, session:Session):
    users = session.exec(select(User))
    for user in users:
        user_email = user.user_email
        verify_password = verfiyPassword(user.user_password, login_form.password)
        if user_email == login_form.username and verify_password:
            data = {
                "user_name": user.user_name,
                "user_email": user.user_email,
                }
            access_token = generateToken(data=data, expiry_time=access_expiry_time)
            refresh_token = generateToken(data=data, expiry_time=refresh_expriy_time)
            Token = Token(refresh_token=refresh_token)
            session.add(token)
            session.commit()
            session.refresh(token)
            return {
                "access_token": access_token,
                "refresh_token": refresh_token
                }
        else:
            raise InvalidInputException("Email or Password")
            

def getUser(token:Annotated[str,Depends(auth_schema)], session:Session):
    try:
        if token:
            data = decodeToken(token)
            user_email = data["user_email"]
            user = session.exec(select(User).where(User.user_email == user_email)).one()
            return user
    except:
        raise NotFoundException("Token")
