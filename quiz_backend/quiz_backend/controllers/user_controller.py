from quiz_backend.utils.imports import User, Token, UserModel, Session, select



def signUp(user_form:UserModel, session: Session):
    # TODO: verify if user exist
    # select(User).where(User.user_email==user_form.user_email)
    hashed_password = passwordIntoHash(user_form.user_password)
    user(user_name= user_form.user_name,user_email=user_form.user_email,)