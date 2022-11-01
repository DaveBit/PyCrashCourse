poll = {}
name_prompt = "What's your name?"
place_prompt = "if you could visit one place in the world, where would you go?"
continue_prompt = "Are you the last user to respond? (yes/no)"


while True:
    name = input(name_prompt)
    response = input(place_prompt)
    poll[name] = response
    last_one = input(continue_prompt)
    if last_one.lower() == 'yes':
        break

for name, response in poll.items():
    print(name + " want's to go to " + response)


