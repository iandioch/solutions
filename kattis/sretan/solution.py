# We must add 1 so that we get 0s handled properly.
n = int(input()) + 1 
# Take the binary repr and ignore the most significant bit
b = bin(n)[3:]
# Convert all zeroes to 4s and ones to 7s
print(''.join('47'[int(c)] for c in b))
