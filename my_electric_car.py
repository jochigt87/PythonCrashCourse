#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#from car import Car, ElectricCar

#my_tesla = ElectricCar('Tesla','S',2015)

# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()

#carro = Car('Nissan','GTR',2018)
# print(carro.get_descriptive_name())

import car

nuevo_car = car.Car('Subaru', 'WRX', 2017)

print(nuevo_car.get_descriptive_name())


carroElectrico = car.ElectricCar('GUAZHOU', 'Chicken Limited', 2018)

print(carroElectrico.get_descriptive_name())
carroElectrico.get_descriptive_name()
carroElectrico.battery.get_range()
