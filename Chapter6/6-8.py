#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Pets: Make a several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the
# answer's name. Store these dictionaries in a list called pets. Next, loop
# through your list and as you do print everything you know about each pet.

pets_list = []

pets = {
        'animal_kind': 'dog',
        'race': 'husky',
        'owner': 'jochi',
        'food': 'purina',
        }

pets_list.append(pets)

pets = {
        'animal_kind': 'dog',
        'race': 'pug',
        'owner': 'samuel',
        'food': 'dog_chow',
        }

pets_list.append(pets)

pets = {
        'animal_kind': 'dog',
        'race': 'german sheppard',
        'owner': 'richard',
        'food': 'pedigree',
        }

pets_list.append(pets)

print(pets_list)

for pets in pets_list:
    owner = pets['owner'].title()
    animal = pets['animal_kind']
    race = pets['race'] 
    eat = pets['food']

    print(owner + " have a " + animal + " his race is " + race + " and eat " + eat)

