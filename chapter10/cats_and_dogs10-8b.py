filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        print("Reading file: " + filename)
        with open('text_files/'+filename) as file:
            content = file.read()
            print(content + "\n")
    except FileNotFoundError:
        print("It seems like something went wrong...")
