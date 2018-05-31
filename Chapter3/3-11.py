#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Intentional Error:
# if you haven't received an index error in one of your programs yet,
# try to make one happen. Change an index in one of your programs to
# produce an index error. Make sure you correct the error before
# closing the program.

mycities = ['Santo Domingo', 'Neyba', 'Santiago', 'Higuey']

try:
    print(mycities[4])
except: IndexError
print("Su indice esta fuera de rango no puede ser mayor a:",len(mycities)-1)


