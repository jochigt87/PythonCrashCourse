#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Admin: An administrator is a special kind of user. Write a class called Admin
# that inherits method from the User class you wrote in Exercise 9-3 (page 166
# or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
# of string like "can add post", "can delete post", "can ban user", and so on.
# Write a method called show_privileges() that lists the administrator's set
# of privileges. Create an instance of Admin, and call your method.


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


class Admin(User):
    """ Clase administrator """

    def __init__(self, first_name, last_name, phone, email):
        super().__init__(first_name, last_name, phone, email)
        self.privileges = [
            'can add post',
            'can delete post',
            "can ban user",
        ]

    def show_privileges(self):
        print("This user can " + str(self.privileges))


yo = User('jochimin', 'contreras', 8098844268, 'contrerasjochimin@gmail.com')
administrator = Admin('root', 'user', 0, 'root_user0@gmail.com')
administrator.describe_user()
administrator.show_privileges()
