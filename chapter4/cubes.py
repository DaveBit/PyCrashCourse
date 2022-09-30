cubes = []
for number in range(1, 11):
    cubes.append(number**3)
for cube in cubes:
    print(cube)

cubes2 = [value**3 for value in range(1, 11)]
for cube in cubes2:
    print(cube)
