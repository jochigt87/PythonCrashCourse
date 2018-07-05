#!/usr/bin/env python
# -*- coding: utf-8 -*-

def greet_users(names):
    """ Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello " + name.title() + "!"
        print(msg)

usernames = ['harry', 'mike', 'margot']
greet_users(usernames)
