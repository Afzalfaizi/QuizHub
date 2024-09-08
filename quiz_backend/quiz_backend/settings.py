from starlette.config import Config

try:
    config = Config(".env")
except FileNotFoundError as e:
    print(e)

db_url = config("DB_URL")
db_test_url = config("DB_TEST_URL")