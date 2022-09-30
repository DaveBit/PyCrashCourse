countries = ['spain', 'france', 'slovakia', 'italy', 'slovenia', 'poland', 'austria']
favouriteCountry = 'slovakia'
# in this exercise the idea is to apply all the methods used in this chapter.

print("Original list: \n", countries)
countries[1] = 'andorra'
countries.append('luxembourg')
countries.insert(0, 'uk')
print("Andorra set at 1, append luzembourg, insert uk at 0", countries)
del countries[0]
print("Deleted  country at 0", countries)
lastCountryVisited = countries.pop()
print("pop:", lastCountryVisited)
print("list after pop:", countries)
italy = countries.pop(3)
print("pop at 3:", italy)
countries.remove(favouriteCountry)
print("remove favourite country which was slovakia:", countries)
countries.sort()
print("sort the list:", countries)
print("sorted list with reverse:", sorted(countries, reverse=True))
print("sorted doesn't change the order, just at printing:", countries)
countries.reverse()
print("reversing the reversed", countries)
print("printing the length: ", str(len(countries)))


