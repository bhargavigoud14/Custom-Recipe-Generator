from ecommerce.user.register import*
from ecommerce.user.authentication import*
from ecommerce.order.order_management import*

register("bhargavi","b@gmail.com",23456544)
if auth_user("bhargavi",23456544):
    order("Laptops")

else:
    print("user doesnot exist")



