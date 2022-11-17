filename = 'text_files/programming_poll.txt'
responses = []

while True:
    response = input("Why do you like programing? \n Enter 'quit' if you want to leave\n")
    if response == 'quit':
        break
    else:
        responses.append(response)


with open(filename, 'a') as file_object:
    for response in responses:
        file_object.write(response + "\n")

with open(filename) as file_object:
    content = file_object.read()

print(content)
