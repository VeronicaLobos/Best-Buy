import sys
from products import Product
from store import Store


# setup initial stock of inventory
product_list = [ Product(name="MacBook Air M2", price=1450, quantity=100),
                 Product(name="Bose QuietComfort Earbuds", price=250, quantity=500),
                 Product(name="Google Pixel 7", price=500, quantity=250)
               ]
best_buy = Store(product_list)

# user interface will go here

def _show_all_products_store(my_store):
    """

    """
    products = my_store.get_all_products()

    ordered_list = 1
    print("------")
    for product in products:
        print(f"{ordered_list}. {product.show()}")
        ordered_list += 1
    print("------")
    print("")


def _command_dispatcher(user_input, my_store):
    """
    Pairs the menu options (key) with the functions
    available to the user in the CLI program (value).
    Returns a function call.
    ...
    """
    commands = {
        1: _show_all_products_store,
        2: "hi",
        3: "hi",
        4: sys.exit
        }
    return commands[user_input](my_store)

def _check_input():
    """
    Asks user for input, a number between 0 and 10
    Else, will continue asking for a valid input
    Returns an integer
    """
    while True:
        try:
            user_input = int(input("Please choose a number: "))
            assert 1 <= user_input <= 4
            return user_input
        except AssertionError:
            return
        except ValueError:
            print("Error with your choice! Try again!")
            return


def _print_menu():
    """
    Prints a menu for the user/buyer.
    """
    print("\tStore Menu\n\t----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def start(my_store):
    """
    Gets the store object as a parameter,
    shows the user the menu.
    Checks user input.

    """
    while True:
        _print_menu()
        user_input = _check_input()
        _command_dispatcher(user_input, best_buy)


def main():
    start(best_buy)


if __name__ == "__main__":
    main()