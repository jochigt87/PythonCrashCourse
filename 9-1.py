#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Restaurant: Make a class called Restaurant. The __init__() method for
# Restaurant should store two attributes: a restaurant_name and a cuisine_type
# Make a method called describe_restaurant() that prints these two pieces of
# information, and a method called open_restaurant() that print a message
# indicating that the restaurant is open.

# Make an instance called restaurant from your class. Print the two attributes
# individually, and then call both methods.


class Restaurant():  # We make the class Restaurant.

    # Class store two attributes.
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())

    def open_restaurant(self):
        print(self.restaurant_name.title() + " Restaurant is Open!")


restaurant = Restaurant('Delicias', 'sea food')

print(restaurant.describe_restaurant())
print(restaurant.open_restaurant())
