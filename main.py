from products import Product

# Test Products class

bose = Product(name="Bose QuietComfort Earbuds", price=250, quantity= 500)
mac = Product("MacBook Air M2", 1450, 100)
print(bose.show())
print(mac.show())

bose.buy(2)
mac.buy(100)
print(mac.is_active())
print(mac.show())

# bose.set_quantity(1000)
# bose.show()