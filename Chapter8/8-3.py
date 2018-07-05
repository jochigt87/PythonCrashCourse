#!/usr/bin/env python
# -*- coding: utf-8 -*-

# T-Shirt: Write a function called make_shirt() that accepts a size and the
# text of a message thata should be printed on the shirt. The function should
# print a sentence summarizing the size of the shirt and the message printed on
# it. Call the function once using positional arguments to make a shirt. Call
# the function a second time using keyword arguments.


def make_shirt(size, text_on_shirt):
    
    """Display a message of size of t-shirt and text on shirt"""
    print("The size is: " + size + "\n" + text_on_shirt)
 
make_shirt('small', 'Working on Python')
