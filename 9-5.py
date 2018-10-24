#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Login Attempts: Add an attribute called login_attemps to your User class from
# Exercice 9-3 (page 166). Write a method called increment_login_attempts()
# that increments the value of login_attemps by 1. Write another method called
# reset_login_atttempts() that resets the value of login_attempts to 0.

# Make an instance of the User class and call inscrement_login_attempts()
# several times. Print the value of login_attempts to make sure it was
# incremented properly, and the call reset_login_atttempts(). Print
# login_attempts again to make sure it was reset to 0.


class User():

    # Create two attributes called first_name and last_name
    # and create several other attributes that are typically
    # stored in a user profile
    def __init__(self, first_name, last_name, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        # Add an attribute called login_attemps to your User class.
        self.login_attemps = 0

    def describe_user(self):
        print("Description User's: \n")
        print(self.first_name.title() + " " + self.last_name.title() + "\n " +
              str(self.phone) + "\n " + self.email)
        print("Attempts: " + str(self.login_attemps))

        # return a dictionary with the values first_name and last_name
        # user = {'first_name': self.first_name, 'last_name': self.last_name}
        # print(user)

    def greet_user(self):
        print("Hi User! " + self.first_name.title())

        # Write a method called inscrement_login_attempts that increments the value of login_attemps by 1.
    def increment_login_attempts(self):
        self.login_attemps += 1

    def reset_login_atttempts(self):
        self.login_attemps = 0
        print("Login reset to :" + str(self.login_attemps))


mi_usuario = User('Jochimin', 'Contreras', 8098844268,
                  'contrerasjochimin@gmail.com')

mi_usuario.greet_user()
mi_usuario.increment_login_attempts()
# mi_usuario.reset_login_atttempts()
mi_usuario.describe_user()
