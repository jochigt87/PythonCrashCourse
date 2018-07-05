#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sometimes you won't know ahead of time how many arguments a function needs to
# accept. Fortunately, Python allows a function to collect an arbitrary number
# of arguments from the calling statement. For example, consider a fuction that
# builds a pizza. It needs to accept a number of topping, but you can't know
# ahead of time how many topping a person will want. The function in the
# following example has one parameter, *topping, but this paramenter collects
# as many arguments as the calling line providers:

def make_pizza(*topping):
    """Summrize the pizza we are about to make."""
    print("\nMaking a pizza with the following topping:")
    for topping in topping:
        print("- " + topping)

make_pizza('peperoni', 'corn')
make_pizza('mushrooms', 'green peppers', 'extra_cheese')
