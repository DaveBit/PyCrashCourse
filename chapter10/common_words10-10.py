filename = 'text_files/the_chinese_theater.txt'

with open(filename) as file:
    content = file.read()

theater_number = 0
theater_number += content.lower().count('the')

print(theater_number)

