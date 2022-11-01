sandwich_orders = ['Vegan sandwich', 'meatlove sandwich', 'mixt sandwich', 'egg_sandwich', 'egg_sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made you a " + current_sandwich)
    finished_sandwiches.append(current_sandwich)

nonrepeated_finished_sandwiches = set(finished_sandwiches)

print("---Sandwiches made today---")
for sandwich in nonrepeated_finished_sandwiches:
    print(sandwich)



