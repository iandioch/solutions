num_tests = int(input())
for _ in range(num_tests):
    num_secs = int(input())
    finishes_at = {1:[]}
    ends = set()
    bads = set()
    p = {}
    for _ in range(num_secs):
        parts = input().split()
        n = int(parts[0])
        if parts[1][0] == 'f':
            ends.add(n)
            p[n] = []
        elif parts[1][0] == 'c':
            bads.add(n)
            p[n] = []
        else:
            p[n] = map(int, parts[1:])

    mem = {}
    def search(index):
        if index in mem:
            return mem[index]
        if index in ends:
            return 1
        ans = 0
        for q in p[index]:
            ans += search(q)
        mem[index] = ans
        return ans

    print(search(1))
