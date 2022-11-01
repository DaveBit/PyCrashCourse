
sandwich_orders = ['Vegan sandwich',
                   'meatlove sandwich',
                   'mixt sandwich',
                   'pastrami',
                   'egg_sandwich',
                   'pastrami',
                   'egg_sandwich',
                   'pastrami']
finished_sandwiches = []

print("We ran out of Pastrami. ")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

if 'pastrami' not in sandwich_orders:
    print("No pastrami found in sandwich orders")
else:
    print("check again")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made you a " + current_sandwich)
    finished_sandwiches.append(current_sandwich)

nonrepeated_finished_sandwiches = set(finished_sandwiches)

print("---Sandwiches made today---")
for sandwich in nonrepeated_finished_sandwiches:
    print(sandwich)
