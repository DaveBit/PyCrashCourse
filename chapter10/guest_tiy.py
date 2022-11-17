""" This is a program that prompts the user for their name. When they respond
, writes their name to a file called guests.txt"""

file_names = 'text_files/names'
if not file_names:
    file_names = 'text_files/names'

while True:
    name = input("What's your name? \n Enter 'quit' if you want to leave\n")
    if name == 'quit':
        break
    else:
        with open(file_names, 'a') as file_object:
            file_object.write(name + "\n")

with open(file_names) as file_names:
    content = file_names.read()

print(content)