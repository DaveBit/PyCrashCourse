def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested. """
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)
    print(toppings)


make_pizza(18, 'pineapple')
make_pizza(15, 'mushrooms', 'green peppers', 'extra cheese')
