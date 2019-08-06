from collections import deque

def main():

    HOUR = 60*60

    num_test = int(input())
    for _ in range(num_test):
        num_buttons, des_time = map(int, input().split())
        buttons = list(map(int, input().split()))


        q = deque()
        # time, num_steps
        q.appendleft((0, 0))
        best_time = HOUR + 1
        besti = -1

        memo = [-1 for i in range(HOUR+1)]
        while len(q):
            time, num_steps = q.popleft()
            if memo[time] > 0 and memo[time] <= num_steps:
                continue
            memo[time] = num_steps

            if time >= des_time and time < best_time:
                best_time = time
                besti = num_steps
            for b in buttons:
                ntime = time + b
                ntime = max(0, ntime)
                ntime = min(HOUR, ntime)
                q.append((ntime, num_steps+1))
        print(besti, best_time - des_time)


main()
