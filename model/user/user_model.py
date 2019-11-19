import psycopg2 as dbapi2
import os, config


class User:
    def __init__(self, username, password, fullname, email, gender, address, paid, activation, photo=None,
                 last_login=None, register_time=None, is_admin=None, is_activated=False):
        self.username = username
        self.password = password
        self.fullname = fullname
        self.email = email
        self.gender = gender
        self.address = address
        self.paid = paid
        self.photo = photo
        self.last_login = last_login
        self.register_time = register_time
        self.is_admin = is_admin
        self.activation = activation
        self.is_activated = is_activated


class user_database:
    def __init__(self):
        self.user = self.User()

    class User:
        def __init__(self):
            self.url = config.DATABASE_URL

        def add_user(self, user):
            with dbapi2.connect(self.url) as connection:
                cursor = connection.cursor()
                cursor.execute("""INSERT INTO users (username, password, fullname, email, gender, address, activation, 
                    is_admin, photo) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING user_id""", (user.username,
                                                                                                user.password,
                                                                                                user.fullname,
                                                                                                user.email,
                                                                                                user.gender,
                                                                                                user.address,
                                                                                                user.activation,
                                                                                                user.is_admin,
                                                                                                user.photo))
                user_id = cursor.fetchone()
                cursor.close()
            return user_id

        def get_user_id(self, username, password):
            with dbapi2.connect(self.url) as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT user_id FROM users WHERE (users.username = %s AND users.password = %s)",
                               (username, password))
                user_id = cursor.fetchone()
                cursor.close()
            return user_id

        def get_user_id_with_username(self, username):
            with dbapi2.connect(self.url) as connection:
                cursor = connection.cursor()
                statement = "SELECT user_id FROM users WHERE (users.username = '" + username + "')"
                cursor.execute(statement)
                user_id = cursor.fetchone()
                cursor.close()
            return user_id

        def get_user_id_with_email(self, email):
            with dbapi2.connect(self.url) as connection:
                cursor = connection.cursor()
                statement = "SELECT user_id FROM users WHERE (users.email = '" + email + "')"
                cursor.execute(statement)
                user_id = cursor.fetchone()
                cursor.close()
            return user_id
