import sys

def countGC(s):
	count = 0
	for char in s:
		if char == 'G' or char == 'C':
			count += 1

	return 100*(count + 0.0)/len(s)

def main():
	data = sys.stdin.read()
	lines = data.split("\n")
	curr = ""
	name = ""
	first = True

	highest = 0
	highestName = ""
	for line in lines:
		line = line.strip(" ").strip("\n")
		if len(line) == 0:
			continue
		if line[0] == '>':
			if not first:
				x = countGC(curr)
				#print name, " : ", curr, " : ", x
				if x > highest:
					highest = x
					highestName = name
			curr = ""
			name = line[1:]
			first = False
		else:
			curr += line

	# there's one more line left
	x = countGC(curr)
	#print name, " : ", curr, " : ", x
	if x > highest:
		highest = x
		highestName = name

	print highestName
	print highest

if __name__ == '__main__':
	main()
