#!/usr/bin/env python
# Cameron Brandon White

import argparse
import codecs
from functools import reduce

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

parser = argparse.ArgumentParser(
    description='Print numbers from FIRST to LAST, in steps of INCREMENT')

parser.add_argument(
    '--version',
    action='version', version='2.0')

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
    dest='format', 
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

parser.add_argument(
    'first', metavar='FIRST',
    help='The first number',
    type=int)

parser.add_argument(
    'last', metavar='LAST',
    help='The last number',
    type=int)

parser.add_argument(
    'increment', metavar='INCREMENT',
    help='The step size',
    type=int, default=1, nargs='?')

if __name__ == '__main__':

    args = parser.parse_args()

    # Depending on the options used the format will be constructed
    # differently. 
    if args.format:
        # If the format option was used then the format given will 
        # be passed directly.
        format = '{{{}}}'.format(args.format)
    elif args.padding:
        # If a padding was provided then apply it by constructing
        # the format with the supplied padding character and the
        # length of the largest number.
        format = '{{:{}>{}d}}'.format(args.padding, 
                                      len(str(args.last)))
    else:
        # Else the empty format will be used specifing no 
        # formatting.
        format = '{}'

    separator = unescape_control_codes(args.separator)

    # The following statement creates a list of integers using the 
    # range specified by first, last, and increment. The map 
    # transform the list into a list of interger strings using the
    # format given. The reduce concatenates all the strings in the
    # list together with the separator in between.
    print(reduce(lambda x, y: x + separator + y,
        map(lambda a: format.format(a),
            range(args.first, args.last + 1, args.increment))))
