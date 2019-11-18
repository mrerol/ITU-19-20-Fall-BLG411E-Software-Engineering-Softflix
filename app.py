from flask import Flask
import dbinit

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    dbinit.db_init()
    app.run()
