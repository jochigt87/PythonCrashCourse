#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Glossary 2: Now that you know to loop through a dictionary, clean up the code
# from Exercise 6-3 (page 102) by replacing your series of print statements
# with a loop that runs through the dictionary's keys and values. When you're
# sure that your loop works, add five more Python terms to your glossary. When
# you run your program again, these new words and meaning should automatically
# be included in the output.


programming_creator = {
        'Dennis_Ritchie': 'C',
        'James_Gosling': 'Java',
        'Guido_Van_Rossum': 'Python',
        'John_Mcarthy': 'LISP',
        'Bredan_Eich': 'Javascript',
        'Rasmus_Lerdorf': 'PHP',
        'Martin_Odersky': 'Scala',
        'Jet_Brains': 'Kotlin',
        'Larry Wall': 'Perl',
        }

for name, language in programming_creator.items():
    print(name,":", language)
