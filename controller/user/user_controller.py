import hashlib
from itsdangerous import URLSafeTimedSerializer
import view.user.user_view
from flask import session
import model.user.user_model
import config
import mail_sender

user_database = model.user.user_model.user_database()


def login():
    return view.user.user_view.login()


def login_checker(request):
    username = request.form['username']
    password = request.form['password']
    salted_pass = password + config.password_salt
    hashed_pass = hashlib.md5(salted_pass.encode())
    hashed_password = hashed_pass.hexdigest()
    user_id = user_database.user.get_user_id(username, hashed_password)
    print('user_id', user_id)
    if user_id is None:
        return "0"
    else:
        user = user_database.user.get_user(user_id)
        if user['user'].is_activated:
            return "1"
        else:
            return "-1"


def register():
    return view.user.user_view.register()


def validate_username(request):
    username = request.form['username']
    user_id = user_database.user.get_user_id_with_username(username)

    if user_id is None:
        return "1"
    else:
        return "0"


def validate_email(request):
    email = request.form['email']
    if len(email.split('@')) == 0:
        return "-1"
    else:
        if len(email.split('@')[0]) == 0 or len(email.split('@')[1]) == 0:
            return "-1"
        else:
            if len(email.split('@')[1].split('.')) == 0:
                return "-1"
            else:
                if len(email.split('@')[1].split('.')[0]) == 0 or len(email.split('@')[1].split('.')[1]) == 0:
                    return "-1"

    user_id = user_database.user.get_user_id_with_email(email)

    if user_id is None:
        return "1"
    else:
        return "0"


def send_activation_mail(request):
    username = request.form['username']
    email = user_database.user.get_email_with_username(username)
    if email is None:
        return "0"

    activation = user_database.user.get_activation_with_email(email[0])
    if activation is None:
        return "0"
    else:
        message = """<br>"""
        message += """<strong>Welcome to SoftFlix</strong><br>"""
        message += """<p>Please click the below link to activate your account</p>"""
        message += """<a href='http://127.0.0.1:5000/activate/""" + activation[0] + """'>Activate</a>"""
        res = mail_sender.send_activation_email("SoftFlix - Activation", message, email[0])
        if res == -1:
            return "0"
        else:
            return "1"


def register_checker(request):
    username = request.form['username']
    flag = validate_username(request)
    if flag == "0" or not(8 <= len(username) <= 25):
        return "-1"

    password = request.form['password']

    if not (8 <= len(password) <= 25):
        return "-1"

    salted_pass = password + config.password_salt
    hashed_pass = hashlib.md5(salted_pass.encode())
    hashed_password = hashed_pass.hexdigest()
    email = request.form['email']
    flag = validate_email(request)
    if flag == "0":
        return "-1"

    activation = generate_confirmation_token(email)
    fullname = request.form['fullname']
    if len(fullname) < 1:
        return "-1"

    gender = request.form['gender']
    if gender not in ["m", "f"]:
        return "-1"

    address = request.form['address']

    temp_user = model.user.user_model.User(username=username, password=hashed_password, fullname=fullname, email=email,
                                           gender=gender, address=address, paid=False, activation=activation,
                                           is_admin=False, is_activated=False)

    user_id = user_database.user.add_user(temp_user)
    if user_id is None:
        return "0"
    else:
        message = """<br>"""
        message += """<strong>Welcome to SoftFlix</strong><br>"""
        message += """<p>Please click the below link to activate your account</p>"""
        message += """<a href='http://127.0.0.1:5000/activate/""" + temp_user.activation + """'>Activate</a>"""
        mail_sender.send_activation_email("SoftFlix - Activation", message, temp_user.email)
        return "1"


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(config.SECRET_KEY)
    return serializer.dumps(email, salt=config.SECURITY_PASSWORD_SALT)# .split(".")[0]


def confirm_token(token, expiration=10800):
    serializer = URLSafeTimedSerializer(config.SECRET_KEY)
    try:
        email = serializer.loads(
            token,
            salt=config.SECURITY_PASSWORD_SALT,
            max_age=expiration
        )
    except:
        return False
    return email
