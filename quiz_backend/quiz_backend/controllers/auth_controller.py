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
def generateAccessToken(data, expiry_time: timedelta):
    try:
        # Make a copy of the payload data
        to_encode_data = data.copy() 
        # Add expiration time to the token payload
        to_encode_data.update({
            "exp": expiry_time
        })
        # Encode the data into a JWT using the provided secret key and algorithm
        access_token = jwt.encode(to_encode_data, secret_key, algorithm="algorithm")
        # Return the generated access token
        return access_token
    except JWTError as je:
        print(je)

# Placeholder function to generate a refresh token
def generateRefreshToken():
    ...

# Placeholder function to verify passwords
def verfiyPassword():
    ...

# Placeholder function for token services (e.g., validation, decoding)
def tokenService():
    ...

