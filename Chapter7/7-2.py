#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Restaurant Seating: Write a program that asks the user how many people are in
# their dinner group. If the answer is more than eight, print a message saying
# they'll have to wait for a table. Otherwise, report that their table is
# ready.

peoples = input("How many people are in your dinner group.? ")

peoples = int(peoples)

if peoples > 8:
    print("You have to wait for a table!")
else:
    print("You table is ready")
