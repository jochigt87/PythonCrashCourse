#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you
# wrote in Exercice 9-1 (page 166) or Exercice 9-4 (page 171). Either version
# of the class will work; just pick the one you like better. Add an attribute
# called flavors that stores a list of ice cream flavors. Write a method that
# displays these flavors. Create an instance of IceCreamStand, and call this
# method.


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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = [
            'chocolate',
            'vainilla',
            'fresa',
            'bachata_mix',
            'ron_pasas',
        ]

    def displays_flavors(self):
        for sabores in self.flavors:
            print("Los sabores son: " + str(sabores))


mi_local = IceCreamStand('Frozen', 'Ice Cream')
mi_local.describe_restaurant()
mi_local.displays_flavors()
