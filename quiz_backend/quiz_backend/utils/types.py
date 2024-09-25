from datetime import timedelta
from typing import TypedDict


TokenType = TypedDict(
    "TokenType", 
        {
            "user_name": str,
            "user_email": str,
            "access_expiry_time": timedelta,
            "refresh_expiry_time": timedelta
        })
66