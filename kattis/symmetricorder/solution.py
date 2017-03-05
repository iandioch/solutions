c = 1
while True:
    n = int(input())
    if n == 0:
        break
    w = [input() for _ in range(n)]
    print ("SET", c)
    for i in range(0, n, 2):
        print(w[i])
    for i in range(n-(n%2)-1, -1, -2):
        print(w[i])
    c += 1
