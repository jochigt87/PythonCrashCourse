#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Exercice 3-7. Shrinking List
# You just found out that your new dinner table wont arrive in time
# for the dinner, and you have space for only two guests.

# * Start with your program from Exercise 3-6. Add a new line that
# print a message saying that you can invite only two people for
# dinner.

# * Use pop() to remove guests from your list ine at a time until
# only two names remain in your list.
# Each time you pop a name from your list, print a message to that
# person letting them know you're sorry you cant invite them to dinner

# * Print a message to each of the two people still on your list,
# letting them know they're still invited.

# * Use del to remove the last two names from you list, so you have
# an empty list. Print your list to make sure you actually have an
# empty list at the end of your program.

myguests = ['Manuel', 'Fidel', 'Ivan', 'Julio', 'Raymon']
myguests.insert(0, "Carlos")
myguests.insert(3, "Francisco")
myguests.append("Mike")

# print("Personas invitadas:")
# for i, x  in enumerate(myguests):
#    print(i+1, x)

# print("He encontrado una mesa mas grande para ustedes, Los esperamos.")

# print("\n")

print(myguests.pop(0),
      "Lo sentimos mucho no podemos invitarte a la cena por falta de espacio")
print(myguests.pop(1),
      "Lo sentimos mucho no podemos invitarte a la cena por falta de espacio")
print(myguests.pop(2),
      "Lo sentimos mucho no podemos invitarte a la cena por falta de espacio")
print(myguests.pop(3),
      "Lo sentimos mucho no podemos invitarte a la cena por falta de espacio")
print(myguests.pop(0),
      "Lo sentimos mucho no podemos invitarte a la cena por falta de espacio")
print(myguests.pop(1),
      "Lo sentimos mucho no podemos invitarte a la cena por falta de espacio")
print(myguests, "Ustedes son los que estan invitados a la cena :-)")
del myguests[0]
del myguests[0]

print("  ", myguests)
