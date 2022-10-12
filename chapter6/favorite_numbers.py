from datetime import datetime
favorite_numbers = {'Katus': 5,
                    'Dave': 9,
                    'Lorenzo': 15,
                    'hernesto': 1,
                    'Belardo': 38
                    }
for names in favorite_numbers:
    print(names + "'s favorite number is: " + str(favorite_numbers[names]))

# the below process is according to the book and using the technics studied.
# the above otherwise, it's how the auto of this exercise would do.

num = favorite_numbers['Katus']
print("Katus' favorite number is " + str(num) + ".")


# favorite_numbers.keys is faster than favorite_numbers.
time = datetime.now()
if 'Kletus' not in favorite_numbers:
    print('hey hey')
time = datetime.now() - time
print(time)

time = datetime.now()
if 'Kletus' not in favorite_numbers.keys():
    print('hey hey')
time = datetime.now() - time
print(time)