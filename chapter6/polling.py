favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'Edward': 'ruby',
    'phil': 'python',
    }

people = ['roBerto', 'Jennifer', 'Eusebio', 'phil', 'edward', 'sarah']
people_lower = [name.lower() for name in people]  # this is the short way of doing it.

# the below is an alternative way of lowering a list.
# for names in people:
#   people_lower.append(names.lower())

for name in people_lower:
    if name.lower() in favorite_languages.keys():
        print(name.title() + ', Thanks for participating')
    else:
        print('Please ' + name + ', take some time to do the poll')
