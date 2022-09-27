locations = ['bratislava', 'valencia', 'mainz', 'rudesheim', 'london']

print('---Original list---')
print(locations)
print('\n---Using sorted(). Original list did not change---')
print(sorted(locations))
print(locations)
print('\n---Using sorted() with reverse. Original list did not change---')
print(sorted(locations, reverse=True))
print(locations)
print('\n---Using reverse. Original list did change this time---')
locations.reverse()
print(locations)
print('\n---Using reverse again. Original list did change this time---')
locations.reverse()
print(locations)
print('\n---Using sort(). Original list did change this time---')
locations.sort()
print(locations)
print('\n---Using sort() again with reverse. Original list did change this time---')
locations.sort(reverse=True)
print(locations)
