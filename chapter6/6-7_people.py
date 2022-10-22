people = []

person = {'first_name': 'Hernesto',
          'last_name': 'fernandez',
          'height': 181,
          'eyes color': 'blue',
          'profession': 'Engineer',
          'age': 34,
          'city': 'Palm City',
          }

people.append(person)

person = {'first_name': 'David',
          'last_name': 'Torres',
          'height': 186,
          'eyes color': 'green',
          'profession': 'Social Sciences',
          'age': 38,
          'city': 'Valencia',
          }

people.append(person)

person = {'first_name': 'Fabian',
          'last_name': 'Rodriguez',
          'height': 175,
          'eyes color': 'brown',
          'profession': 'psychologist',
          'age': 26,
          'city': 'Berlin',
          }

people.append(person)

for person in people:
    name = person['first_name'].title() + " " + person['last_name'].title()
    age = str(person['age'])
    city = person['city'].title()
    print(name + " is " + age + " and comes from " + city)
    print("The profession is : ", person['profession'] + "\n")


'''
for person in people:
    for key, value in person.items():
        print(key + ": " + str(value))
    print("\n")
'''
