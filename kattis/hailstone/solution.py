def h(n):
    if n == 1:
        return 1
    if n % 2 == 0:
        return n + h(n//2)
    return n + h(3*n + 1)

print(h(int(input())))
