import sys

def merge(a, b):
	result = []
	index = 0
	x = 0
	y = 0
	while(index < len(a) + len(b)):
		if y == len(b):
			result.append(a[x])
			x+=1
		elif x < len(a) and a[x] < b[y]:
			result.append(a[x])
			x+=1
		else:
			result.append(b[y])
			y+=1
		index += 1
	return result

def mergeSort(a):
	if len(a) == 1:
		return a
	return merge(mergeSort(a[0:len(a)/2]), mergeSort(a[len(a)/2:]))

if __name__=='__main__':
	n = int(sys.stdin.readline())
	parts = sys.stdin.readline().split(" ")
	nums = [0 for x in range(n)]
	for index in range(n):
		nums[index] = int(parts[index])
	ans = mergeSort(nums)
	for num in ans:
		print num,
