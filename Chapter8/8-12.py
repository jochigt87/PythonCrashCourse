#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Sandwiches: Write a function that accepts a list of items a person wants on a
# sandwich. The function should have one parameter that collects as many items
# as the function call provides, and it should print a summary of the sandwich
# that is being ordered. Call the function three times, using a diferrent
# number of arguments each time.

def sandwichMaker(*sandwiches):
    print("Making great and delecious sandwiches for you")
    for sandwich in sandwiches:
        print("Adding " + sandwich + " to your sandwich")
    print("sandwich is ready to eat :-)")

sandwichMaker('1 lead cheese', '1 eggs', 'beef')

