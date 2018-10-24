#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Car():
    """ A simple attemp to represent a car """

    def __init__(self, make, model, year):
        """ Initialize attributes to describe a car """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 12  # Setting a Default value for an attribute

    def get_descriptive_name(self):
        """ Return a neatly formatted descriptive name """
        long_name = str(self.year) + ' ' + self.make + '  ' + self.model
        return long_name.title()

    def read_odometer(self):
        """ Print a statement showing the car's mileage. """
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """ Set the odometer reading to the given value """
        #self.odometer_reading = mileage

        """ Set the odometer reading to the given value.
            Reject the change if it attemps to roll the odometer back  """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """ Add the given amount to the odometer reading.! """
        self.odometer_reading += miles


class ElectricCar(Car):

    """ Represents aspects of a car, specific to electric vehicules. """

    def __init__(self, make, model, year):
        """ Initialize attributes of the parent class. """
        super()


my_new_car = Car('audi', 'A4', 2016)

my_new_car.get_descriptive_name()
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(2890)
my_new_car.increment_odometer(2)
my_new_car.read_odometer()

micar = ElectricCar('toyota', 'TDR', 2019)
micar.get_descriptive_name()
micar.update_odometer(1200)
