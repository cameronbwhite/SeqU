#!/usr/bin/env python
# Copyright © 2013 Cameron Brandon White
# This specification describes the "universal sequence" command sequ. 
# The sequ command is a backward-compatible set of extensions to the 
# seq UNIX command. There are many implementations of seq out there: 
# this specification is built on the seq supplied with GNU Coreutils 
# version 8.21.

import argparse
import codecs
from functools import reduce

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
    dest='format',
    type=str)

GROUP.add_argument(
    '-w', '--equal-width',
    help='equalize width by padding with leading zeroes',
    dest='equalWidth',
    default=False, const=True, action='store_const')

PARSER.add_argument(
    'first', metavar='FIRST',
    help='The first number',
    type=float)

PARSER.add_argument(
    'last', metavar='LAST',
    help='The last number',
    type=float)

PARSER.add_argument(
    'increment', metavar='INCREMENT',
    help='The step size',
    type=float, default=1, nargs='?')

def frange(start, stop, step=1):
    """A range function that accepts floats"""

    if start >= stop:
        yield start

    while start < stop:
        yield start
        start += step

def main():

    args = PARSER.parse_args()

    # Depending on the options used the format will be constructed
    # differently.
    if args.format:
        # If the format option was used then the format given will
        # be passed directly.
        format = '{{{}}}'.format(args.format)
    elif args.equalWidth:
        # If the equalWidth option was used then the format will
        # pad 0s using the length of the largest number.
        format = '{{:0{}}}'.format(len(str(args.last)))
    else:
        # Else the empty format will be used specifing no
        # formatting.
        format = '{}'

    # Control codes are automatically escaped when passed through
    # the command line. The following statement removes the escaping.
    separator = codecs.getdecoder('unicode_escape')(args.separator)[0]

    # The following statement creates a list of integers using the
    # range specified by first, last, and increment. The map
    # transform the list into a list of interger strings using the
    # format given. The reduce concatenates all the strings in the
    # list together with the separator in between.
    print(reduce(lambda x, y: x + separator + y,
        map(lambda a: format.format(a),
            frange(args.first, args.last + 1, args.increment))))

if __name__ == '__main__':

    main()
