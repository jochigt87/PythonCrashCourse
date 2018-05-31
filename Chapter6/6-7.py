#!/usr/bin/env python
# -*- coding: utf-8 -*-

# People: Start with the program you wrote for Exercise 6-1 (page 102). Make
# two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As
# you loop through the list, print everything you know about each person.
people = []

persons = {
        'first_name': 'Jochimin',
        'last_name':'Contreras',
        'age':'29',
        'city':'Santo Domingo',
        }

people.append(persons)

persons = {
        'first_name': 'Mike',
        'last_name':'Henriquez',
        'age':'24',
        'city':'Santo Domingo',
        }

people.append(persons)

persons = {
        'first_name': 'Jesus',
        'last_name':'Marti',
        'age':'25',
        'city':'Santo Domingo',
        }

people.append(persons)

for persons in people:
    name = persons['first_name'].title() + " " + persons['last_name'].title()
    age = str(persons['age'])
    city = persons['city']

    print(name + " from " + city +" "+ age +" years old" )
