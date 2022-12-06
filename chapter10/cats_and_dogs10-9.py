filenames = ['cats.txt', 'dogs.txt']


for filename in filenames:
    try:
        with open('text_files/'+filename) as file:
            content = file.read()

    except FileNotFoundError:
        pass

    else:
        print("Reading file: " + filename)
        print(content + "\n")
