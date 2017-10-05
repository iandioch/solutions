num_tests = int(input())
for _ in range(num_tests):
    cities, pilots = map(int, input().split())
    print(cities-1)
    for _ in range(pilots):
        input()
