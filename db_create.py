from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.db_user}:{settings.db_password}@localhost:{settings.db_port}/teller'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
if not database_exists(engine.url):
    create_database(engine.url)

print(database_exists(engine.url))
