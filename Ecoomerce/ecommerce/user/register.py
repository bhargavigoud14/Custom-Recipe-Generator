details={}
def register(user_name,email,password):
    print(f"Registring {user_name} and {email}")
    details['username']=user_name
    details['email']=email
    details['password']=password
    return details
    

