#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Favorite Numbers: Modify your program fro Exercise 6-2(page 102) so each
# person can have more than one favorite number. Then print each person's name
# along with their favorite numbers.

favorite_numbers= {
        'jochi': [7, 19, 11],
        'raymon': [19, 4, 87],
        'ivan': [14, 12, 3],
        'jesus': [23, 2, 11],
        'manuel': [32, 31, 90]
        }


for name, numbers in favorite_numbers.items():
    print(name.title() + " favorite number is :")
    for number in numbers:
        print(str(number))
