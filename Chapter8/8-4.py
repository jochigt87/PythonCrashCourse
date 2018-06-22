#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Large Shirt: Modify the make_shirt() function so that shirts are large by
# default with a message that reads I Love Python. Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with a
# diferrent message.

def make_shirt(size='large', text='I Love Python'):
    print(size + "\n" + text + "\n")

make_shirt()
make_shirt('medium')
make_shirt('small','Automate Boring Stuff With Python')
