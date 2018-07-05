#!/usr/bin/env python
# -*- coding: utf-8 -*-

def build_person(first_name, last_name):
    """ Return a dictionary of information about a person """
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jochi', 'contreras')
print(musician)
