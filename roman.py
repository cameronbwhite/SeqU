#!/usr/bin/env python
# Cameron Brandon White

NUMBER_TO_ROMAN = {
  1     : 'i',
  4     : 'iv',
  5     : 'v',
  9     : 'ix',
  10    : 'x',
  40    : 'xl',
  50    : 'l',
  90    : 'xc',
  100   : 'c',
  500   : 'd',
  1000  : 'm'
 }

class Roman(object):
    """ Class to represent Roman numbers """    

    def __init__(self, number):
        """ Roman can be initilized with a positive integer or
        a string with a valid roman number. It can also act as
        a copy constructor if number is a another Roman.
        """
        if isinstance(number, int): 
            if number <= 0:
                raise ValueError('number must be greater than 0')
            self._roman = ''
            for i in reversed(sorted(NUMBER_TO_ROMAN)):
                self._roman += NUMBER_TO_ROMAN[i] * (number // i)
                number %= i
        elif isinstance(number, str):
            self._roman = number.lower()
            self.toNumber()
        elif isinstance(number, Roman):
            self._roman = number._roman

    def __str__(self):

        return str(self._roman)

    def __repr__(self):

        return repr(self._roman)
    
    def __format__(self, format_spec):
    
        type_char = format_spec[-1]
        if type_char not in ['r', 'R']:
            raise ValueError(
                "Unknown format code '{}' for object in type {}".format(
                    type_char, type(self)))
    
        func = str.upper if str.isupper(type_char) else str.lower
        return format(func(str(self)), format_spec[:-1])
    
    def __float__(self):

        return float(self.toNumber())

    def __int__(self):

        return int(self.toNumber())

    def toNumber(self):
        """ Return the integer representation of the number """

        number = 0
        roman = self._roman
        for i in reversed(sorted(NUMBER_TO_ROMAN,
                key=lambda a: len(NUMBER_TO_ROMAN[a]))):
            while NUMBER_TO_ROMAN[i] in roman:
                number += i
                roman = roman.replace(NUMBER_TO_ROMAN[i], '', 1)
        if roman:
            raise SyntaxError('Invalid Roman number')
        return number


