# break statement

prompt = "\nWhat's your age?"
prompt += "\nInsert your age in number:"
free_ticket = 0
tendollars_ticket = 0
fifteendollars_ticket = 0



while True:

    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Free entrance")
        free_ticket += 1
    elif age < 12:
        print("Your ticket is 10e")
        tendollars_ticket += 1
    else:
        print("Your ticket is 15e")
        fifteendollars_ticket += 1

total = tendollars_ticket*10 + fifteendollars_ticket*15
print("\nTotal cost is: " + str(total))
