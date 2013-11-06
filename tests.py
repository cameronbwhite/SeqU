#!/usr/bin/env python
# Copyright © 2013 Cameron Brandon White

import unittest
import subprocess

class TestSeqU(unittest.TestCase):
    
    def test_twoargs_allint(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0 5')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0\n1\n2\n3\n4\n5')

    def test_twoargs_allfloat(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0.0 5.0')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0.0\n1.0\n2.0\n3.0\n4.0\n5.0')

    def test_twoargs_onefloat_1(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0.0 5')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0.0\n1.0\n2.0\n3.0\n4.0\n5.0')

    def test_twoargs_onefloat_2(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0 5.0')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0.0\n1.0\n2.0\n3.0\n4.0\n5.0')

    def test_threeargs_allint(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0 5 2')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0\n2\n4')

    def test_threeargs_allfloat(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0.0 5.0 2.0')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0.0\n2.0\n4.0')

    def test_threeargs_onefloat_1(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0.0 5 2')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0.0\n2.0\n4.0')

    def test_threeargs_onefloat_2(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0 5.0 2')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0.0\n2.0\n4.0')

    def test_threeargs_onefloat_3(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0 5 2.0')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0.0\n2.0\n4.0')

    def test_threeargs_twofloat_1(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0.0 5.0 2')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0.0\n2.0\n4.0')

    def test_threeargs_twofloat_2(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0.0 5 2.0')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0.0\n2.0\n4.0')

    def test_threeargs_twofloat_3(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0 5.0 2.0')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0.0\n2.0\n4.0')
    
    def test_noargs(self):
        status, text = subprocess.getstatusoutput('./sequ.py')
        self.assertNotEqual(status, 0)
    
    def test_onearg_1_int(self):
        status, text = subprocess.getstatusoutput('./sequ.py 1')
        self.assertEqual(status, 0)
        self.assertEqual(text, '1')

    def test_onearg_1_float(self):
        status, text = subprocess.getstatusoutput('./sequ.py 1.0')
        self.assertEqual(status, 0)
        self.assertEqual(text, '1.0')

    def test_onearg_5_int(self):
        status, text = subprocess.getstatusoutput('./sequ.py 5')
        self.assertEqual(status, 0)
        self.assertEqual(text, '1\n2\n3\n4\n5')

    def test_onearg_5_float(self):
        status, text = subprocess.getstatusoutput('./sequ.py 5.0')
        self.assertEqual(status, 0)
        self.assertEqual(text, '1.0\n2.0\n3.0\n4.0\n5.0')
    
    def test_big2small(self):
        status, text = subprocess.getstatusoutput('./sequ.py 10 0')
        self.assertEqual(status, 0)
        self.assertEqual(text, '')
    
    def test_invalid_type(self):
        status, text = subprocess.getstatusoutput('./sequ.py a 0')
        self.assertNotEqual(status, 0)
