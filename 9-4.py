#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Number Served: Start with your program from Exercise 9-1 (page 166). Add an
# attribute called number_served with a default value of 0. Create an instance
# called restaurant from this class. Print the number of costumers the
# restaurant has served, and then change this value and print it again.

# Add a method called set_number_served() that let's you set the number of
# costumers that have been served. Call this method with a new number and print
# the value again.

# Add a method called increment_number_served() that lets you inscrement the
# number of costumers who've been served. Call this method with any number you
# like that could represent how many costumers were served in, say, a day
# bussines.


class Restaurant():  # We make the class Restaurant.

    # Class store two attributes.
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        # Add an attribute called number_served with a default value of 0

    def describe_restaurant(self):
        print(str(self.restaurant_name.title()))
        print(str(self.cuisine_type.title()))
        print(str(self.number_served))

    def set_number_served(self, served):
        self.number_served = served

    def open_restaurant(self):
        print(self.restaurant_name.title() + " Restaurant is Open!")

    def increment_number_served(self, served):
        self.number_served += served


my_restaurant = Restaurant('Mora', 'sea food')

my_restaurant.set_number_served(20)

my_restaurant.increment_number_served(20)

my_restaurant.describe_restaurant()
