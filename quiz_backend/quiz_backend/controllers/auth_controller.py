# Import the JWTError and jwt module from the jose package to handle JSON Web Tokens (JWT).
from jose import jwt, JWTError
# Import CryptContext from passlib to handle password hashing and verification.
from passlib.context import CryptContext
# Import timedelta from datetime to manage token expiry times.
from datetime import timedelta
# Import the algorithm used for encoding JWTs from the quiz_backend.settings file.
from quiz_backend.settings import algorithm
# Create an instance of CryptContext, using bcrypt for password hashing.
pwd_context = CryptContext(schemes="bcrypt")



# Function to generate an access token
# Parameters:
#   - data (dict): the payload to be encoded in the token
#   - expiry_time (timedelta): the token's expiration time
def generateToken(data, expiry_time: timedelta):
    try:
        to_encode_data = data.copy() 
        to_encode_data.update({
            "exp": expiry_time
        })
        token = jwt.encode(to_encode_data, secret_key, algorithm="algorithm")
        return token
    except JWTError as je:
        print(je)

# Placeholder function to verify passwords
def verfiyPassword():
    ...

# Placeholder function for token services (e.g., validation, decoding)
def tokenService():
    ...

