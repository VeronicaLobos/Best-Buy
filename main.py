import sys
from products import Product
from store import Store


# setup initial stock of inventory ---------------------------
def setup_inventory():
    """
    Creates and returns a store object:
    a list containing product objects.
    """
    product_list = [ Product(name="MacBook Air M2",
                             price=1450, quantity=100),
                 Product(name="Bose QuietComfort Earbuds",
                         price=250, quantity=500),
                 Product(name="Google Pixel 7",
                         price=500, quantity=250)
               ]
    return Store(product_list)

# commands available through the user interface go here ------

def __print_total_products(my_store):
    """
    Command from the command dispatcher function:
    2. Show total amount in store

    Gets and iterates though every product object stored
    in the store object received as an argument, retrieves
    their quantity attribute and sums them.
    Prints the total amount formated as a string.
    """
    total_amount = 0
    for product in my_store.get_all_products():
        total_amount += product.get_quantity()

    print(f"Total of {total_amount} items in store")


def __print_all_products_store(my_store):
    """
    Command from the command dispatcher function:
    1. List all products in store

    Arg: my_store is a store object which contains a list of
        product objects. It has a method to return said
        product objects, and the product objects have a method
        that serializes their attributes into a string.

    Retrieves all product objects from the given store,
    formats each product's information into a string.
    Prints these strings in an ordered list.
    """
    products = my_store.get_all_products()

    ordered_list = 1
    print("------")
    for product in products:
        print(f"{ordered_list}. {product.show()}")
        ordered_list += 1
    print("------")


# commands for the user interface go here --------------------
def _command_dispatcher(user_input, my_store):
    """
    Utility command for the start function.


    Args: user_input, the key to access a value in the dict.
        my_store, given as a parameter for a function call.
    Pairs the menu options (key) with the functions
    available to the user in the CLI program (value).
    Returns a function call with a store object as
    parameter.
    """
    commands = {
        1: __print_all_products_store, # tested
        2: __print_total_products,
        3: "hi",
        4: sys.exit
        }
    return commands[user_input](my_store)


def _check_input():
    """
    Utility command for the start function.


    Asks user for input, a number between 1 and 4
    Else, will continue asking for a valid input.
    Handles errors if wrong value input or number
    out of range.
    Returns an integer.
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
    Utility command for the start function.

    Prints a menu for the buyer with the
    command options available from the user
    interface.
    """
    print("\tStore Menu\n\t----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def start(store):
    """
    Starts the self-service terminal.
    Allows users to check products, inventory,
    make and order or exit the terminal.

    Gets the store object as a parameter,
    shows the user the menu.
    Checks user input.
    Calls a function chosen by the user.
    Prints a space after a command has
    successfully run and restarts.
    """
    while True:
        _print_menu()
        user_input = _check_input()
        _command_dispatcher(user_input, store)
        print("")


def main():
    """
    Opens a store, sets inventory.
    Starts a self-service terminal.
    """
    best_buy = setup_inventory()
    start(best_buy)


if __name__ == "__main__":
    main()