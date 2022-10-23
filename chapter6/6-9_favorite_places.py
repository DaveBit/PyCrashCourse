favorite_places = {
    'roberto': ['Valencia', 'Bratislava', 'Viena'],
    'hernesto': ['Barcelona', 'Teruel'],
    'Teresa': ['Praga']
    }

for name, places in favorite_places.items():
    if len(places) == 1:
        print("\n" + name.title() + "'s favourite language is: ")
    else:
        print("\n" + name.title() + "'s favourite languages are: ")
    for place in places:
        print("\t" + place)


