#using the list to acces the values

names1 = ['Car', 'Boat', 'Plane', 'Subway']
print("I would like to have a Mazda " + names1[0])
print("I would like to have a big " + names1[1])
print("I would like to have a boeing " + names1[2])
print("I would like to have a long " + names1[3])

#using the pop() methond.

names2 = ['Honda', 'Suzuki', 'Kawasaki']
print(names2)
print(names2.pop())
print(names2)

#using the del statement. Values shift.
names3 = ['Honda', 'Suzuki', 'Kawasaki']
del names3[1]
print(names3)
