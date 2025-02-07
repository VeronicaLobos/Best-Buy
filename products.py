
class Product:
     def __init__(self, name:str, price:float, quantity:int):
          """
          Creates the instance variables (active is set to True).
          If something is invalid (empty name / negative price or
          quantity), raises an exception.
          The 'active' attribute is boolean and reflects product
          availability. It is dinamically set during object
          instantiation.
          """

          # Error handling

          if not isinstance(name, str):
               raise TypeError("Name must be a string")
          if not name:
               raise ValueError("Name must contain characters")

          if not isinstance(price, (int, float)):
               raise TypeError("Price must be a number")
          if price < 0:
               raise ValueError("Price must be higher than 0")

          if not isinstance(quantity, int):
               raise TypeError("Quantity must be an integer")
          if quantity < 0:
               raise ValueError("Quantity must be 0 or higher")

          # Attributes

          self.name = name
          self.price = price
          self.quantity = quantity
          self.active:bool = quantity > 0


     def get_quantity(self) -> float:
          """
          Getter function for quantity.
          Returns the quantity (float).
          """
          return self.quantity


     def set_quantity(self, quantity) -> int:
          """
          Setter function for quantity.
          If quantity reaches 0, deactivates the product.
          Prints a message informing the user of the availability
          of the product.
          """
          try:
               self.quantity: int = quantity
               if self.is_active():
                    self.activate()
               else:
                    self.deactivate()
          except:
               if not isinstance(quantity, int):
                    raise TypeError("Quantity must be an number")
               if quantity < 0:
                    raise ValueError("Quantity must be 0 or higher")
          finally:
               if self.is_active == True:
                    print(f"Product currently available, {self.quantity} units left.")
               else:
                    print("Product currently unavailable.")


     def is_active(self) -> bool:
          """
          Getter function for active.
          Returns True if the product is active, otherwise False.
          """
          return self.active


     def activate(self):
          """
          Activates the product.
          """
          self.active: bool = True


     def deactivate(self):
          """
          Deactivates the product.
          """
          self.active: bool = False


     def show(self) -> str:
          """
          Returns a string that represents the product, for example:
          "MacBook Air M2, Price: 1450, Quantity: 100"
          """
          return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"


     def buy(self, quantity) -> float:
          """
          Buys a given quantity of the product.
          Returns the total price (float) of the purchase.
          Updates the quantity of the product.
          In case of a problem (when? think about it), raises an Exception.
          """
          if not isinstance(quantity, (int, float)):
               raise TypeError("Quantity must be a number")
          if quantity < 0:
               raise ValueError("Please introduce at least one unit to buy")

          total_price = quantity * self.price

          try:
               if self.quantity >= quantity:
                    print(f"** The total is {total_price}€ for {quantity} units.")
                    self.quantity -= quantity
               else:
                    print("Not enough product in store.")
          except Exception as e:
               print("Error: ", e)
          finally:
               print("Updating available product units:")
               #### complete here
               print(self.show())
