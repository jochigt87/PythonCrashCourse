#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Example of IF and Else Statements
'''

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
