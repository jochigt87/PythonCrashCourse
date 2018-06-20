#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Dream Vacation: Write a program that poll users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where
# would you go? Include a block of code that prints the results of the poll.

polling_active = True

while polling_active:
    name = input(str("What is your name: "))
    response = input(str("Which place in the world you would like to visit?" ))

    responses[name] = response
    
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False


    print("\n ---Results ---")
    for name, response in responses.items():
        print(name + " would you like to visit " + response + ".")
