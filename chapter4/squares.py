squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)

print(squares)

# you can write this 3 lines code into 1 line using 'List Comprehensions'

squares2 = [value**2 for value in range(1, 11)]
print(squares2)
