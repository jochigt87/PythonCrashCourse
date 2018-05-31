#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Buffet:

# *A buffet-style restaurant offers only five basic foods. think of
#  five simple foods, and store them in a tuple.

# Use a for loop to print each food the restaurant offers.

# Try to modify one of the items, and make sure that Python rejects the change.

# The restaurant changes its menu, replacing two of the items with different foods.
# Add a block of code that rewrite the tuple, and then use a for loop to print
# each of the items on the revised menu.

menu = ('rice and beans', 'beefs', 'chicken cheese', 'steak')

print("Menu: \n")
for food in menu:
    print(food)
print()
menu = ('rice', 'chicken cheese', 'steak')

for food_menu in menu:
    print(food_menu)


