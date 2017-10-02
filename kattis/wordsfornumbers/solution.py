import sys

def num2word(num):
	u = {
		0: 'zero',
		1: 'one',
		2: 'two',
		3: 'three',
		4: 'four',
		5: 'five',
		6: 'six',
		7: 'seven',
		8: 'eight',
		9: 'nine',
		10: 'ten',
		11: 'eleven',
		12: 'twelve',
		13: 'thirteen',
		14: 'fourteen',
		15: 'fifteen',
		16: 'sixteen',
		17: 'seventeen',
		18: 'eighteen',
		19: 'nineteen',
	}
	d = {
		2: 'twenty',
		3: 'thirty',
		4: 'forty',
		5: 'fifty',
		6: 'sixty',
		7: 'seventy',
		8: 'eighty',
		9: 'ninety',
	}
	if num < 20:
		return u[num]
	p = num//10
	q = num%10
	if q == 0:
		return d[p]
	return d[p]+'-'+u[q]

nums = []
for i in range(99, -1, -1):
	s = num2word(i)
	nums.append((str(i), s))


for line in sys.stdin.readlines():
	s = line
	for num, numstring in nums:
		s = s.replace(num, numstring)
	if s[0].upper() != line[0].upper():
		s = s[0].upper() + s[1:]
	print(s, end='')
