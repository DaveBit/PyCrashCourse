my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods[:]  # way easier than in java :) Just assign one array to another and that's it.

my_foods.append('cannoli')
friend_food.append('ice cream')

for food in my_foods:
    print(food)
for food in friend_food:
    print(food)
