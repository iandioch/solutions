import sys

arr = list(map(int, ''.join(sys.stdin.readlines()).split(',')))
arr[1] = 12
arr[2] = 2
ptr = 0
while True:
    if ptr >= len(arr):
        print('Pointer passed end of input')
        break
    if arr[ptr] == 1:
        ans = arr[arr[ptr+1]] + arr[arr[ptr+2]]
        arr[arr[ptr+3]] = ans
        ptr += 4
    elif arr[ptr] == 2:
        ans = arr[arr[ptr+1]] * arr[arr[ptr+2]]
        arr[arr[ptr+3]] = ans
        ptr += 4
    elif arr[ptr] == 99:
        print(arr[0])
        break
    else:
        print('Unrecognised instruction:', arr[ptr])
        break
