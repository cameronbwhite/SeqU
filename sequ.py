#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2013 Cameron Brandon White
# This specification describes the "universal sequence" command sequ. 
# The sequ command is a backward-compatible set of extensions to the 
# seq UNIX command. There are many implementations of seq out there: 
# this specification is built on the seq supplied with GNU Coreutils 
# version 8.21.

import argparse
import codecs
from roman import Roman
from alpha import Alpha
import sys

FORMAT_WORD_AND_CHAR = {
    'arabic' : 'f', 'ARABIC' : 'f',
    'float'  : 'f', 'FLOAT'  : 'f',
    'roman'  : 'r', 'ROMAN'  : 'R',
    'alpha'  : 'a', 'ALPHA'  : 'A'}

TYPE_AND_FORMAT_WORD = {
    Roman : 'roman',  'roman'  : Roman,
    Alpha : 'alpha',  'alpha'  : Alpha,
    int   : 'arabic', 'arabic' : int,
    float : 'float',  'float'  : float}

def char_type(string):
    """ Function which is used as a type for argparse.
    If the string does not contain only one character
    then an error is thrown.
    """
    string = unescape_control_codes(string)
    if len(string) == 1:
        return string
    raise argparse.ArgumentTypeError('must be a single character')

def float_int_type(value):
    """ Function which is used as a type for argparse.
    If the argument is not a valid float or int an
    error is thrown. The type returned will be int if
    no fractional component is found otherwise the type
    will be a float."""
    if '.' in str(value):
        value_type = float
    else:
        value_type = int
    try:
        return value_type(value)
    except ValueError:
        raise argparse.ArgumentTypeError('must be a valid float or int')

def any_type(value):
    """ Function which is used as a type for argpase. """

    try:
        return float_int_type(value)
    except argparse.ArgumentTypeError:
        pass

    try:
        return Alpha(value)
    except ValueError:
        pass

    try:
        return Roman(value)
    except ValueError:
        pass

    raise argparse.ArgumentTypeError(
            'Must be a valid int, float, Alpha, or Roman')

def parse():
    parser = argparse.ArgumentParser(
        description='Print numbers from FIRST to LAST, in steps of INCREMENT')

    parser.add_argument(
        '--version',
        action='version', version='2.0')

    parser.add_argument(
       '-F', '--format-word',
       dest='format_word',
       choices = FORMAT_WORD_AND_CHAR.keys())

    group1 = parser.add_mutually_exclusive_group()

    group1.add_argument(
        '-s', '--separator', metavar='STRING',
        help='use the STRING to separate numbers',
        dest='separator',
        default='\n',
        type=str)

    group1.add_argument(
        '-W', '--words',
        help='Output the sequence as a single space-separeted line of words',
        dest='separator',
        const=' ', action='store_const')

    group2 = parser.add_mutually_exclusive_group()

    group2.add_argument(
        '-f', '--format', metavar='FORMAT',
        help='use python format style floating-point FORMAT',
        dest='format_str',
        type=str)

    group2.add_argument(
        '-p', '--pad', metavar='CHAR',
        help='equalize width by padding with the padding provided',
        dest='padding',
        type=char_type)

    group2.add_argument(
        '-P', '--pad-spaces',
        help='equalize width by padding with leading spaces',
        dest='padding',
        const=' ', action='store_const')

    group2.add_argument(
        '-w', '--equal-width',
        help='equalize width by padding with leading zeroes',
        dest='padding',
        const='0', action='store_const')
    
    args = parser.parse_known_args()[0]
    
    try:
        argument_type = TYPE_AND_FORMAT_WORD[
                str(args.format_word).lower()]
    except KeyError:
        argument_type = any_type
    
    parser.add_argument(
        'first', metavar='FIRST',
        help='The first number',
        type=argument_type, default=argument_type(1), nargs='?')

    parser.add_argument(
        'increment', metavar='INCREMENT',
        help='The step size',
        type=argument_type, default=argument_type(1), nargs='?')

    parser.add_argument(
        'last', metavar='LAST',
        help='The last number',
        type=argument_type)

    return parser.parse_args()

def frange(start, stop, step=1):
    """A range function that accepts floats"""

    while start < stop:
        yield float(start)
        start += step

def longest_roman(n):
    lengths = {
         1 : 1,   2 : 2,   3 : 3,    8 : 4,   18 : 5,   28 : 6, 38 : 7,
        88 : 8, 188 : 9, 288 : 10, 388 : 11, 488 : 12, 988 : 13}
    n = int(Roman(n))
    last = 0
    for i in sorted(lengths):
        if n%1000 <= i:
            last = i
            break
    return lengths[last] + (n // 1000)

def separate(separator, iterable):
    """ seperate generates a iterable with the
    separator element between every element of the
    given iterable. """
    it = iter(iterable)
    value = next(it)
    yield value
    for i in it:
        yield separator
        yield i

def unescape_control_codes(string):
    """ Control codes are automatically escaped when passed
    through the command line. The following removes the
    escaping. """
    return codecs.getdecoder('unicode_escape')(string)[0]

def main():
    
    args = parse()
    
    # Determine the length of the largest fractional part of the
    # three positional arguments. From bottom to top, right to left
    # this statement does the following. First the number is turned
    # into a string then split into its integer and fractional parts,
    # next if the number had a fractional part the len of it is
    # taken, finally the largest length is return.
    fractional_length = max(
        map(lambda parts: len(parts[1]) if len(parts) == 2 else 0,
            map(lambda number: str(number).split('.'), 
                [args.first, args.last, args.increment])))

    # The length of the largest number.
    max_length = len(str(int(args.last))) + fractional_length
    max_length += 1 if fractional_length else 0 # for the '.'
    
    try:
        format_character = FORMAT_WORD_AND_CHAR[args.format_word]
    except KeyError:
        word = TYPE_AND_FORMAT_WORD[type(args.last)]
        word = word.lower() if str(args.last).islower() else word.upper()
        format_character = FORMAT_WORD_AND_CHAR[word]

    format_type = type(args.last)
    format_type = float if format_type is int else format_type

    # Depending on the options used the format will be constructed
    # differently.
    if args.format_str:
        # If the format option was used then the format given will
        # be passed directly.
        format_str = '{{{}}}'.format(args.format_str)
    elif args.padding:
        # If a padding was provided then apply it by constructing
        # the format with the supplied padding character and the
        # length of the largest number.
        if format_character == 'f':
            format_str = '{{:{}>{}.{}{}}}'.format(
                    args.padding, max_length, fractional_length,
                    format_character)
        else:
            format_str = '{{:{}>{}{}}}'.format(
                    args.padding, max_length, format_character)

    else:
        # Else the default format will be used.
        if format_character == 'f':
            format_str = '{{:.{}{}}}'.format(
                    fractional_length, format_character)
        else:
            format_str = '{{:{}}}'.format(format_character)

    separator = unescape_control_codes(args.separator)
    
    # The following statement creates a list of integers using the
    # range specified by first, last, and increment. The map
    # transforms the list into a list of interger strings using the
    # format given. separate places the separator between each element.
    for i in separate(separator, 
             map(lambda a: format_str.format(a),
             map(lambda b: format_type(b),
             frange(float(args.first), (float(args.last)+1),
                 float(args.increment))))):
        print(i, end='')

    print()

if __name__ == '__main__':
    
    try:
        main()
    except SystemExit:
        sys.exit(1)
    else:
        sys.exit(0)
