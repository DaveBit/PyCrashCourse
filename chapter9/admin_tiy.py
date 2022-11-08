from users_tiy import User


class Admin(User):
    def __init__(self, first_name, last_name, **others):
        super().__init__(first_name, last_name, **others)
        self.privileges = ["can add post", "can delete post", "can ban user",
                           "can unban user"]

    def show_privileges(self):
        print("\nAdmin's privileges: ")
        for privilege in self.privileges:
            print("- " + privilege)


admin1 = Admin("Dave", "Bit", location='UK', email='lulaby@hotmail', username='matroska')
admin1.greet_user()
admin1.describe_user()
admin1.show_privileges()
