import sys

def countNucleotides(s):
	numA = 0
	numT = 0
	numG = 0
	numC = 0

	for char in s:
		if char == 'A':
			numA+=1
		elif char == 'T':
			numT+=1
		elif char == 'G':
			numG+=1
		elif char == 'C':
			numC+=1

	return str(numA) + " " + str(numC) + " " + str(numG) + " " + str(numT)

if __name__=='__main__':
	s = sys.stdin.readline()
	print countNucleotides(s)