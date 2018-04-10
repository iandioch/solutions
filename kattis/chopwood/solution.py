import heapq

n = int(input())
nums = list(map(lambda x: int(x)-1, (input() for _ in range(n))))

if nums[-1] != n:
    # invalid input
    print('Error')
else:
    req = [0 for _ in range(n+1)]
    for num in nums:
        req[num] += 1

    q = []
    for i in range(n):
        if req[i] == 0:
            heapq.heappush(q, i)
    if not len(q):
        print('Error')
    else:
        for i in range(n):
            num = heapq.heappop(q)
            print(num+1)
            req[nums[i]] -= 1
            if req[nums[i]] == 0:
                heapq.heappush(q, nums[i])
