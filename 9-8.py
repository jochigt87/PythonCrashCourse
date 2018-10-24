"""
Esto es un Ejercicio de PYTHON CRASH COURSE.

Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of string as described
in Exercise 9-7. Move the show_privileges() method to this class.
Make a Privileges instance as an attribute in the Admin class.
Create a new instance of Admin and use your method to show its privileges.
"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-


class User():
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email

# Make a method called describe_user that prints a
# summary of the user's information.

    def describe_user(self):
        print("Description User's: \n")
        print(self.first_name.title() + " " + self.last_name.title() + "\n " +
              str(self.phone) + "\n " + self.email)

        # return a dictionary with the values first_name and last_name
        user = {'first_name': self.first_name, 'last_name': self.last_name}
        print(user)

    def greet_user(self):
        print("Hi User! " + self.first_name.title())


class Admin(User):
    def __init__(self, first_name, last_name, phone, email):
        super().__init__(first_name, last_name, phone, email)
        self.privileges = [
            'can add post',
            'can delete post',
            'can ban user',
        ]
        self.privilegios = Privileges()

# Write a separate Privileges class, the class
# should have one attribute privileges.


class Privileges():
    self.privileges = [
        'can add post',
        'can delete post',
        'can ban user',
    ]

    def show_privileges(self):
        print("This user can " + str(self.privileges))


yo = Admin('jochimin', 'contreras', 8098844268, 'contrerasjochimin@gmail.com')
print(yo)
