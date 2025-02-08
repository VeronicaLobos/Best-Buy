from products import Product

# Test Products class

bose = Product(name="Bose QuietComfort Earbuds", price=250, quantity= 500)
mac = Product("MacBook Air M2", 1450, 100)

bose.set_quantity(100)
print(bose.show())
print(bose.is_active())
print(bose.buy(100))
print(bose.get_quantity())
print(bose.is_active())
