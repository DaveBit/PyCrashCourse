from datetime import datetime

start_time = datetime.now()

# here below I assign to the list 9 numbers, but I do it without using the method list() and range() in one.
# it could have been done list(range(1,10)) this saves time.
ordinal_numbers = []
for number in range(1, 10):
    ordinal_numbers.append(number)

for number in ordinal_numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')

end_time = (datetime.now() - start_time)
print(end_time)

start_time = datetime.now()

# below we use the functions as expected. Omitting the first loop, and not using (f'{number}st') the execution time
# is reduced by half.
ordinal_numbers = list(range(1, 10))

for number in ordinal_numbers:
    if number == 1:
        print('1st')
    elif number == 2:
        print('2nd')
    elif number == 3:
        print('3rd')
    else:
        print(str(number) + 'th')

end_time = (datetime.now() - start_time)
print(end_time)
