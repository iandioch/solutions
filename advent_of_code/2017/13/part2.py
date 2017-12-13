import sys

def height_at_time(height, time):
    period = (height*2 - 2)
    left = time % period
    if left >= height:
        left = height*2 - 2 - left
    return left

d = {}
for line in sys.stdin.readlines():
    p = line.split(':')
    d[int(p[0])] = int(p[1])

delay = 0
end = max(d.keys()) + 1
while True:
    caught = False

    for curr in range(end):
        if curr in d:
            p = height_at_time(d[curr], delay+curr)
            if p == 0:
                caught = True
                break
    if not caught:
        print(delay)
        break
    delay += 1
