from quiz_backend.utils.imports import User, Token, UserModel, Session, select
from quiz_backend.utils.exception import ConflictException



def signUp(user_form:UserModel, session: Session):
    # TODO: verify if user exist
    user_exist = session.exec(select(User).where(User.user_email==user_form.user_email)).all()
    if user_exist:
        raise ConflictException("email")
    hashed_password = passwordIntoHash(user_form.user_password)
    user(user_name= user_form.user_name,user_email=user_form.user_email,user_password=hashed_password)
    session.add(user)
    session.commit()
    session.refresh(user)

    #TODO: generate access token and refresh token
