import config
import os
import sys
import psycopg2 as dbapi2

INIT_STATEMENTS = [

    """DROP TABLE IF EXISTS users cascade""",

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

    )""",

    """CREATE TABLE movie (
        movie_id SERIAL PRIMARY KEY,
        poster_url text,
        overview text,
        release_date time without time zone,
        movie_api_id integer,
        title text,
        backdrop_path text,
        popularity double precision,
        vote_count text,
        vote_average double precision,
        original_language character varying(5)
    )""",

    """CREATE TABLE genre (
        genre_id SERIAL PRIMARY KEY,
        genre character varying(25) NOT NULL
    )""",

    """CREATE TABLE movies_genre (
        movie_id integer REFERENCES movie(movie_id),
        genre_id integer REFERENCES genre(genre_id)
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
