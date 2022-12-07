import sys
import collections

def findind(line, windowsize = 14):
    def all_unique(d):
        return len(set(d)) == len(d)

    window = collections.deque()
    for i in range(len(line)):
        if len(window) < windowsize:
            window.append(line[i])
            continue

        if all_unique(window):
            return i

        window.popleft()
        window.append(line[i])

def main():
    for line in sys.stdin.readlines():
        line = line.strip()
        print(findind(line))

main()
