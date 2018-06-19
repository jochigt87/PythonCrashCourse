#!/usr/bin/env python
# -*- coding: utf-8 -*-

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\nEnter 'quit' to end the program "

# active = True
while True:
    city = input(prompt)

    if city == 'quit':
        # active = False
        break
    else:
        print("I'd love to go to " + city.title() + "!")
