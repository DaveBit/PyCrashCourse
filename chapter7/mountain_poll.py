responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat's your name?")
    response = input("Which mountain would you like ot climb someday?")
    responses[name] = response  # in the key name we add the response. it's a dictionary.
    repeat = input("would you lie to let another person respond (yes/no) ")

    if repeat.lower() == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb the " + response + ".")

