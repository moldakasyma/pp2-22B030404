import psycopg2
from config import conn

config=psycopg2.connect(**conn)
current=config.cursor()

create_table='''CREATE TABLE snake(
    username VARCHAR(40),
    highscore INT NOT NULL,
    level INT NOT NULL
    );'''
    
current.execute(create_table)

current.close()
config.commit()
config.close()