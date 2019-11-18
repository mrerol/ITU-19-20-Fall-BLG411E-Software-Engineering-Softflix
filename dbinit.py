import config
import os
import sys
import psycopg2 as dbapi2

INIT_STATEMENTS = [

    """DROP TABLE IF EXISTS users cascade """,

    """CREATE TABLE IF NOT EXISTS users 
    (
        user_id SERIAL NOT NULL PRIMARY KEY,
        user_name VARCHAR(15) UNIQUE NOT NULL,
        email VARCHAR (50) NOT NULL,
        password VARCHAR (50) NOT NULL,
        name VARCHAR (50) NOT NULL,
        surname VARCHAR (50) NOT NULL,
        gender VARCHAR (1) NOT NULL,
        address VARCHAR (250) NOT NULL,
        last_login TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        register_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        is_admin BOOLEAN NOT NULL DEFAULT FALSE
    )"""


]




def initialize(url):
    with dbapi2.connect(url) as connection:
        cursor = connection.cursor()
        for statement in INIT_STATEMENTS:
            cursor.execute(statement)
        cursor.close()


def db_init():
    url = config.DATABASE_URL
    if url is None:
        print("Usage: DATABASE_URL=url python dbinit.py", file=sys.stderr)
        sys.exit(1)
    if config.DB_INIT_FLAG:
        initialize(url)
