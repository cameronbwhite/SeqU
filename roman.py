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

    def __init__(self, number):

        self._roman = ''
        for i in reversed(sorted(NUMBER_TO_ROMAN)):
            self._roman += NUMBER_TO_ROMAN[i] * (number // i)
            number %= i

    def __str__(self):

        return str(self._roman)

    def __repr__(self):

        return repr(self._roman)

    def toNumber(self):

        number = 0
        roman = self._roman
        for i in reversed(sorted(NUMBER_TO_ROMAN,
                key=lambda a: len(NUMBER_TO_ROMAN[a]))):
            while NUMBER_TO_ROMAN[i] in roman:
                number += i
                roman = roman.replace(NUMBER_TO_ROMAN[i], '', 1)
        return number


