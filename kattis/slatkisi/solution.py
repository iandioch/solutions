value, zeroes = map(int, input().split())
value /= 10**zeroes
value = round(value, 0)
value *= 10**zeroes
print(int(value))
