import json


def ask_number():
    """This functions ask for a number"""
    filename = "favorite_number.json"
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        while True:
            number = input("\nWhat's your favorite number?")
            if number.isnumeric():
                store_number(number)
                break
            else:
                print("\nThat's not a numeric entry. Try again.")
                continue
    else:
        print("I know your favorite number! It's " + str(number) + ".")


def store_number(number):
    """This function stores the number in a file, if it does not exist, it's created"""
    filename = "favorite_number.json"
    try:
        with open(filename, 'w') as f_obj:
            json.dump(number, f_obj)
            print("\nThe number was stored")
    except FileNotFoundError:
        with open(filename, 'w+') as f_obj:
            json.dump(number, f_obj)
            print("\nA new file has been created and the number was stored.")


ask_number()
