#!/usr/bin/env python
# -*- coding: utf-8 -*-

def make_pizza(*topping):
    """Print the list of topping that have been resquested."""
    print(topping)

make_pizza('peperoni')
make_pizza('mushrooms', 'green peppers', 'extra_cheese')

