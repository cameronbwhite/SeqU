#!/usr/bin/env python
# Copyright © 2013 Cameron Brandon White

import unittest
import subprocess

class TestSeqU(unittest.TestCase):
    
    def test_success(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0 10')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0\n1\n2\n3\n4\n5\n6\n7\n8\n9\n10')
    
    def test_noargs(self):
        status, text = subprocess.getstatusoutput('./sequ.py')
        self.assertNotEqual(status, 0)
    
    def test_onearg(self):
        status, text = subprocess.getstatusoutput('./sequ.py 1')
        self.assertNotEqual(status, 0)
    
    def test_big2small(self):
        status, text = subprocess.getstatusoutput('./sequ.py 10 0')
        self.assertEqual(status, 0)
        self.assertEqual(text, '')
    
    def test_invalid_type(self):
        status, text = subprocess.getstatusoutput('./sequ.py a 0')
        self.assertNotEqual(status, 0)


