#!/usr/bin/python3
"""
Module contains the ``print_square`` function
"""


def text_indentation(text):
    """Prints a text with 2 new lines aftereach of
    these characters: . , ? and :"""
    if type(text) != str:
        raise TypeError('text must be a string')
    else:
        for i in text:
            if (i == '.') or (i == '?') or (i == ':'):
                print('\n')
            else:
                print(i, end='')
