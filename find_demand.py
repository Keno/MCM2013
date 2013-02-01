#!/usr/bin/env python

import sys

try:
	fin = open(sys.argv[1], "r")
except:
	sys.exit("Error, no/invalid input file")

try:
	fout = open(sys.argv[2], "w")
except:
	sys.exit("Error, no/invalid output file")

class county(object):
	def __init__(self, state, fips):
		self.state = state
		self.fips = fips

	def add_data(self, total_water, total_fresh, total_saline, total_ground, total_surface):
		self.total_water = total_water
		self.total_fresh = total_fresh
		self.total_saline = total_saline
		self.total_ground = total_ground
		self.total_surface = total_surface

s = fin.read()

lines = s.split('\r1995\t')
lines = lines[1:]
counties = []

for line in lines:
	l = line.split('\t')
	new_county = county(l[1], l[2])
	new_county.add_data(l[-6], l[-8], l[-7], l[-12], l[-9])
	counties.append(new_county)

for county in counties:
	fout.write(str(county.state) + '\t' + str(county.fips) + '\t' + str(county.total_water) + '\n')
