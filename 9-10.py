#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imported Restaurant: Using your latest Restaurant class, store it in a module
# Make a separate file that imports Restaurant. Make a Restaurant instance,
# and call one of Restaurant's methods to show that the import statement is
# working properly.


from restaurante import Restaurant

my_restaurante = Restaurant('SOFIA', 'Criolla')

print(my_restaurante.describe_restaurant())
