from quiz_backend.utils.imports import User, Token, UserModel,LoginModel, Session, select, verfiyPassword, generateToken, ConflictException
from quiz_backend.utils.exception import ConflictException
from quiz_backend.settings import access_expiry_time, refresh_expriy_time




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
    user = User(user_name=user_form.user_name, user_email=user_form.user_email, user_password=hashed_password)
    
    # Add and commit the new user to the database
    session.add(user)
    session.commit()
    session.refresh(user)

    # Prepare token data with user's name and email
    data = {
        "user_name": user.user_name,
        "user_email": user.user_email
    }
    
    # Generate access and refresh tokens
    access_token = generateToken(data=data, expiry_time=access_expiry_time)
    refresh_token = generateToken(data=data, expiry_time=refresh_expriy_time)
    
    # Store the refresh token in the database
    token = Token(refresh_token=refresh_token)
    session.add(token)
    session.commit()  # Fixed typo: 'sessin' to 'session'

    # Return the generated tokens
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }

# login functionality 

def login(user_login_form: LoginModel, session: Session):
    # Retrieve all users from the database
    users = session.exec(select(User))
    for user in users:
        user_email = user.user_email
        verify_password = verfiyPassword(user.user_password, login_form.user_password)
        if user_email == login_form.user_email and verify_password:
                data = {
            "user_name": user.user_name,
            "user_email": user.user_email
        }
                # Generate access and refresh tokens
                access_token = generateToken(data=data, expiry_time=access_expiry_time)
                refresh_token = generateToken(data=data, expiry_time=refresh_expriy_time)
                # Store the refresh token in the database
                token = Token(refresh_token=refresh_token, user_id=user.id)
                session.add(token)
                session.commit()
                session.refresh(token)
                # Return the generated tokens
                return {
                    "access_token": access_token,
                    "refresh_token": refresh_token
                }
        else:
            InvalidInputException("Email or Password")
    


    
    # Update the refresh token in the database if it already exists
    token = session.exec(select(Token).where(Token.user_id == user.id)).first()
    if token:
        token.refresh_token = refresh_token
        session.commit()
       
    