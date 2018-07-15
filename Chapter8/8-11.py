#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Unchanged Magicians: Start with your work from Exercise 8-10. Call the
# function make_great() with a copy of the list of magicians' name. Because the
# original list will be unchanged, return the new list and store it in a
# separate list. Call show_magicians() with each list to show that you have one
# list of the original names and one list with the Great added to each
# magician's name.

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

