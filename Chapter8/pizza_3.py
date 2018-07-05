#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Mixing positional and Arbitrary Arguments

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) + 
          "-inch pizza with the following topping:")
    for topping in toppings:
        print("- " + topping)

make_pizza(3, 'peperoni')
make_pizza(23, 'mushrooms', 'green peppers', 'extra_cheese')

