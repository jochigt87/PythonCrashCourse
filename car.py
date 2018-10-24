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


class Battery():
    """ A simple attemp to model a battery for an electric car. """

    def __init__(self, battery_size=70):
        """ Initialize the battery's attributes """
        self.battery_size = battery_size

    def describe_battery(self):
        """ Print a statement describing the battery size. """
        print("This car has a " + str(self.battery_size) + "kwh battery.")

    def get_range(self):
        """ Print a statement about the range this battery provides. """
        if self.battery_size == 70:
            range1 = 240
        elif self.battery_size == 85:
            range1 = 270

        message = "This car can go approximately " + str(range1)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):
    """ Models aspects of a car, specific to a electric car. """

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then Initialize attributes specific to an electric car.
        """

        super().__init__(make, model, year)
        self.battery = Battery()
