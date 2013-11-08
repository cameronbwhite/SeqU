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
        status, text = subprocess.getstatusoutput('./sequ.py 0 2 5')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0\n2\n4')

    def test_threeargs_allfloat(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0.0 2.0 5.0')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0.0\n2.0\n4.0')

    def test_threeargs_onefloat_1(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0.0 2 5')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0.0\n2.0\n4.0')

    def test_threeargs_onefloat_2(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0 2 5.0')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0.0\n2.0\n4.0')

    def test_threeargs_onefloat_3(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0 2.0 5')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0.0\n2.0\n4.0')

    def test_threeargs_twofloat_1(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0.0 2 5.0')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0.0\n2.0\n4.0')

    def test_threeargs_twofloat_2(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0.0 2.0 5')
        self.assertEqual(status, 0)
        self.assertEqual(text, '0.0\n2.0\n4.0')

    def test_threeargs_twofloat_3(self):
        status, text = subprocess.getstatusoutput('./sequ.py 0 2.0 5.0')
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

    def test_separator_1(self):
        status, text = subprocess.getstatusoutput('./sequ.py -s \':\' 1 10')
        self.assertEqual(status, 0)
        self.assertEqual(text, '1:2:3:4:5:6:7:8:9:10')

    def test_seperator_spaces_1(self):
        status, text = subprocess.getstatusoutput(
                './sequ.py -s \' \' 3')
        self.assertEqual(status, 0)
        self.assertEqual(text, '1 2 3')
        
    def test_equalwidth_1(self):
        status, text = subprocess.getstatusoutput(
                './sequ.py -w 1 20 100')
        self.assertEqual(status, 0)
        self.assertEqual(text, '001\n021\n041\n061\n081')

    def test_equalwidth_2(self):
        status, text = subprocess.getstatusoutput(
                './sequ.py -w 1 20.1 100')
        self.assertEqual(status, 0)
        self.assertEqual(text, '001.0\n021.1\n041.2\n061.3\n081.4')
    
    def test_words_1(self):
        status, text = subprocess.getstatusoutput(
                './sequ.py -W 3')
        self.assertEqual(status, 0)
        self.assertEqual(text, '1 2 3')
    
    def test_pad_spaces_1(self):
        status, text = subprocess.getstatusoutput(
                './sequ.py -P 0 500 1000')
        self.assertEqual(status, 0)
        self.assertEqual(text, '   0\n 500\n1000')

    def test_pad_letter_1(self):
        status, text = subprocess.getstatusoutput(
                './sequ.py -p a 0 500 1000')
        self.assertEqual(status, 0)
        self.assertEqual(text, 'aaa0\na500\n1000')
