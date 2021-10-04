from helpers import check_user_existence, get_user
from aut_app import login
from helpers import get_user

username = input("enter ur username: ")
password = input("Enter ur password: ")


if check_user_existence(username):
    user = get_user(username)
    logged_in = login(user,password)
    if logged_in:
        user["logged_in"] = True
        print(user)
    else:
        print("Please, enter a valid password")
else:
    print("Please, enter a valid username")
