#!/usr/bin/env python
# -*- coding: utf-8 -*-

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about user."""
    profile = {}
    profile['first_name'] = first
    profile['second_name'] = last

    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                            location = 'princeton',
                            field = 'physics',
                             hobbies = 'think the time is relative!')

print(user_profile)
