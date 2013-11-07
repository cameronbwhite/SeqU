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
from functools import reduce

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

PARSER.add_argument(
    '-s', '--separator', metavar='STRING',
    help='use the STRING to separate numbers',
    dest='separator',
    default='\n',
    type=str)

GROUP = PARSER.add_mutually_exclusive_group()

GROUP.add_argument(
    '-f', '--format', metavar='FORMAT',
    help='use python format style floating-point FORMAT',
    dest='format_str',
    type=str)

GROUP.add_argument(
    '-w', '--equal-width',
    help='equalize width by padding with leading zeroes',
    dest='equal_width',
    default=False, const=True, action='store_const')

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

    # Depending on the options used the format will be constructed
    # differently.
    if args.format_str:
        # If the format option was used then the format given will
        # be passed directly.
        format_str = '{{{}}}'.format(args.format_str)
    elif args.equal_width:
        # If the equal_width option was used then the format will
        # pad 0s using the length of the largest number.
        format_str = '{{:0{}.{}f}}'.format(
                len(str(args.last)), fractional_length)
    else:
        # Else the empty format will be used specifing no
        # formatting.
        format_str = '{{:.{}f}}'.format(fractional_length)

    # Control codes are automatically escaped when passed through
    # the command line. The following statement removes the escaping.
    separator = codecs.getdecoder('unicode_escape')(args.separator)[0]

    # The following statement creates a list of integers using the
    # range specified by first, last, and increment. The map
    # transform the list into a list of interger strings using the
    # format given. The reduce concatenates all the strings in the
    # list together with the separator in between.
    try:
        print(reduce(lambda x, y: x + separator + y,
            map(lambda a: format_str.format(a),
                frange(args.first, args.last + 1, args.increment))))
    except TypeError:
        pass

if __name__ == '__main__':

    main()
    sys.exit()

