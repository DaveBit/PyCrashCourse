#  dictionaries on a list

pets = []

pet = {
    'owner': 'roberto',
    'name': 'jack',
    'weight': 15,
    'kind': 'beagle dog',
    }
pets.append(pet)

pet = {
    'owner': 'michael',
    'name': 'garfield',
    'weight': 7,
    'kind': 'red bengal cat',
    }
pets.append(pet)

pet = {
    'owner': 'clara',
    'name': 'levi',
    'weight': 1,
    'kind': 'red factor canary',
    }
pets.append(pet)

for pet in pets:
    print("Here is what I know about " + pet['name'].title())
    for key, value in pet.items():
        print("\t" + key.title() + ": " + str(value))
