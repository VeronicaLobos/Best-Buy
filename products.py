
class Product:
     def __init__(self, name:str, price:float, quantity:int):
          """
          Creates the instance variables (active is set to True).
          If something is invalid (empty name / negative price or quantity), raises an exception.
          """
          self.name = name
          self.price = price
          self.quantity = quantity
          self.active:bool = True

     def get_quantity(self) -> float:
          """
          Getter function for quantity.
          Returns the quantity (float).
          """
          pass

     def set_quantity(self, quantity):
          """
          Setter function for quantity.
          If quantity reaches 0, deactivates the product.
          """
          pass

     def is_active(self) -> bool:
          """
          Getter function for active.
          Returns True if the product is active, otherwise False.
          """
          pass

     def activate(self):
          """
          Activates the product.
          """
          pass

     def deactivate(self):
          """
          Deactivates the product.
          """
          pass

     def show(self) -> str:
          """
          Returns a string that represents the product, for example:
          "MacBook Air M2, Price: 1450, Quantity: 100"
          """
          pass

     def buy(self, quantity) -> float:
          """
          Buys a given quantity of the product.
          Returns the total price (float) of the purchase.
          Updates the quantity of the product.
          In case of a problem (when? think about it), raises an Exception.
          """
          pass