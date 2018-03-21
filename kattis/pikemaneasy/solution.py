MOD = 1000000007

num_probs, total_length = map(int, input().split())
a, b, c, curr = map(int, input().split())

prob_times = [curr]
for _ in range(1, num_probs):
    curr = (((a*curr)+b)%c) + 1
    prob_times.append(curr)

prob_times.sort()

done_probs = 0
penalty = 0
passed_time = 0
while done_probs < num_probs:
    if passed_time + prob_times[done_probs] <= total_length:
        penalty = (penalty + prob_times[done_probs] + passed_time) % MOD
        passed_time += prob_times[done_probs]
        done_probs += 1
    else:
        break
print(done_probs, penalty)
