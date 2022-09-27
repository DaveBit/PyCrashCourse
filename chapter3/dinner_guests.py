guestList = ['roger federer', 'emma raducanu', 'rafa nadal']
name = guestList[0]
print("I would like to invite you " + name.title() + " for dinner")

name = guestList[1]
print("I would like to invite you " + name.title() + " for dinner")

name = guestList[2]
print("I would like to invite you " + name.title() + " for dinner")

# print(guestList[2].title() + " can't make it")
cantAttend = 'rafa nadal'
print(cantAttend.title() + " can't attend")
guestList.remove(cantAttend)
# in the solution of the exercise they use "del" statement. del(guestList[2])
guestList.append('novak djokovic')

name = guestList[0]
print("I would like to invite you " + name.title() + " for dinner")

name = guestList[1]
print("I would like to invite you " + name.title() + " for dinner")

name = guestList[2]
print("I would like to invite you " + name.title() + " for dinner")

# previously rafa nadal was on the last position of the list. So we could use remove/append/pop.
# let's remove now emma and insert tsipsipas

print("\nThe new guestList is:")
print(guestList)

print("Emma can't come today eventually")
del(guestList[1])
guestList.insert(1, 'stefanos tsitsipas')

print("The new guestList is: ")
print(guestList)

print("I found a bigger dinner table")
guestList.insert(0, 'mateo berretini')
print(len(guestList))
guestList.insert(3, 'cameron norrie')
guestList.append('casper ruud')

print("The new guestList is: ")
print(guestList)
print("\n")

# below we are using a loop. It doesn't have to be like that but not using it.
# loops will be seen later on.
for name in guestList:
    print(name.title() + " I invite you a dinner")
print("\n")

print("Just two people can be invited.")
while guestList:
    if len(guestList) > 2:
        name = guestList.pop()
        print("Sorry " + name.title() + ", I can't invite you for dinner")
    else:
        break

print("\n")
print(guestList[0] + ", You are still invited")
print(guestList[1] + ", You are still invited")
print('The number of guest invited is: ' + str(len(guestList)))
print("\n The final list is: ")
print(guestList)


del(guestList[0])
del(guestList[0])
# when we remove the first [0] the second item [1] becomes [0]

print('The list was deleted:')
print(guestList)
