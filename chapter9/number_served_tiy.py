class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describes the restaurate"""
        print("The restaurant name is: " + self.restaurant_name + "\n and the cuisine type is " + self.cuisine_type)
        print("The restaurant has served: " + str(self.number_served))

    def open_restaurant(self):
        """Display a message that the restaurant is open"""
        msg = self.restaurant_name + " is open. Come on in!"

    def set_number_served(self, number):
        """Allow user to set the number of customers that have been served"""
        if self.number_served <= number:
            self.number_served = number
        else:
            print("You can't decrease the number set")

    def increment_number_served(self, number):
        """Allow user to increment the number of customers served"""
        self.number_served += number

"""
my_restaurant = Restaurant('La espanola', 'spanish')
print(my_restaurant.number_served)

#  changing an attribute by accessing it.
my_restaurant.number_served = 10
print(my_restaurant.number_served)

#  updating the value with a method
my_restaurant.set_number_served(25)
print(my_restaurant.number_served)

#  increasing the value with a method
my_restaurant.increment_number_served(10)
print(my_restaurant.number_served)
"""