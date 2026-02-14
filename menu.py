# Main Menu class
# Menus found in the Basta Fazoolin franchises as well as their times of service
class Menu:
    # The constructor method __init__ used to access instance attributes and methods
    def __init__(self, name, items, start_time, end_time):
        self.name = name  # Next 4 rows initialize the attributes
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    # String representation method, will communicate menu and times
    def __repr__(self):
        return (
            f"Welcome to Basta Fazoolin. \n"
            f"The {self.name!r} menu will be available from {self.start_time!r}00 to {self.end_time!r}00. \n"
            f"Please take your time and enjoy your complimentary breadsticks"
        )

    # This method will add up the prizes of all the items that were purchased and return the total amount
    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in purchased_items:
            if purchased_item in self.items:
                bill += self.items[purchased_item]
        return bill


# Next 4 categories contain the 4 menus that can be found in the restaurant 'Basta Fazooli'
brunch = Menu(
    "brunch",
    {
        "pancakes": 7.50,
        "waffles": 9.00,
        "burger": 11.00,
        "home fries": 4.50,
        "coffee": 1.50,
        "espresso": 3.00,
        "tea": 1.00,
        "mimosa": 10.50,
        "orange juice": 3.50,
    },
    11,
    16,
)
early_bird = Menu(
    "early bird",
    {
        "salumeria plate": 8.00,
        "salad and breadsticks (serves 2, no refills)": 14.00,
        "pizza with quattro formaggi": 9.00,
        "duck ragu": 17.50,
        "mushroom ravioli (vegan)": 13.50,
        "coffee": 1.50,
        "espresso": 3.00,
    },
    15,
    18,
)
dinner = Menu(
    "dinner",
    {
        "crostini with eggplant caponata": 13.00,
        "caesar salad": 16.00,
        "pizza with quattro formaggi": 11.00,
        "duck ragu": 19.50,
        "mushroom ravioli (vegan)": 13.50,
        "coffee": 2.00,
        "espresso": 3.00,
    },
    17,
    23,
)
kids = Menu(
    "kids",
    {
        "chicken nuggets": 6.50,
        "fusilli with wild mushrooms": 12.00,
        "apple juice": 3.00,
    },
    11,
    21,
)
