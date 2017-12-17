import codecs
import sys

# braille_mappings.csv stolen gratefully from
# https://raw.githubusercontent.com/markomanninen/pybrl/master/braille_mappings.csv
# which is Copyright (c) 2015 Marko Manninen
# 
# According to the MIT licence:
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.


with codecs.open('braille_mappings.csv', 'r', encoding='utf-8') as f:
	d = {}
	for line in f.readlines():
		p = line.split(',')
		letter = p[2]
		dots = p[3]
		d[dots] = letter
	lines = sys.stdin.readlines()
	for i in range(0, len(lines[0])//3):
		dots = []
		if lines[0][i*3] == '.':
			dots.append(1)
		if lines[1][i*3] == '.':
			dots.append(2)
		if lines[2][i*3] == '.':
			dots.append(3)
		if lines[0][i*3 + 1] == '.':
			dots.append(4)
		if lines[1][i*3 + 1] == '.':
			dots.append(5)
		if lines[2][i*3 + 1] == '.':
			dots.append(6)
		k = '-'.join(str(c) for c in dots)
		print(d[k], end='')
