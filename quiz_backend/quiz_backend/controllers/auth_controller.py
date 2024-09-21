from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import timedelta
from quiz_backend.settings import algorithm, secret_key

pwd_context = CryptContext(schemes="bcrypt")



def generateToken(data, dict, expiry_time: timedelta):
    try:
        to_encode_data = data.copy() 
        to_encode_data.update({
            "exp": expiry_time
        })
        token = jwt.encode(to_encode_data, secret_key, algorithm="algorithm")
        return token
    except JWTError as je:
        raise je


def decodeToken(token:str):
    try:
        # decoded_data = jwt.decode(token, secret_key, algorithm="algorithm")
        return decodeToken   
    except JWTError as je:
        raise je
def passwordIntoHash(plaintext:str):
    hashedpassword = pwd_context.hash(plaintext)
    return hashedpassword

# Placeholder function to verify passwords
def verfiyPassword(hashPass:str, plaintext:str):
    verify_password = pwd_context.verify(plaintext, hash=hashPass)
    return verify_password


    access_token = generateToken(data, user_details["access_expiry_time"])
    refresh_token = generateToken(data, user_details["refresh_expiry_time"])
    
    return{
        "access_token":access_token,
        "refresh_token":refresh_token
    }

# Placeholder function for token services (e.g., validation, decoding)
def tokenService():
    ...

