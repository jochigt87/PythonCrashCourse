#!/usr/bin/env python
# -*- coding: utf-8 -*-

# More Conditional Tests:
# You don't have to limit the number of tests you create to 10. If you want to
# try more comparisions, write more tests and add them to conditional_tests.py.
# Have at least one True and one False result for each of following:

#* Tests for equality and inequality with strings
#* Tests using lower() function
#* Numerical tests involving equality and inequality, greater than and less
# than, greater than or equal to, and less than or equal to

#* Test using the (and) keyword and the (or) keyword.

#* Test whether an item is in a list.

#* Test whether an item is not in a list.


# Equality and Inequality with strings
name = 'Jochimin'
print(name == 'jochimin')

name2 = 'Fidel'
print(name2.lower() == 'fidel')
print()

# Numerical keyword AND and OR
a = 10
b = 4

print(a > b)
print(b>a)
print(a == a and a > b)
print(b < a or a > b)

users = ['juan', 'pedro', 'mike']
user = 'juan'
user2 = 'Michael'

for userx in users:
    if userx == user:
        print(user, "Esta en la lista")

if user2 not in users:
    print(user2, "No esta en la lista")
