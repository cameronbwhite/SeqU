#!/usr/bin/env python
# Cameron Brandon White

import argparse
from functools import reduce

parser = argparse.ArgumentParser(
	description='Print numbers from FIRST to LAST, in steps of INCREMENT')

parser.add_argument(
	'--version',
	action='version', version='2.0')

parser.add_argument(
	'-s', '--separator', metavar='STRING',
	help='use the STRING to separate numbers',
	dest='separator',
	default='\n',
	type=str)

group = parser.add_mutually_exclusive_group()

group.add_argument(
	'-f', '--format', metavar='FORMAT',
	help='use python format style floating-point FORMAT',
	dest='format', 
	type=str)

group.add_argument(
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
	help='The step size',
	type=int, default=1, nargs='?')

if __name__ == '__main__':

	args = parser.parse_args()

	if args.format:
		format = '{{{}}}'.format(args.format)
	elif args.equalWidth:
		format = '{{:0{}}}'.format(len(str(args.last)))
	else:
		format = '{}'

	print(reduce(lambda x, y: x + args.separator + y,
		map(lambda a: format.format(a),
			range(args.first, args.last + 1, args.increment))))
