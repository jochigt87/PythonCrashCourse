#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name 
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting")

    def roll(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() + " rolled over!")


""" Making an Instance from a Class """
my_dog_1 = Dog('chivi', 12)

print("My Dog name's is " + my_dog_1.name.title() + ".")
print("My Dog is " + str(my_dog_1.age) + " years old")

