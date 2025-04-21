# commerce/user/authentication.py

from user.register import UserRegister

class UserAuthentication:
    @staticmethod
    def check_user_exists(email):
        # Check if the user's email exists in the users_dict
        return email in UserRegister.users_dict

    @staticmethod
    def authenticate(email):
        # Authenticate user by checking if the user exists
        return UserAuthentication.check_user_exists(email)
