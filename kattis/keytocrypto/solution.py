A = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cypher = input()
key = input()
ans = ''
for i in range(len(cypher)):
    c = A.find(cypher[i])
    k = A.find(key[i])
    j = c - k % len(A)
    ans += A[j]
    key += A[j]
print(ans)
