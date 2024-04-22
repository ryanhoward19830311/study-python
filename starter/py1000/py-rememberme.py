import json

def greet_user():
    filename = "py1000/username.json"
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("Please input your user name:")
        with open(filename, "w") as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}")


greet_user()