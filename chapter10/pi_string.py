""" Working with a file's content"""

filename = 'text_files/pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()  # when you read, numbers are read as a string. You may use int().

pi_string = ''
for line in lines:
    pi_string += line.strip()  # removes the blank spaces.

print(pi_string)
print(len(pi_string))