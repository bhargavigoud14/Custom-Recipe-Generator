# commerce/order/order.py

from user.authentication import UserAuthentication
from product.products import *
class Order:
    orders_dict = {}  # Class-level dictionary to store orders

    def __init__(self, email, product, quantity):
        self.order_data = {
            "email": email,
            "product": product,
            "quantity": quantity
        }

    def place_order(self):
        # Check if the user is authenticated before placing the order
        if not UserAuthentication.authenticate(self.order_data["email"]):
            return {"message": "User not authenticated. Cannot place order."}

        # Create a unique key for each order (could be email + product)
        order_key = f"{self.order_data['email']}_{self.order_data['product']}"
        
        # Check if the order already exists
        if order_key in Order.orders_dict:
            return {"message": "Order for this product already exists."}
        
        # Add the order to the orders dictionary
        Order.orders_dict[order_key] = self.order_data
        # Products.update_product_quantity(product, quantity)
        return {"message": f"Order placed for {self.order_data['quantity']} {self.order_data['product']}(s)"}
        
    @classmethod
    def get_orders(cls):
        # Return the dictionary of all orders
        return cls.orders_dict
