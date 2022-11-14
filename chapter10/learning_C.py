print("\n---My solution---")
with open ('text_files/i_have_learned_so_far.txt') as file_object:
    for line in file_object:
        if 'Python' in line:
            line = line.replace('Python', 'C').rstrip()
            print(line)

# or
print("\n---Exercise solution using a list---")
with open ('text_files/i_have_learned_so_far.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace('Python', 'C').rstrip()
    print(line)
