#!/usr/bin/env python
# -*- coding: utf-8 -*-

pets = ['dog', 'cat', 'goldfish', 'rabbit', 'cat', 'lion', 'zebra', 'cat']

print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
