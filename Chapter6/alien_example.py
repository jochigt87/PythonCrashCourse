#!/usr/bin/env python
# -*- coding: utf-8 -*-


# velocidad = raw_input("Choose the speed: slow, medium, fast")

#alien_0['speed'] = str()
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print("Original x-position: " + str(alien_0['x_position']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed.

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3
else:
    # The Light_Speed :-)
    x_increment = 5
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

    
