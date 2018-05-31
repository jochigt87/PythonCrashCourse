#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Multiple of Ten: Ask the user for a number, and then report whether the
# number is a multiple of 10 or not.

number = input("Insert a number: ")
number = int(number)

if number % 10 == 0:
    print("Its multiple of ten")
else:
    print("Its not multiple of ten")

