favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']

# Print the names of all the pizzas.
for pizza in favorite_pizzas:
    print(pizza)
print("\n")

# Print a sentence about each pizza.
for pizza in favorite_pizzas:
    print("I really love " + pizza + " pizza!")

print("\nI really love pizza!")

friend_pizzas = favorite_pizzas[:]
favorite_pizzas.append('carbonara')
friend_pizzas.append('barbecue')

print('My favourite pizzas are: ')
for pizza in favorite_pizzas:
    print(pizza)

print("My friend's favourite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)
