from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import timedelta
from quiz_backend.settings import algorithm, secret_key


pwd_context = CryptContext(schemes="bcrypt")


def generateToken(data,dict, expiry_time: timedelta):
    try:
        to_encode_data = data.copy() 
        to_encode_data.update({
            "exp": expiry_time
        })
        token = jwt.encode(to_encode_data, secret_key, algorithm="algorithm")
        return token
    except JWTError as je:
        raise je
        

# Placeholder function to verify passwords
def verfiyPassword():
    ...

# Placeholder function for token services (e.g., validation, decoding)
def tokenService():
    ...

