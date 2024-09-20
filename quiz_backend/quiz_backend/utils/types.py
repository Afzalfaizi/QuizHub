from quiz_backend.utils.imports import TypedDict, timedelta

TokenType = TypedDict(
    "TokenType",
    {
        "user_name": str,
        "user_email": str,
        "access_expiry_time":timedelta,
        "refresh_expiry_time":timedelta
    }
    )