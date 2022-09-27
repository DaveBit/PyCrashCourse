countries = ['spain', 'france', 'slovakia', 'italy', 'slovenia', 'poland', 'austria']
favouriteCountry = 'slovakia'
# in this exercise the idea is to apply all the methods used in this chapter.

print(countries)
countries[1] = 'andorra'
countries.append('luxembourg')
countries.insert(0, 'uk')
print(countries)
del countries[0]
print(countries)
lastCountryVisited = countries.pop()
print(lastCountryVisited)
print(countries)
italy = countries.pop(3)
print(italy)
countries.remove(favouriteCountry)
print(countries)
countries.sort()
print(countries)
print(sorted(countries, reverse=True))
print(countries)
countries.reverse()
print(countries)
print(str(len(countries)))


