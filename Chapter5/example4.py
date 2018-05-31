#!/usr/bin/env python
# -*- coding: utf-8 -*-

banned_users = ['Maria', 'andrew', 'carolina', 'david']
user = 'maria'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")
else:
    print(user.title() + ", Sorry you can't post a response")

