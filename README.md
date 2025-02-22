### My first OOP practice with Python

This is the first part of a project to learn how to create classes, and to help me understand basic OOP with Python.

#### Instalation

Clone this repository and run main *duh*

#### What does this button do?

Best Buy (this program) is a CLI that simulates a self-checkout TPV.
A store object is generated along with product objects when the program runs (hard coded).
The user interface prints a menu of actions available in a command dispatcher.
Users can check inventory from a store class object, which contains product class objects.
Users can check the total amount of units across all products in the store.
Users can order: grand total is shown and product quantity is updated.


##### Making nice code:

+ Type Hinting: Improved code readability, it will facilitate static analysis.
+ Docstrings: Explaining the purpose of each class, and the behaviour of each method, will improve maintainability.
+ Error Handling: Type checking, empty strings and negative values will cause errors when running the program.
+ Exception messages: Each error will raise different error messages, making debugging easier and to guide the user during interaction.

* Product class dynamic attribute: The instantiation will contain an "active" (bool) attribute, which will be initialized as True if the "quantity" (int) attribute is higher than zero, otherwise its value will be set to False.