cars = ['bmw', 'audi', 'toyota', 'subaru']
print('Unordered list: ')
print(cars)

cars.sort()
print('\nOrdered list: ')
print(cars)

cars.sort(reverse=True)
print('\nReversed ordered list: ')
print(cars)

print('\n Original list: ')
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

print('\n List sorted for now: ')
print(sorted(cars))
# sorted() can be used as follows: sorted(cars, reverse=True)

