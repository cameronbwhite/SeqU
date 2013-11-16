#!/usr/bin/env python
# Copyright © 2013 Cameron Brandon White

class Alpha:
    """ A single character from 'a' to 'z' """

    def __init__(self, value):
        """ Alpha can be initilized with a number of a letter.
        The letter must be in the alphabet. You may give either
        an upper case or lower case letter. Alpha interprets 0
        as 'a' and 25 as 'z'. Any number greater than 25 is
        rolled back to 0 with mod.
        """

        if type(value) is str:
            if len(value) is not 1:
                raise ValueError("one character only")
        else:
            value = chr(int(value)%26+ord('a'))

        if value.isalpha():
            self._value = value.lower()
        else:
            raise ValueError("must a letter in the alphabet")

    def __str__(self):
        return str(self._value)

    def __repr__(self):
        return "Alpha('{}')".format(self._value)

    def __float__(self):
        return float(int(self))

    def __int__(self):
        return ord(self._value) - ord('a')
