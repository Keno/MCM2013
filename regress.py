#!/usr/bin/env python

import os
import sys
import string

missing = ('21','23','41','42','47','48','49','54')

def regression(a, b, c, state):
	if state in missing:
		return (c-a) * 2 + c
	else:
		return (c-a) * 5.0 / 2 + (a+b+c)/3.0

try:
	fin = open(sys.argv[1], "r")
except:
	sys.exit("Error, no/invalid input file")

try:
	fout = open(sys.argv[2], "w")
except:
	sys.exit("Error, no/invalid output file")

class county(object):
	w25 = 0
	def __init__(self, state, fips, w95, w00, w05):
		self.state = state
		self.fips = fips
		self.w00 = w00
		self.w95 = w95
		self.w05 = w05

s = fin.readlines()
s = s[1:]

counties = [county(x[0],x[1],x[2],x[3],x[4]) for x in map(string.split, s)]
	
for county in counties:
	county.w25 = regression(float(county.w95), float(county.w00), float(county.w05), county.state)

	fout.write(county.state + '\t')
	fout.write(county.fips + '\t')
	fout.write(county.w95 + '\t')
	fout.write(county.w00 + '\t')
	fout.write(county.w05 + '\t')
	fout.write(str(county.w25) + '\n')

