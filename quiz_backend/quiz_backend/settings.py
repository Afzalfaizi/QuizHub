from starlette.config import Config
from quiz_backend.utils.imports import timedelta
try:
    config = Config(".env")
except FileNotFoundError as e:
    print(e)

db_url = config("DB_URL")
db_test_url = config("DB_TEST_URL")
access_expiry_time = timedelta(minutes=int(config.get("ACCESS_EXPIRY_TIME")))
refresh_expriy_time = timedelta(days=int(config.get("REFRESH_EXPIRY_TIME")))
secret_key = config.get("SECRET_KEY")
algorithm = config.get("ALGORITHM", default="HS256")  # Provide a default if missing
