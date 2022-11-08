class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is: " + self.restaurant_name + "\n and the cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open")


my_restaurant = Restaurant('La Lola', 'spanish')

print("Nombre: " + my_restaurant.restaurant_name)
print("Cuisine: " + my_restaurant.cuisine_type)

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
