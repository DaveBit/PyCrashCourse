import json


def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()

    while True:
        response = input("Hey there, is " + username + " your username?\nYes/No.\n")
        if response.lower() == 'yes':
            print("Welcome back, " + username + "!")
            break
        elif response.lower() == 'no':
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
            break
        else:
            print("Please, answer yes or no")



greet_user()
