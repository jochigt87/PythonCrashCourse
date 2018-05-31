#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Rivers: Make a dictionary containig three major rivers and the country each
# river runs through. One key-value pair might be 'nile':'egypt'.

# Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.

# Use a loop to print the name of each river included in the dictionary.
# Use a loop to print the name of each country included in the dictionary.

rivers = {
        'Ganges': 'India',
        'Yang_Tse_Kiang': 'China',
        'Liena': 'Siberia',
        'Mississippi': 'United_States',
        'Amazona': 'South_America',
        }

for key, values in rivers.items():
    print("The " + key + " runs through " + values)
