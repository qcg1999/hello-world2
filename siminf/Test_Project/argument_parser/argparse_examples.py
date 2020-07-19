# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 00:22:05 2020

@author: Charlie
"""


import argparse
parser = argparse.ArgumentParser()

parser.add_argument('--foo', help='fool a foo.')
parser.add_argument('--age', help='how old.', type=int)
args = parser.parse_args()
print("foo: {}".format(args.foo))
print("age: {}".format(args.age))
