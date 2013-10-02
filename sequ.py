#!/usr/bin/env python
# Cameron Brandon White

import argparse
from functools import reduce

parser = argparse.ArgumentParser(
	description='Print numbers from FIRST to LAST, in steps of INCREMENT')

parser.add_argument(
	'-f', '--format', metavar='FORMAT',
	help='use printf style floating-point FORMAT',
	dest='format')

parser.add_argument(
	'-s', '--separator', metavar='STRING',
	help='use the STRING to separate numbers',
	dest='separator',
	default='\n',
	type=str)

parser.add_argument(
	'-w', '--equal-width',
	help='equalize width by padding with leading zeroes',
	dest='equalWidth',
	default=False, const=True, action='store_const')

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
	type=int, default=1, nargs='?')

if __name__ == '__main__':

	args = parser.parse_args()

	print(reduce(lambda x, y: str(x) + args.separator + str(y),\
		range(args.first, args.last, args.increment)))
