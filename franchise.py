# Franchise class
# Will contain information about the different franchises for Basta Fazoolin restaurants

# Import statement that lets this module tap into the menu module
from menu import brunch, early_bird, dinner, kids


class Franchise:
    # The constructor method __init__ used to access instance attributes and methods
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    # String representation method, will communicate franchise locations and their menus
    def __repr__(self):
        return f"Welcome to the Basta Fazoolin located at {self.address!r}. \n"


# Next 2 variables contain our franchise locations and menus offered
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise(
    "12 East Mulberry Street", [brunch, early_bird, dinner, kids]
)

# Testing the string representation method
print(flagship_store)
