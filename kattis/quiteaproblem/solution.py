import sys

lines = sys.stdin.readlines()
for line in lines:
    if 'problem' in line.lower():
        print('yes')
    else:
        print('no')
