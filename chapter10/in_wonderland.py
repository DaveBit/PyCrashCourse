def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        #  Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + " words.")
        books_dictionary[book.replace('.txt', '')] = int(num_words)



file = "text_files/alice_in_wonderland.txt"
filenames = ['alice_in_wonderland.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt', 'olala.txt']
books_dictionary = {}

for book in filenames:
    count_words('text_files/'+book)

books_dictionary_sorted = dict(sorted(books_dictionary.items(), key=lambda x: x[1], reverse=True))
#  sorted iterates through the dictionary, we retrieve the items, and organized them by an anonimous expression which
#  is lambda, takes one argument in this case (value) and sort them by value [1].

print(books_dictionary_sorted)
print("The longest book is " + (list(books_dictionary_sorted.keys())[0]).replace('_', ' ').title())
print("The longest book is " + next(iter(books_dictionary_sorted)).replace('_', ' ').title())
#  or
max_value = max(books_dictionary.values())
print(max_value)
print("The longest book is " + str(max(books_dictionary, key=books_dictionary.get)))
#  max looks for the highest value. First argument is the iterable.
#  second argument is the key we are going to use to find the max value.
#  we are using books_dictionary.get since it retrieves the value for each key.

print(max(books_dictionary))
print(books_dictionary)

