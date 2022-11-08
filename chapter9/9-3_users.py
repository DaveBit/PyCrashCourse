class User():
    def __init__(self, first_name, last_name, **others):
        self.user_profile = {
            'first_name': first_name,
            'last_name': last_name,
        }
        for key, value in others.items():
            self.user_profile[key] = value

    def describe_user(self):
        """Display a summary of the user's information."""
        for key, value in self.user_profile.items():
            print(key + ": " + str(value))
        print("\n")

    def greet_user(self):
        print("Hello " + self.user_profile['first_name'])


user1 = User('Dave', 'bit', location='valencia', username='matroska', email='davedestroyer')
user1.describe_user()
user2 = User('Kat', 'Lula', location='bratislava', age='24', email='lulaby')
user2.describe_user()
user1.greet_user()
user2.greet_user()






