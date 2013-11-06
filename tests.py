#!/usr/bin/env python
# Copyright © 2013 Cameron Brandon White

import unittest
import subprocess

class TestSeqU(unittest.TestCase):
    
    def test_success(self):
        text = subprocess.getoutput('./sequ.py 0 10')
        self.assertEqual(text, '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10')
    
    def test_noargs(self):
        text = subprocess.getoutput('./sequ.py')
        self.assertEqual(text, 'usage: sequ.py [-h] FIRST LAST\nsequ.py: error: the following arguments are required: FIRST, LAST')
    
    def test_onearg(self):
        text = subprocess.getoutput('./sequ.py 1')
        self.assertEqual(text, 'usage: sequ.py [-h] FIRST LAST\nsequ.py: error: the following arguments are required: LAST')
    
    def test_big2small(self):
        text = subprocess.getoutput('./sequ.py 10 0')
        self.assertEqual(text, '')
    
    def test_invalid_type(self):
        text = subprocess.getoutput('./sequ.py a 0')
        self.assertEqual(text, "usage: sequ.py [-h] FIRST LAST\nsequ.py: error: argument FIRST: invalid int value: 'a'")


