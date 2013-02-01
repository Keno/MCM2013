#!/usr/bin/env python

import os
import sys
import string
from numpy import loadtxt
from scipy import stats

missing = (21,23,41,42,47,48,49,54)

try:
	fin = open(sys.argv[1], "r")
except:
	sys.exit("Error, no/invalid input file")

try:
	fout = open(sys.argv[2], "w")
except:
	sys.exit("Error, no/invalid output file")

try:
	data = loadtxt(sys.argv[1])
except:
	sys.exit("Can't read file.")

lines = fin.readlines()

X = range(85, 110, 5)
X2 = [85, 90, 95, 105]

for i in range(len(lines)):
	if data[i, 0] in missing:
		l = []
		l.extend(data[i, 2:])
		l.remove(l[-2])
		g, y, r, p, std_err = stats.linregress(X2, l)

		lines[i] = (lines[i].split('\n'))[0] + '\t' + str(g * 125.0 + y) + '\n'
	else:
		l = data[i, 2:]
		g, y, r, p, std_err = stats.linregress(X, l)

		lines[i] = (lines[i].split('\n'))[0] + '\t' + str(g * 125.0 + y) + '\n'

for line in lines:
	fout.write(line)
