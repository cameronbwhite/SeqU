#!/usr/bin/env python
# Copyright © 2013 Cameron Brandon White
# This specification describes the "universal sequence" command sequ. 
# The sequ command is a backward-compatible set of extensions to the 
# seq UNIX command. There are many implementations of seq out there: 
# this specification is built on the seq supplied with GNU Coreutils 
# version 8.21.

import argparse
import codecs
import sys

# Function which is used as a type for argparse. If the string does 
# not contain only one character then error thrown.
def char(string):
    string = unescape_control_codes(string)
    if len(string) == 1:
        return string
    raise argparse.ArgumentTypeError('must be a single character')

# Control codes are automatically escaped when passed through
# the command line. The following removes the escaping.
def unescape_control_codes(string):
    return codecs.getdecoder('unicode_escape')(string)[0]

def floatIntType(value):
    """ Function which is used as a type for argparse.
    If the argument is not a valid float or int an
    error is thrown. The type returned will be int if
    no fractional component is found otherwise the type
    will be a float."""
    if '.' in value:
        value_type = float
    else:
        value_type = int
    try:
        return value_type(value)
    except ValueError:
        raise argparse.ArgumentTypeError('must be a valid float or int')
    
PARSER = argparse.ArgumentParser(
    description='Print numbers from FIRST to LAST, in steps of INCREMENT')

PARSER.add_argument(
    '--version',
    action='version', version='2.0')

group1 = PARSER.add_mutually_exclusive_group()

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

group2 = PARSER.add_mutually_exclusive_group()

group2.add_argument(
    '-f', '--format', metavar='FORMAT',
    help='use python format style floating-point FORMAT',
    dest='format_str',
    type=str)

group2.add_argument(
    '-p', '--pad', metavar='CHAR',
    help='equalize width by padding with the padding provided',
    dest='padding',
    type=char)

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

PARSER.add_argument(
    'first', metavar='FIRST',
    help='The first number',
    type=floatIntType)

PARSER.add_argument(
    'last', metavar='LAST',
    help='The last number',
    type=floatIntType, default=None, nargs='?')

PARSER.add_argument(
    'increment', metavar='INCREMENT',
    help='The step size',
    type=floatIntType, default=1, nargs='?')

def frange(start, stop, step=1):
    """A range function that accepts floats"""

    while start < stop:
        yield float(start)
        start += step

def separate(separator, iterable):
    """ seperate generates a iterable with the
    separator element between every element of the
    given iterable """ 
    it = iter(iterable)
    value = next(it)
    yield value
    for i in it:
        yield separator
        yield i

def main():

    args = PARSER.parse_args()

    # Handle the case where only one positional argument is
    # given.
    if args.last is None:
        args.last = args.first
        args.first = 1
    
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
        format_str = '{{:{}>{}.{}f}}'.format(
                args.padding, max_length, fractional_length)
    else:
        # Else the default format will be used.
        format_str = '{{:.{}f}}'.format(fractional_length)

    separator = unescape_control_codes(args.separator)

    # format given. separate place the separate between each element.
    for i in separate(separator, map(lambda a: format_str.format(a),
            frange(args.first, args.last + 1, args.increment))):
        print(i, end='')

    print()

if __name__ == '__main__':

    main()
    sys.exit()
