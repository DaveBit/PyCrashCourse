toppinglist = []
topnumber = 1
topping = ""

print("What toppings would you like to add?")
while True:
    topping = input(f'Insert the popping number {topnumber}:')
    if topping.lower() == 'quit':
        break
    elif topping in toppinglist:
        print(f'"You have already added this topping, pick another one"')
    else:
        toppinglist.append(topping)
        topnumber += 1
        print(f'{topping} added to the pizza')

print(toppinglist)