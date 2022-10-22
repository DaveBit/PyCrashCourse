favorite_places = {
    'roberto': ['Valencia', 'Bratislava', 'Viena'],
    'hernesto': ['Barcelona', 'Teruel'],
    'Teresa': ['Praga']
    }

for name, places in favorite_places.items():
    print("\n" + name.title() + "'s favourite languages are: ")
    for place in places:
        print("\t" + place)


