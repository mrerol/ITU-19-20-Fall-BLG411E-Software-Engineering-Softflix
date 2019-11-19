import config
import os
import sys
import psycopg2 as dbapi2

INIT_STATEMENTS = [

    """DROP TABLE IF EXISTS users cascade """,

    """CREATE TABLE IF NOT EXISTS users 
    (
        user_id SERIAL PRIMARY KEY,
        username text NOT NULL UNIQUE ,
        password text NOT NULL,
        fullname text NOT NULL,
        last_login timestamp without time zone DEFAULT CURRENT_TIMESTAMP,
        email text NOT NULL UNIQUE CHECK (email ~~ '%@%.%'::text),
        gender text,
        address text,
        register_time timestamp without time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
        paid boolean NOT NULL DEFAULT false,
        photo BYTEA,
        is_admin boolean NOT NULL DEFAULT false,
        is_activated boolean NOT NULL DEFAULT false,
        activation text NOT NULL UNIQUE

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
