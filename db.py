import psycopg2
import settings

con = psycopg2.connect(
  database = settings.DATABASE, 
  user = settings.DB_USER, 
  password = settings.DB_PASSWORD, 
  host = settings.BD_HOST, 
  port= settings.BD_PORT
)
cur = con.cursor()  

print("Database opened successfully")


cur.execute('''

     CREATE TABLE IF NOT EXISTS STORY  
     (STORY_ID INT PRIMARY KEY NOT NULL,
     USER_ID INT NOT NULL,
     GENRE_ID INT NOT NULL,
     STORY TEXT NOT NULL,
     DATETIME time with time zone NOT NULL);

     CREATE TABLE IF NOT EXISTS TELLER  
     (TELLER_ID INT PRIMARY KEY NOT NULL,
     TELLER_NAME TEXT NOT NULL,
     CHAT_ID INT NOT NULL);

     CREATE TABLE IF NOT EXISTS STORY_COMMENT  
     (STORY_ID INT NOT NULL,
     COMMENT_ID INT NOT NULL);

     CREATE TABLE IF NOT EXISTS COMMENT  
    (COMMENT_ID INT PRIMARY KEY NOT NULL,
     USER_ID INT NOT NULL,
     COMMENT TEXT NOT NULL,
     DATETIME time with time zone NOT NULL);

     CREATE TABLE IF NOT EXISTS GENRE  
     (GENRE_ID INT PRIMARY KEY NOT NULL,
     GENRE TEXT NOT NULL);
     
     ''')
     

print("Table created successfully")
con.commit()  
con.close()