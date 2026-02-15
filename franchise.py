# Franchise class
# Will contain information about the different franchises for Basta Fazoolin restaurants

# Import statement that lets this module tap into the menu module
from menu import brunch, early_bird, dinner, kids, arepas_menu


class Franchise:
    # The constructor method __init__ used to access instance attributes and methods
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    # String representation method, will communicate franchise locations and their menus
    def __repr__(self):
        return f"Franchise location: {self.address!r}."

    # This method will take in a time and return which menus are available
    def available_menus(self, time):
        available = []
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                available.append(menu)
        return available


# Next 2 variables contain our franchise locations and menus offered
flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise(
    "12 East Mulberry Street", [brunch, early_bird, dinner, kids]
)
# Added new arepas franchise
arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])
