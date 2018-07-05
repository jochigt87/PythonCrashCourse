#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Great Magicians: Start with a copy of your program from Exercise 8-9. Write a
# function called make_great() that modifies the list of magicians by adding
# the phrase the Great to each magicians's name. Call show_magicians() to see
# that the list has actually been modified.

def make_great(magicians_names, unamed_magicians):
    
    
    
    while unamed_magicians:
        names_now = magicians_names.pop()

    print("Names of magicians" + names_now)
    unamed_magicians.append(names_now)

#    for names in magicians_names:
#       print("Great " + names)

def show_magicians(magicians_names):
    
    for names_now in magicians_names:
        print(names_now)

magicians_names = ['joudini', 'chespin', 'gasparin', 'nestarin']
unamed_magicians = []

make_great(magicians_names[:], unamed_magicians)

show_magicians(magicians_names)
