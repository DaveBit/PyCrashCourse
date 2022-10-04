age = 0

while True:
    try:
        age = int(input("What's your age?"))
    except ValueError:
        print('Please, enter an integer')
        continue  # continue makes the iteration to start over again.
    print('You have entered: ', age)
    break  # breaks makes the iteration to stop and continue with the code.

if age < 2:
    print('You are a baby')
elif age < 4:
    print('You are a toodler!')
elif age < 13:
    print('You are a kid')
elif age < 20:
    print('You are an teenager')
elif age < 65:
    print('You are an adult')
else:
    print('You are an elder!')
