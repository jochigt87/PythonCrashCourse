#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Hello Admin:
# Make a list of five or more usernames, including the name 'admin'. Imagine
# you are writing code that will print a greeting to teach user after they log
# in to a website. Loop through the list, and print a greeting to each user:

# *If the username is 'admin', print a special greeting, such as Hello admin,
# would you like to see a status report?

# *Otherwise, print a generic greeting, such as Hello Eric, thank you for
# logging in again.


usernames = ['onix', 'firebase', 'hadoop', 'admin', 'pycoder', 'jochigt']

for user in usernames:
    if user in usernames:
        print("Hello", user, "thank you for logging")
    if 'admin' in user:
        print("Hello ADMIN")
