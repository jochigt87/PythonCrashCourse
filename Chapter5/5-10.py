#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Checking Usernames: Do the folowing to create a program that simulates how
# websites ensure that everyone has a unique username.

# *Make a list of five or more usernames called (current_users).

# *Make another list of five usernames called new_users. Make sure one or two
# of new usernames are also in the (current_users) list.

# *Loop through the new_users list to see if each new username has already been
# used. If it has, print a message that the person will need to enter a new
# username. If a username has not been used, print a message saying that the
# username is avaliable.

# *Make sure your comparison is case insensitive. is 'John' has been used,
# 'JOHN' shuold not be accepted.

current_users = ['onix', 'Firebase', 'Jadoop', 'ADMIN', 'pycoder', 'jochigt']
new_users = ['admin']

for user in current_users:
    if user.lower() in new_users:
        print(user, "This User is not avaliable.")
    else:
        print(user, "This user is avaliable")
