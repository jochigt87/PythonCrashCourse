#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Movie Tickets: A movie theater charges different ticket prices depending on a
# person's age. If a person is under the age of 3, the ticket is free; if they
# are between 3 and 12, the ticket is $10; and if they are over age 12, the
# ticket is $15. Write a loop in which you ask users their age, and then tell
# them the cost of their movie ticket.

promt = "\nInsert you age: "
promt += "\n(Type '0' if you want exit. ) "

active = True
while active:
    message = input(promt)
    age = int(message)
    if age == 0:
        break
    elif age <= 3:
        print("You Ticket is FREE ;-)")
    elif age >= 3 and age <= 12:
        print("You Ticket price is $10. ")
    elif age >= 12:
        print("You Ticket price is $15. ")
