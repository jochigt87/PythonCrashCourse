#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python3'
favorite_languages['sarah'] = 'C'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python2.7'
favorite_languages['luis'] = 'Go'

for name, languages in favorite_languages.items():
    print(name.title() + "'s favorite laguages is " + languages.title() + ".")
