#!/usr/bin/env python

import os
import sys
from numpy import loadtxt, where
from scipy import stats

try:
	data = loadtxt(sys.argv[1])
except:
	sys.exit("Can't read file.")

X = range(85, 110, 5)

for l in data:
	gradient, intercept, r_value, p_value, std_err = stats.linregress(X, l[2:])
	print gradient * 125 + intercept
