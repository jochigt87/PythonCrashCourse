#!/usr/bin/env python
# -*- coding: utf-8 -*-

# No Pastrami: Using the list sandwich_orders from Exercesi 7-8, make sure the
# sandwich 'pastrami' appears in the list at least three times. Add code near
# the begginig of your program to print a message saying the deli has run out
# of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in
# finished_sandwiches.

sandwich_orders = ['napolitano', 'pastrami', 'cubano', 'ham_cheese', 'pastrami', 'vegetarian',
                   'solo_cheese', 'french', 'pastrami']

finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    sandwiches = sandwich_orders.pop()
    finished_sandwiches.append(sandwiches)

    for finished_sandwiches in sandwich_orders:
        print(finished_sandwiches)
