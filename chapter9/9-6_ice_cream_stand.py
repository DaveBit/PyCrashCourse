from number_served_tiy import Restaurant


class IceCreamStand(Restaurant):
    """Represents the icecream stand"""

    def __init__(self, restaurant_name, cuisine_type='ice_cream'):
        """Initialize an ice cream stand"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['chocolate', 'strawberry', 'vanilla', 'mango']

    def show_flavours(self):
        """Display the flavours available"""
        print("The flavours available are: \n")
        for flavor in self.flavours:
            print(" - " + flavor.title())


icecreamstand1 = IceCreamStand("The big one")
icecreamstand1.describe_restaurant()
icecreamstand1.show_flavours()

