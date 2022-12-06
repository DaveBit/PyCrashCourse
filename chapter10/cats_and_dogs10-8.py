cats_file = 'text_files/cats.txt'
dogs_file = 'text_files/dogs.txt'

try:
    with open(cats_file, 'r') as cats:
        cat_content = cats.read()

    with open(dogs_file, 'r') as dogs:
        dog_content = dogs.read()

    print(cat_content)
    print(dog_content)
except FileNotFoundError:
    print("Something went wrong")
