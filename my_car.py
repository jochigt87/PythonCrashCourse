#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from car import Car

my_new_car = Car('Honda', 'Type-R', 2018)

print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 60

my_new_car.read_odometer()
