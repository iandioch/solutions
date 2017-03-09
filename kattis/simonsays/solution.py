ORDER = 'Simon says'
n = int(input())
for t in range(n):
    line = input()
    if (line[:len(ORDER)] == ORDER):
        print(line[len(ORDER):])
