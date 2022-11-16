import psycopg2
import settings
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection(
    settings.db_name, settings.db_user, settings.db_password,
    settings.db_host, settings.db_port
)


def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


create_database_query = "CREATE DATABASE teller"
create_database(connection, create_database_query)


connection_teller = create_connection(
    "teller", settings.db_user, settings.db_password,
    settings.db_host, settings.db_port
)


def execute_query(connection_teller, query):
    connection_teller.autocommit = True
    cursor = connection_teller.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


create_tables = '''
     CREATE TABLE IF NOT EXISTS TELLER
     (TELLER_ID SERIAL PRIMARY KEY,
     TELLER_NAME TEXT NOT NULL,
     CHAT_ID INT NOT NULL);

     CREATE TABLE IF NOT EXISTS GENRE
     (GENRE_ID SERIAL PRIMARY KEY,
     GENRE TEXT NOT NULL);

     CREATE TABLE IF NOT EXISTS STORY
     (STORY_ID SERIAL PRIMARY KEY,
     TELLER_ID INTEGER REFERENCES TELLER(TELLER_ID),
     GENRE_ID INTEGER REFERENCES GENRE(GENRE_ID),
     STORY TEXT,
     DATETIME time with time zone NOT NULL);

     CREATE TABLE IF NOT EXISTS COMMENT
    (COMMENT_ID SERIAL PRIMARY KEY,
     TELLER_ID INTEGER REFERENCES TELLER(TELLER_ID),
     COMMENT TEXT NOT NULL,
     DATETIME time with time zone NOT NULL);

     CREATE TABLE IF NOT EXISTS STORY_COMMENT
     (STORY_ID INTEGER REFERENCES STORY(STORY_ID),
     COMMENT_ID INTEGER REFERENCES COMMENT(COMMENT_ID));
    '''

execute_query(connection_teller, create_tables)

