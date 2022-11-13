"""Module to practice the different access options we have"""

#  using read()
with open('text_files/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    print(type(contents))

#  iterating line by line with a for loop.
with open('text_files/pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip())
    print(type(file_object))

#  Using the file content out of the 'with open' block
with open('text_files/pi_digits.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
print(type(lines))

#  testing open() without 'with'
file_object = open('text_files/pi_digits.txt')
file_object.close()
