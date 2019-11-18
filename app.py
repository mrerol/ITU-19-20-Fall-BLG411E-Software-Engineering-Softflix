from flask import Flask, request
import dbinit
import controller.user.user_controller

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login')
def login():
    return controller.user.user_controller.login()

@app.route('/softflix/api/login', methods=['POST'])
def softflix_api_login():
    print('softflix_api_login')
    return controller.user.user_controller.login_checker(request)



if __name__ == '__main__':
    dbinit.db_init()
    app.run()
