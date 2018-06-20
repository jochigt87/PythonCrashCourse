#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Favorite Book: Write a function called favorite_book() that accepts one
# parameter, title. The function should print a message, such as One of my
# favorite books is Alice is Wonderland. Call the function, making sure to
# include a book title as an argument in the function call.

def favorite_book(book):
    print("One of my favorite books is " + book.title())

favorite_book('Da Vinci Code')
