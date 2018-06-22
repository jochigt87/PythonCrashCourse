#!/usr/bin/env python
# -*- coding: utf-8 -*-

# User Album: Start with you program from Exercise 8-7. Write a while loop that
# allows users to enter an album's artist and title. Once you have that
# information, call make_album() with the user's input and print the dictionary
# that's created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title):
    album = {'artist': artist_name, 'title': album_title}
    return album

while True:
    print("\nPlease insert info about your artist name and album title" )
    print("(enter 'q' at any time to quit)")

    artist_name = input("Artist Name:" )
    if artist_name == 'q':
        break

    album_title = input("Album Title: ")
    if album_title == 'q':
        break
musico = make_album(artist_name, album_title)


print(musico)
