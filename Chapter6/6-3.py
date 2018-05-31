#!/usr/bin/env python

# -*- coding: utf-8 -*-

# Glosary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion , let's call it glossary.

# Think of five programming words you've learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meaning as values.


# Print each word and its meaning as neatly formatted output. You might print
# the word followed by a colon and then its meaning, or print the word an one
# line and then print its meaning indented on a second line. Use the newline
# character(\n) to insert a blank line between each word-meaning pair in your
# output.

programming_creator = {
        'Dennis_Ritchie': 'C',
        'James_Gosling': 'Java',
        'Guido_Van_Rossum': 'Python',
        'John_Mcarthy': 'LISP',
        'Bredan_Eich': 'Javascript',
        }

for name, language in programming_creator.items():
    print(name,":", language)

