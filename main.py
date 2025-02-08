from products import Product
from store import Store

# Test Products class

bose = Product(name="Bose QuietComfort Earbuds", price=250, quantity= 500)
mac = Product("MacBook Air M2", 1450, 100)


my_store = Store([bose, mac])
price = my_store.order([(bose, 5), (mac, 30), (bose, 10)])
print(f"Order cost: {price} dollars.")


