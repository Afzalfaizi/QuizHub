from jose import jwt, JWTError
from passlib.context import CryptContext

pwd_context = CryptContext(schemes="bcrypt")


def generateAccessToken():
    ...

def generateRefreshToken():
    ...

def verfiyPassword():
    ...

def tokenService():
    ...
