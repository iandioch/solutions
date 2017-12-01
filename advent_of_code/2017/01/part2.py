s = input().strip()
n = [s[i] for i in range(len(s)-1, -1, -1) if s[i] == s[i-len(s)//2]]
print(sum(map(int, n)))
