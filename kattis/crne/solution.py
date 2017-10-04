n = int(input())
p = n//2
q = p
if p+q < n:
    p += 1
print((p+1)*(q+1))
