#!/usr/bin/env python
# -*- coding: utf-8 -*-

prompt = "\nTell me something, and i Will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
