#!/usr/bin/env python
# Cameron Brandon White

import argparse
import codecs
from roman import Roman
from functools import reduce

FORMAT_WORDS = ['arabic', 'ARABIC',
               'alpha',  'ALPHA',
               'roman',  'ROMAN',
               'floating', 'FLOATING']

def sequRange(formatWord, first, last, increment):
    """ Function for sequ to generate a range based on the
    formatWord.
    """

    if formatWord in ['roman', 'ROMAN']:
        mapping = map(lambda x: str(Roman(x)),
                range(Roman(first).toNumber(), 
                      Roman(last).toNumber() + 1, 
                      Roman(increment).toNumber()))
        if formatWord.isupper():
            mapping = map(lambda x: x.upper(), mapping)

    elif formatWord in ['arabic', 'ARABIC']:
        mapping = range(first, last + 1, increment)

    elif formatWord in ['floating', 'FLOATING']:
        mapping = frange(first, last + 1.0, increment)

    elif formatWord in ['alpha', 'ALPHA']:
        if isinstance(first, str):
            first = ord(first)
        if isinstance(last, str):
            last = ord(last)
        if isinstance(increment, str):
            increment = ord(increment)
        mapping = map(lambda x: chr(x), range(first, last + 1, increment)) 
        if formatWord.isupper():
            mapping = map(lambda x: x.upper(), mapping)

    return mapping

def frange(start, stop, step=1.0):
    """ Floating point range function """

    if start >= stop:
        yield start

    while start < stop:
        yield start
        start += step

def charType(string):
    """ Function which is used as a type for argparse.
    If the string does not contain only one character
    then an error is thrown.
    """
    string = unescape_control_codes(string)
    if len(string) == 1:
        return string
    raise argparse.ArgumentTypeError('must be a single character')

def formatWordType(word):
    """ Function which is used as a type for argparse.
    If the string is not in list then an error is thrown.
    """
    if word in FORMAT_WORDS:
        return word
    else:
        raise argparse.ArgumentTypeError('Must be a format Word')

def romanType(number):
    """ Function which is used as a type for argparse.
    If the argument is not a type of Roman number then
    an error is thrown.
    """
    try:
        return Roman(number)
    except:
        raise argparse.ArgumentTypeError('Must be a valid roman number')

def unescape_control_codes(string):
    """ Control codes are automatically escaped when 
    passed through the command line. The following 
    removes the escaping.
    """
    return codecs.getdecoder('unicode_escape')(string)[0]

PARSER = argparse.ArgumentParser(
    description='Print numbers from FIRST to LAST, in steps of INCREMENT')

PARSER.add_argument(
    '--version',
    action='version', version='2.0')

PARSER.add_argument(
   '-F', '--format-word',
   dest='formatWord',
   default='arabic',
   type=formatWordType)

GROUP1 = PARSER.add_mutually_exclusive_group()

GROUP1.add_argument(
    '-s', '--separator', metavar='STRING',
    help='use the STRING to separate numbers',
    dest='separator',
    default='\n',
    type=str)

GROUP1.add_argument(
    '-W', '--words',
    help='Output the sequence as a single space-separeted line of words',
    dest='separator',
    const=' ', action='store_const')

GROUP2 = PARSER.add_mutually_exclusive_group()

GROUP2.add_argument(
    '-f', '--format', metavar='FORMAT',
    help='use python format style floating-point FORMAT',
    dest='formatStr',
    type=str)

GROUP2.add_argument(
    '-p', '--pad', metavar='CHAR',
    help='equalize width by padding with the padding provided',
    dest='padding',
    type=charType)

GROUP2.add_argument(
    '-P', '--pad-spaces',
    help='equalize width by padding with leading spaces',
    dest='padding',
    const=' ', action='store_const')

GROUP2.add_argument(
    '-w', '--equal-width',
    help='equalize width by padding with leading zeroes',
    dest='padding',
    const='0', action='store_const')

PARSER.add_argument(
    'first', metavar='FIRST',
    help='The first number')

PARSER.add_argument(
    'last', metavar='LAST',
    help='The last number')

PARSER.add_argument(
    'increment', metavar='INCREMENT',
    help='The step size',
    default=1, nargs='?')

def main():

    args = PARSER.parse_args()

    # Depending on the options used the format will be constructed
    # differently.
    if args.formatStr:
        # If the format option was used then the format given will
        # be passed directly.
        formatStr = '{{{}}}'.format(args.formatStr)
    elif args.padding:
        # If a padding was provided then apply it by constructing
        # the format with the supplied padding character and the
        # length of the largest number.
        formatStr = '{{:{}>{}}}'.format(args.padding,
                                     len(str(args.last)))
    else:
        # Else the empty format will be used specifing no
        # formatting.
        formatStr = '{}'

    separator = unescape_control_codes(args.separator)

    # The following statement creates a list of integers using the
    # range specified by first, last, and increment. The map
    # transform the list into a list of interger strings using the
    # format given. The reduce concatenates all the strings in the
    # list together with the separator in between.
    print(reduce(lambda x, y: x + separator + y,
        map(lambda a: formatStr.format(a),
            sequRange(args.formatWord, 
                      args.first, args.last, args.increment))))

if __name__ == '__main__':

    main()
