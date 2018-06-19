#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pizza Topping: Write a loop that prompts the user to enter a series of pizza
# topping until they enter a 'quit' value. As they enter each topping, print a
# message saying you'll add that topping to their pizza.

title = "Insert you favorite topping:"
title2 = "\nType quit for exit!\n"

while True:
    menu = input(title + title2)
    
    if menu.lower() == 'quit':
        break
    else:
        print(menu.title() + " You'll add that topping to their pizza!.")
