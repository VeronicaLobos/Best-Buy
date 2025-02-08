from products import Product
from store import Store


# setup initial stock of inventory
product_list = [ Product(name="MacBook Air M2", price=1450, quantity=100),
                 Product(name="Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product(name="Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)


# user interface will go here
def start():
    """
    Prints a menu for the user/buyer.
    """
    print("\tStore Menu\n\t----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")

def main():
    start()

if __name__ == "__main__":
    main()