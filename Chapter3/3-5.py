#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Exercice 3-5. Changing Guest List
# You just heard that one of your guests cant make the dinner,
# so you need to send out a new set of invitations. You'll have to
# think of someone else to invite.

# * Start with your program from Exercise 3-4. Add print statement
# at the end of your program stating the name of the guest who can't
# make it.

# * Modify your list, replacing the name of the guest who cant make it with,
# the name of the new person you are inviting.

# * Print a second set of invitation messages, one for each person,
# who is still in your list.

myguests = ['Ivan', 'Julio', 'Fidel']

myguests[2] = 'Manuel'

print(myguests)
