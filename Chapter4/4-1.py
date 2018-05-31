#!/usr/bin/env python
# -*- coding: utf-8 -*-i

# Pizzas:
# Think of at least three kinds of you favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name
# of each pizza.

# * Modify your for loop to print a sentece using the name of pizza
# instead of printing just the name of the pizza. For each pizza you
# should have one line of output containing a simple statement like
# like I like pepperoni piza.

# * Add a line at the end of your program, outside the for loop, that
# states how much you like pizza. The output should consist of three
# or more lines about the kinds of pizza you like and then an
# additional sentence, such as I Really like pizza.

favorite_pizza = [
        'pepperoni',
        'jamon y queso',
        'vegetales',
        'salchicha_italiana']

# print(favorite_pizza)

for pizza in favorite_pizza:
    print("I like", pizza, "pizza")
print("I Really like ", favorite_pizza[0], 'pizza')
print("I Really like ", favorite_pizza[1], 'pizza')
