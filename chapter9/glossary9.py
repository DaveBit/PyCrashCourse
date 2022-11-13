# glossary copied from the solutions library.
# from python 3.7, dictionaries are ordered, so that OrderedDict makes no sense anymore.

from collections import OrderedDict

glossary_orderedDict = OrderedDict()

glossary1 = {

    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
    }

print('Adding the values to glossary_orderedDict...')
for key, value in glossary_orderedDict.items():
    glossary_orderedDict[key] = value
print("Done...")

print("_____Ordered dictionary_____")
for word, definition in glossary1.items():
    print("\n" + word.title() + ": \n" + definition)


print("_____Unordered dictionary_____")
for word, definition in glossary1.items():
    print("\n" + word.title() + ": " + definition)