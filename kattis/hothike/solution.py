n = int(input())
day = list(map(int, input().split()))
best = min((i for i in range(n-2)), key=lambda i: max(day[i], day[i+2]))
print(best+1, max(day[best], day[best+2]))
