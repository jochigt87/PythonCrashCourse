#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Exercice 3-6. More Guests
# You just found a bigger dinner table, so now more space available
# Think of three more guests to invite to dinner.

# * Start with program from exercise 3-4 or Exercise 3-5.
# Add a print statement to the end of your program informing people
# that you found a bigger dinner table.

# * Use insert() to add one new guest to the beggining of your list.
# * Use insert() to add one new guest to the middle of your list.
# * User append() to add one new guest to the end of your list.
# * Print a new set of invitation messages, one for each person in
# you list.

myguests = ['Manuel', 'Fidel', 'Ivan', 'Julio', 'Raymon']

myguests.insert(0, "Carlos")
myguests.insert(3, "Francisco")
myguests.append("Mike")

print("Personas invitadas:")
for i, x  in enumerate(myguests):
    print(i+1, x)

print("He encontrado una mesa mas grande para ustedes, Los esperamos.")
