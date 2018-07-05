#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Polling: Use the code in favorite_language.py (page 104)

# Make a list of people who should take the favorite languages poll, include
# some names that are already in the dictionary and same that are not.

# Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding. If they
# have not yet taken the poll, print a message inviting them to take the poll.

favorite_language = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

for name, languages in favorite_language.items():
    print(name.title() + "'s favorite_language " + languages.title() + ".")

programmers = ['ken','jen','guido','james','dennis','rob','phil', 'sarah']

for program in programmers:
    if program in favorite_language.keys():
        print("Thanks for you vote," + program.title())
    else:
        print(program.title() + " What's you favorite programming language?")
