#!/usr/bin/env python
# Copyright © 2013 Cameron Brandon White
# This specification describes the "universal sequence" command sequ. 
# The sequ command is a backward-compatible set of extensions to the 
# seq UNIX command. There are many implementations of seq out there: 
# this specification is built on the seq supplied with GNU Coreutils 
# version 8.21.

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

	for i in range(args.start, args.end + 1):
		print(i)