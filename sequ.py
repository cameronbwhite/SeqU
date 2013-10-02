#!/usr/bin/env python
# Cameron Brandon White

import argparse

parser = argparse.ArgumentParser(
	description='Print the numbers from start to end.')

parser.add_argument(
	'start',
	help='The starting place',
	type=int)

parser.add_argument(
	'end',
	help='The ending place',
	type=int)

if __name__ == '__main__':

	args = parser.parse_args()

	for i in range(args.start, args.end):
		print(i)