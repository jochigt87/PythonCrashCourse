#!/usr/bin/env python
# -*- coding: utf-8 -*-

# User Profile: Start with a copy of user_profile.py from page 153. Build a
# profile of youself by calling build_profile(), using your first and last
# names and three other key-value pairs that describe you.


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['second_name'] = last

    for key, value in user_info.items():
        profile[key] = value 
    return profile


user_profile = build_profile('jochimin', 'contreras',
        location = 'Santo Domingo', field = 'Programming and Networks', age = 29)


print(user_profile)
