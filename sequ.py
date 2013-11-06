#!/usr/bin/env python
# Copyright © 2013 Cameron Brandon White
# This specification describes the "universal sequence" command sequ. 
# The sequ command is a backward-compatible set of extensions to the 
# seq UNIX command. There are many implementations of seq out there: 
# this specification is built on the seq supplied with GNU Coreutils 
# version 8.21.

import argparse

PARSER = argparse.ArgumentParser(
	description='Print the numbers from FIRST to LAST.')

PARSER.add_argument(
	'FIRST',
	help='The starting place',
	type=int)

PARSER.add_argument(
	'LAST',
	help='The ending place',
	type=int)

if __name__ == '__main__':

    ARGS = PARSER.parse_args()

    for i in range(ARGS.first, ARGS.last + 1):
        print(i)
