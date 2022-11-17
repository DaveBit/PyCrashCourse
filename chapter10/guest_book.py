file_names = 'text_files/guest_book'

while True:
    name = input("What's your name? \n Enter 'quit' if you want to leave\n")
    if name == 'quit':
        break

    else:
        print("Hello " + name + "!" + "\n You have been added to the guest book!")
        with open(file_names, 'a') as file_object:
            file_object.write(name + "\n")

with open(file_names) as file_names:
    content = file_names.read()

print(content)