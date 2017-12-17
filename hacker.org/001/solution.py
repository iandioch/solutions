a = 'abcdefghijklmnopqrstuvwxyz'
A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = input()
for c in s:
	if c in a:
		print(a[(a.find(c)+13)%len(a)], end='')
	elif c in A:
		print(A[(A.find(c)+13)%len(A)], end='')
	else:
		print(c, end='')
print() 
