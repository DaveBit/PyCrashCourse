class User:
    def __init__(self, first_name, last_name, **others):
        self.user_profile = {
            'first_name': first_name,
            'last_name': last_name,
            'login_attempts': 0,
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

    def increment_login_attempts(self):
        self.user_profile['login_attempts'] += 1

    def reset_login_attempts(self):
        self.user_profile['login_attempts'] = 0


user1 = User('Dave', 'bit', location='valencia', username='matroska', email='davedestroyer')
user1.describe_user()
user2 = User('Kat', 'Lula', location='bratislava', age='24', email='lulaby')
user2.describe_user()
user1.greet_user()
user2.greet_user()

for login in range(10):
    user1.increment_login_attempts()
    print("User1 login attempts at: " + str(user1.user_profile['login_attempts']))

print("User1 login attempts resetting...")
user1.reset_login_attempts()
print("User1 login attempts: " + str(user1.user_profile['login_attempts']))


