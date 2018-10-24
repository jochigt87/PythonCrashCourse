#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Three Restaurants: Start with your class from Exercise 9-1. Create three
# different instances from the class, and call describe_restaurant() for each
# instances.


class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())


myrestaurant = Restaurant('don camaron', 'sea food')
myrestaurant2 = Restaurant('el rincon', 'typical')
myrestaurant3 = Restaurant('azadero', 'porcina')


myrestaurant.describe_restaurant()
myrestaurant2.describe_restaurant()
myrestaurant3.describe_restaurant()
