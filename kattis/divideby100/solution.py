n = input()
m = input()
leng = len(n)
nz = len(m) - 1

ans = None
if nz == leng:
	ans = '0.' + n
elif nz > leng:
	ans = '0.' + '0'*(nz-leng) + n
else:
	ans = n[:leng-nz] + '.' + n[leng-nz:]

zeroes_until = -1
while ans[zeroes_until] == '0':
	zeroes_until -= 1

if zeroes_until == -1:
	# no zeroes at end
	print(ans)
elif ans[zeroes_until] == '.':
	# don't need a decimal point
	print(ans[:zeroes_until])
else:
	# remove the zeroes at the end
	print(ans[:zeroes_until+1])
