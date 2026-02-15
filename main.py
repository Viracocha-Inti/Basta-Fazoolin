# Project: Basta Fazoolin
# Author: Samir Valencia
# A Python project demonstrating object-oriented programming concepts

# Import statements that lets this module tap into the other module
from menu import brunch, early_bird, dinner, kids, arepas_menu
from franchise import flagship_store, new_installment, arepas_place
from business import business_one, business_two

# Testing menu.py class/methods
print(brunch)
# These variables were used for testing the calculate bill method
breakfast_order = ("pancakes", "home fries", "coffee")
print("Total brunch order: ", brunch.calculate_bill(breakfast_order))
early_bird_order = ("salumeria plate", "mushroom ravioli (vegan)")
print("Total early bird order: ", early_bird.calculate_bill(early_bird_order))

# Testing franchise.py class/methods
print(flagship_store)
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))

# Testing business.py class/methods
print(business_one)
print(business_two)
