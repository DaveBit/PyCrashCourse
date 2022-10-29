cities = {
    'valencia': {'fact': 'warm weather',
                 'population': 5000000,
                 'country': 'spain'},
    'bratislava': {'fact': 'cold weather',
                   'population': 10000000,
                   'country': 'slovakia'},
    'Abu dhabi': {'fact': 'hot weather',
                  'population': 1450000,
                  'country': 'he United Arab Emirates'},
}

for name, city in cities.items():
    print("Tell` me something about: " + str(name).title())
    for key, value in city.items():
        print("\t" + key.title() + ": " + str(value))


#  the below is an interesting approach if you want to print the dictionary values in a
#  defined order.
"""
for name, city in cities.items():
    country = city['country'].title()
    population = city['population']
    mountains = city['nearby mountains'].title()

    print("\n" + city.title() + " is in " + country + ".")
    print("  It has a population of about " + str(population) + ".")
    print("  The " + mountains + " mountains are nearby.")
"""