#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Seeing the world:
# Think of at least five places in the world you'd like to visit:

# Store the locations in a list. Make sure the list is not in
# alphabetical order.

# Print your list in its original order. Dont worry about printing
# the list neatly. Just print it as a raw Python list.

# Use sorted() to print your list in alphabetical order without
# modifying the actual list.

# Show that you list is still in its original order by printing it.

# Use sorted() to print your list in reverse alphabetical order,
# without changing the order of the original list.

# Show that you list is still in its original order by print it again.

# Use reverse() to change the order of your list again.
# Print the list to show its back to its original order.

# Use sort() to change your list so its stored in alphabetical order
# Print the list to show that its order has been changed.

# Use sort() to change your list so it stored in reverse alphabetical
# order. Print the list to show that its order has changed.

myplaces = [
        'China', 'Indonesia', 'Japon', 'Suecia',
        'Francia', 'Ucrania', 'Rumania'
        ]
print(myplaces)

print(sorted(myplaces))

print(myplaces)

print(sorted(myplaces, reverse=True))
print(myplaces)
myplaces.sort()
print(myplaces)
myplaces.sort(reverse=True)
print(myplaces)

if not myplaces:
    print("Lista Llena")
