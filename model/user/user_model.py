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

        def get_user(self, user_id):
            temp_user = dict()
            temp_user['user_id'] = user_id
            _user = None
            with dbapi2.connect(self.url) as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM users WHERE (users.user_id = %s)",
                               (user_id, ))
                user = cursor.fetchone()
                _user = User(username=user[1], password=user[2], fullname=user[3], last_login=user[4], email=user[5],
                             gender=user[6], address=user[7], register_time=user[8], paid=user[9], photo=user[10],
                             is_admin=user[11], is_activated=user[12], activation=user[13])
                temp_user['user'] = _user
                cursor.close()
            return temp_user

        def get_activation_with_email(self, email):
            with dbapi2.connect(self.url) as connection:
                cursor = connection.cursor()
                statement = "SELECT activation FROM users WHERE (users.email = '" + email + "')"
                cursor.execute(statement)
                activation = cursor.fetchone()
                cursor.close()
            return activation

        def get_email_with_username(self, username):
            with dbapi2.connect(self.url) as connection:
                cursor = connection.cursor()
                statement = "SELECT email FROM users WHERE (users.username = '" + username + "')"
                cursor.execute(statement)
                email = cursor.fetchone()
                cursor.close()
            return email

