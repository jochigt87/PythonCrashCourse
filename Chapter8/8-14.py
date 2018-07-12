#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Cars: Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name. It should
# then accept an arbitrary number of keyword arguments. Call the function with
# the required information and two other name-value pairs, such as a color or
# an optional feature. Your function should work for a call like this one.
#
# car = make_car('subaru', 'outback', color = 'blue', tow_packages=True)
#
# Print the dictionary that's returned to make sure all the infomation was
# stored correctly.


def make_car(manufacturer, model, **extra):
    car = {}
    car['marca'] = manufacturer
    car['model'] = model

    for key, value in extra.items():
        car[key] = value 
    return car 

mycar1 = make_car('honda', 'type R', color = 'Grey', doors = '4')

print(mycar1)
