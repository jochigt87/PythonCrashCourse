#!/usr/bin/env python
# -*- coding: utf-8 -*-

# City Names: Write a function called city_country() that takes in the name of
# a city and its country. The function should return a string formatted like
# this.
#
# ________________________________________________________________________________
# "Santiago, Chile"
# ________________________________________________________________________________
#
# Call your function with at least three city-country pairs, and print the
# value that's returned.

def city_country(city, country):
    full = "______________________\n" + city+"," + country + "\n______________________"
    return full.title()

pais = city_country('Santiago', 'chile')
print(pais)
