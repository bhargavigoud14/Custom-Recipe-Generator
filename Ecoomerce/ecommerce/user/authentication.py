from .register import details
def auth_user(user_name,password):
    if user_name == details['username'] and password == details['password']:
        print(f"authenticated for {user_name} sucessfull")
        return True
    else:
        print(f"authentication failed for {user_name}  ")
        return False