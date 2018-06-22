#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Album: Write a function called make_album() that builds a dictionary
# describing music album. The function should take in a artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries are storing the
# album information correctly.

def make_album(artist_name, album_title):
    album = {'artist': artist_name, 'title': album_title}
    return album

full_album = make_album('john lenon', 'down to earth')
album2 = make_album('kokolin', 'dirty river')
album3 = make_album('totoro', 'kokoro')
print(album2)
print(album3)
print(full_album)
