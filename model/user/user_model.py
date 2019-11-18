import psycopg2 as dbapi2
import os, config

class User:
    def __init__(self, username, password, fullname, email, phone, gender, address, paid, photo=None, last_login=None,
                 register_time=None, is_admin=None):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email
        self.phone = phone
        self.gender = gender
        self.address = address
        self.paid = paid
        self.photo = photo
        self.last_login = last_login
        self.register_time = register_time
        self.is_admin = is_admin


class user_database:
    def __init__(self):
        self.user = self.User()

    class User:
        def __init__(self):
            self.url = config.DATABASE_URL

        def add_user(self, user):
            with dbapi2.connect(self.url) as connection:
                cursor = connection.cursor()
                statement = "INSERT INTO users (username, password, fullname, email, phone, gender, address"
                if user.photo is not None:
                    statement += "photo"
                if user.is_admin is not None:
                    statement += "is_admin"

                statement += ") VALUES ("+ user.username + ", " + user.password, ", " + user.fullname + ", " + user.email +\
                    ", " + user.phone + ", " + user.gender + ", " + user.address
                if user.photo is not None:
                    statement += ", " + user.photo
                if user.is_admin is not None:
                    statement += ", " + user.is_admin
                statement += ")"
                cursor.execute(statement)
                cursor.close()

        def get_user_id(self, username, password):

            with dbapi2.connect(self.url) as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT user_id FROM users WHERE (users.username = %s AND users.password = %s)",
                               (username, password))
                user_id = cursor.fetchone()
                cursor.close()
            return user_id

