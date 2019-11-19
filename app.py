from flask import Flask, request, session
from flask_mail import Mail
import dbinit
import controller.user.user_controller

app = Flask(__name__)
mail = Mail(app)



@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login')
def login():
    return controller.user.user_controller.login()


@app.route('/softflix.api.login', methods=['POST'])
def softflix_api_login():
    return controller.user.user_controller.login_checker(request)


@app.route('/softflix.api.validate_username', methods=['POST'])
def softflix_api_validate_username():
    return controller.user.user_controller.validate_username(request)


@app.route('/softflix.api.validate_email', methods=['POST'])
def softflix_api_validate_email():
    return controller.user.user_controller.validate_email(request)


@app.route('/softflix.api.register', methods=['POST'])
def softflix_api_register():
    return controller.user.user_controller.register_checker(request)

@app.route('/register')
def register():
    return controller.user.user_controller.register()


if __name__ == '__main__':
    dbinit.db_init()
    app.run()
