from datetime import datetime
favorite_numbers = {'Katus': [5, 6, 9, 10],
                    'Dave': [9, 15, 25, 24],
                    'Lorenzo': [15, 38, 100],
                    'hernesto': [1, 75, 29],
                    'Belardo': [38, 50, 69]
                    }
for name, values in favorite_numbers.items():
    if len(values) != 1:
        print(name + "'s favorite numbers are: ")
        for number in values:
            print("\t" + str(number))
