#!/usr/bin/env python

import sys
from string import join

try:
	fin = open(sys.argv[1], "r")
except:
	sys.exit("Error, no/invalid input file")

try:
	fin2 = open(sys.argv[2], "r")
except:
	sys.exit("Error, no/invalid input file")

try:
	fout = open(sys.argv[3], "w")
except:
	sys.exit("Error, no/invalid output file")

class county(object):
	written = False
	def __init__(self, state, fips):
		self.state = state
		self.fips = fips

	def add_data(self, total_water):
		self.total_water = total_water

s = fin.read()

lines = [s]

for i in ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']:
	new_lines = []
	for j in lines:
		new_lines.extend(j.split('\n' + i + '\t'))

	lines = new_lines

lines = lines[1:]

counties = []

for line in lines:
	l = line.split()
	new_county = county(l[2], l[3])
	new_county.add_data(l[-6])
	counties.append(new_county)

curlines = fin2.readlines()

for curline in curlines:
	l = curline.split()
	for i in range(len(counties)):
		county = counties[i]
		if l[0] == county.state and l[1] == county.fips:
			break

	l.insert(2, county.total_water)

	fout.write('\t'.join(l) + '\n')
	county.written = True

for county in counties:
	if county.written:
		continue

	fout.write(str(county.state) + '\t' + str(county.fips) + '\t' + '\t' + '\t' + str(county.total_water) + '\n')
