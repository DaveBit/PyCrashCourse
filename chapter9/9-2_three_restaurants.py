class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("The restaurant name is: " + self.restaurant_name + "\n and the cuisine type is " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open")


restaurant1 = Restaurant('La Lola', 'spanish')
restaurant2 = Restaurant('Eureka', 'slovak')
restaurant3 = Restaurant('San Cho', 'Chinese')

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant1.describe_restaurant()