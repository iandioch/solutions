buf = [0]
prev = 0
step = int(input())
for num in range(1, 2018):
	prev += step
	prev %= len(buf)
	prev += 1
	buf = buf[:prev] + [num] + buf[prev:]
print(buf[(prev+1)%len(buf)])
