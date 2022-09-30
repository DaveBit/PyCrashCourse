print('---Using my_food[:]---')

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods[:]  # way easier than in java :) Just assign one array to another and that's it.

print(my_foods)
print(friend_food)

my_foods.append('cannoli')
friend_food.append('ice cream')

print(my_foods)
print(friend_food)

print('---Using my_food---')

my_foods2 = ['pizza', 'falafel', 'carrot cake']
friend_food2 = my_foods2  # don't forget the [:] otherwise, we are not coping the array but connecting them.

print(my_foods2)
print(friend_food2)

my_foods2.append('cannoli')
friend_food2.append('ice cream')

print(my_foods2)
print(friend_food2)
