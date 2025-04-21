class Products:
    products_dict = {
        "Laptop": {"price": 1000, "available": 10},
        "Smartphone": {"price": 500, "available": 20},
        "Headphones": {"price": 50, "available": 100}
    }

    @staticmethod
    def get_products():
        # Return the dictionary of available products
        return Products.products_dict

    @staticmethod
    def update_product_quantity(product_name, quantity):
        # Update the quantity of a product in the dictionary
        if product_name in Products.products_dict:
            Products.products_dict[product_name]["available"] -= quantity
