# here below some examples of dictionaries, how to create them and how to delete key-values

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'
print(alien_0)

print("The alien 0 is " + alien_0['color'])

alien_1 = {}
alien_1['color'] = 'red'
alien_1['points'] = 10
alien_1['x_position'] = 100
alien_1['y_position'] = 25

print("The alien 0 is " + alien_0['color'])
alien_0['color'] = 'red'
print("The alien 0 is " + alien_0['color'])

print('Original x-position: ' + str(alien_0['x_position']))
del alien_1['points']
print(alien_1)
