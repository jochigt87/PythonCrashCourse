#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Users: Make a class called User. Create two attributes called first_name and
# last_name, and then create several other attributes that are typically
# stored in a user profile. Make a method called describe_user() that prints a
# summary of the user's information. Make another method called greet_user()
# prints a personalized greeting to other user.

# Create several instances representing different users, and call both methods
# for each user.


# Make a class called User

class User():

    # Create two attributes called first_name and last_name
    # and create several other attributes that are typically
    # stored in a user profile
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


yo = User('jochimin', 'contreras', 8098844268, 'contrerasjochimin@gmail.com')

# Create several instances representing different users and call both methods
# for each user.

yo.describe_user()
yo.greet_user()
