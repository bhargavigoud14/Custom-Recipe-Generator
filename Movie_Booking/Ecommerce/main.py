# main.py

from user.register import UserRegister
from user.authentication import UserAuthentication
from order.order import Order
from product.products import *

# Function to register a user
def register_user(name, email):
    if UserAuthentication.check_user_exists(email):
        print("User already exists.")
    else:
        user = UserRegister(name, email)
        if user.register():
            print("User registered successfully:", user.user_data)
        else:
            print("Failed to register user.")

# Step 1: Register multiple users
register_user("John Doe", "johndoe@example.com")
register_user("Jane Smith", "janesmith@example.com")
register_user("John Doe", "johndoe@example.com")  # Attempt to register the same user again
register_user("John Doe", "johndoe1@example.com") 
# Step 2: Display all registered users (in dictionary form)
# print("Registered Users:", UserRegister.get_all_users())

# Step 3: Place orders for the users
# User 1 places an order for a Laptop
order1 = Order("johndoe@example.com", "Laptop", 2)
print(order1.place_order())


# User 2 places an order for a Smartphone
order2 = Order("janesmith@example.com", "Smartphone", 1)
print(order2.place_order())

order3 = Order("johndoe1@example.com", "Laptop", 9)
print(order3.place_order())

# Step 4: Display all orders (stored as a dictionary)
# print("Orders:", Order.get_orders())
