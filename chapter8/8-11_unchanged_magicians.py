def show_magicians(magicians: list):
    for magician in magicians:
        print(magician.title())


def make_great(magicians: list):
    great_magicians = []

    print("Populating great_magicians... ")
    while magicians:
        great_magicians.append(magicians.pop() + " the Great")

    if not magicians:
        print("\nMagicians is empty now")

    print("\nPopulating magicians again...")
    while great_magicians:
        magicians.append(great_magicians.pop())
    """
    This method would be faster than the above. Since it just add to the original list, 
    and does not work on two lists. 

    for great_magician in great_magicians:
        magicians.append(great_magician)
    """
    print("\nProcess done\n")
    return magicians


magicians_names = ['Rodrigo', 'Pepe', 'Hernesto', 'Bernardo', 'Kalas']

new_magicians = []

print("\n---Magicians before:---")
show_magicians(magicians_names)
new_magicians = make_great(magicians_names[:])
print("\n---Magicians Original list not altered:---")
show_magicians(magicians_names)
print("\n---New list with 'The great included'---")
show_magicians(new_magicians)
