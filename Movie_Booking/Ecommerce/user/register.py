class UserRegister:
    users_dict = {}  # Class-level dictionary to store multiple users

    def __init__(self, name, email):
        # Store individual user details in a dictionary
        self.user_data = {"name": name, "email": email}

    def register(self):
        # Add the user to the class-level users_dict using email as the key
        UserRegister.users_dict[self.user_data['email']] = self.user_data
        return self.user_data

    @staticmethod
    def get_all_users():
        # Return the dictionary of all registered users
        return UserRegister.users_dict
