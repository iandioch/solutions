import sys

ans = 0
for line in sys.stdin.readlines():
    policy, pw = line.split(':')
    freq, letter = policy.split(' ')
    minf, maxf = map(int, freq.split('-'))
    letter_count = pw.count(letter)
    if letter_count >= minf and letter_count <= maxf:
        ans += 1

print(ans)
