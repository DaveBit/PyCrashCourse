#  A list of dictionaries
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green',
                 'points': 5,
                 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print("...")

print("The total number of aliens is: " + str(len(aliens)))

#  we could change the color of some of the aliens.

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
