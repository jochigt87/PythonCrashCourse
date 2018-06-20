#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Cities: Make a dictionary called cities. use the names of three cities as
# keys in your dicitionary. Create a dicitionary of information about each city
# and include the country that the city is in, its approximate population, and
# one fact about that city. The keys for each city's dictionary should be
# something like country, population, and fact. Print the name of each city and
# of the information you have stored about it.


cities = {
        'santo domingo': {
            'country': 'dominican republic',
            'population': 4000000,
            'fact': 'La ciudad se construyo originalmente en el margen
            oriental.',
            }
        {'san juan': {
            'country': 'puerto rican',
            'population': 2500000,
            'fact': 'La ciudad amurallda es hogar de cafes, galeria de arte,
            museos, hogares maravillosamente restaurados y tiendas unicas',
            }
            {'cuba': {
                'country': 'la habana',
                'population': 3000000,
                'fact': 'Ciudad natal del poeta y escritor modernista Jose
                Marti',
                }
            }
            }
        }
for key, values in cities.items():
    print(key)
