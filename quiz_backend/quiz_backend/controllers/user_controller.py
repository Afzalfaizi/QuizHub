from quiz_backend.utils.imports import User, Token, UserModel, Session, select, verfiyPassword, generateToken, ConflictException
from quiz_backend.utils.exception import ConflictException
from quiz_backend.settings import access_expiry_time, refresh_expriy_time


def signUp(user_form:UserModel, session: Session):
    users = session.exec(select(User))
    
    for user in users:
        is_email_exist = user.user_email == user_form.user_email
        is_password_exist = verfiyPassword(user.user_password, user.user_password)
        if  is_email_exist and is_password_exist:
            raise ConflictException("email and password")
        elif is_email_exist:
            raise ConflictException("email")
        elif is_password_exist:
            raise ConflictException("password")

    hashed_password = passwordIntoHash(user_form.user_password)
    user = User(user_name= user_form.user_name,user_email=user_form.user_email, user_password=hashed_password)
    session.add(user)
    session.commit()
    session.refresh(user)

# Generate access token and refresh token
data = {
    "user_name": user.user_name,
    "user_email": user.user_email
}
access_token = generateToken(data=data, expiry_time=access_expiry_time,)
refresh_token = generateToken(data=data, expiry_time=refresh_expriy_time)
token = Token(refresh_token=refresh_token)
session.add(token)
sessin.commit()
return {
    "access_token": access_token,
    "refresh_token": refresh_token}