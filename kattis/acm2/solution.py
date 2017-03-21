num_probs, firstprob = map(int, input().split())
time = list(map(int, input().split()))

next_time = time[firstprob]
del time[firstprob]
time.sort(reverse=True)
time.append(next_time)

num_ac = 0
score = 0

i = -1

time_left = 300

while len(time) > 0:
    t = time.pop()
    time_left -= t
    if time_left >= 0:
        num_ac += 1
        score += 300-time_left

print(num_ac, score)
