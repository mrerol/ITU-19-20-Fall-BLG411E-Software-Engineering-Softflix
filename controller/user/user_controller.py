import view.user.user_view
import model.user.user_model

user_database = model.user.user_model.user_database()


def login():
    print("aloo")
    return view.user.user_view.login()


def login_checker(request):
    username = request.form['username']
    password = request.form['password']
    user_id = user_database.user.get_user_id(username, password)
    print(user_id, username)
    if user_id is None:
        return "0"
    else:
        return "1"
