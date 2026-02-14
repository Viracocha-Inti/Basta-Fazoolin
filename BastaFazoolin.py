# Project: Basta Fazoolin
# Author: Samir Valencia
# A Python project demonstrating object-oriented programming concepts

# Import statement that lets this module tap into the menu module
from menu import brunch, early_bird, dinner, kids

# Testing that the menu was imported properly and that the methods work.
print(brunch)

# These variables were used for testing the calculate bill method
breakfast_order = ("pancakes", "home fries", "coffee")
print("Total brunch order: ", brunch.calculate_bill(breakfast_order))
early_bird_order = ("salumeria plate", "mushroom ravioli (vegan)")
print("Total early bird order: ", early_bird.calculate_bill(early_bird_order))
