n = int(input())
probabilities = [float(input().split()[1]) for _ in range(n)]
probabilities = sorted(probabilities, reverse=True)
ans = 0
for i in range(1, len(probabilities)+1):
    ans += i*probabilities[i-1]
print(ans)
