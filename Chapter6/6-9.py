#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite
# places for each person. To make this exercise a bit more interesting, ask
# some friends to name a few of their favorite places. Loop through the
# dictionary, and print each person's name and their favorite places.

favorite_places = {
        'luis': ['grand canon', 'Duarte','pico duarte'],
        'jochi': ['petronas tower'],
        'fidel': ['santa cruz', 'lago enriquillo'],
        'michael': ['river titicaca', 'la pelona', 'samana']
        }

for name, places in favorite_places.items():
    print(name.title() + " favorite places :" )
    for place in places:
        print("\t" + place.title())
