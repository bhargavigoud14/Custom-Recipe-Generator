from ..product.inventory import products
def order(product_name):
    if product_name in products:
        stock=products[product_name]
        if stock==0:
            print("no stock")
        else:
            qty=int(input("enter quantity:"))
            if qty>=products[product_name]:
                print(f"{qty} is not available")
            else:
                print(f"order placed {product_name} for {qty}sucessfull")
                products[product_name]-=qty
                print(f"remaining {product_name} are {products[product_name]}")     
            
    else:
        print("no stock")

