from starlette.config import config

try:
    config = Config(".env")
except FileNotFoundError as e:
    print(e)

db_url = config("DATABASE_URL")
db_test_url = config("DATABASE_TESTING_URL")