#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Deli: Make a list called sandwich_orders and fill it with the names of
# various sandwiches. Then makes an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich is made, move it to the list of finished
# sandwiches. After all the sandwiches have been made, print a message listing
# each sandwich that was made.

finished_sandwiches = []

sandwich_orders = ['napolitano', 'cubano', 'ham_cheese', 'vegetarian',
                   'solo_cheese', 'french']


while sandwich_orders:
    sandwiches = sandwich_orders.pop()

    print(sandwiches.title())
    finished_sandwiches.append(sandwiches)

    print("\nThe Following Sandwiches already :")
    for finished_sandwiches in sandwich_orders:
        print("I made your " + finished_sandwiches)
