#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Battery Upgrade: Use the final version of electric_car.py from this section.
# Add a method to the Battery class called upgrade_battery(). This method
# should check the battery size and set the capacity to 85 if it isnt already.
# Make an electric car witha default battry size, call get_range() once, and
# then call get_range() a second time after upgrading the battery. You should
# see an increase in the car's range.


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


class Battery():
    """ Check the battery"""

    def upgrade_battery(selfi, battery_size=85):
        selfi.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 30:


class ElectricCar(Car):

    """ Represents aspects of a car, specific to electric vehicules. """

    def __init__(self, make, model, year):
        """ Initialize attributes of the parent class. """
        super().__init__(make, model, year)


my_new_car = Car('audi', 'A4', 2016)

my_new_car.get_descriptive_name()
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(2890)
my_new_car.increment_odometer(2)
my_new_car.read_odometer()

micar = ElectricCar('toyota', 'TDR', 2019)
micar.get_descriptive_name()
micar.update_odometer(1200)
