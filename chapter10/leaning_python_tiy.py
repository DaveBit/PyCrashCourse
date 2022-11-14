print(" --- Reading in the entire file: ---")
with open ('text_files/i_have_learned_so_far.txt') as file_object:
    content = file_object.read()
    print(content)

print("\n--- Looping over the lines: ---")
with open ('text_files/i_have_learned_so_far.txt') as file_object:
    for line in file_object:
        print(line.rstrip())

print("\n--- Storing the lines in a list: ---")
with open ('text_files/i_have_learned_so_far.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

