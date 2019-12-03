import sys

orig_arr = list(map(int, ''.join(sys.stdin.readlines()).split(',')))
for noun in range(100):
    for verb in range(100):
        arr = orig_arr[:]
        arr[1] = noun
        arr[2] = verb
        ptr = 0
        while True:
            if ptr >= len(arr):
                print('Pointer passed end of input')
                break
            if arr[ptr] == 1:
                if ptr + 3 >= len(arr):
                    print('Not enough space for addition')
                if arr[ptr+1] >= len(arr) or arr[ptr+2] >= len(arr) or arr[ptr+3] >= len(arr):
                    print('Addition params exceeded bounds')
                    break
                ans = arr[arr[ptr+1]] + arr[arr[ptr+2]]
                arr[arr[ptr+3]] = ans
                ptr += 4
            elif arr[ptr] == 2:
                if ptr + 3 >= len(arr):
                    print('Not enough space for multiplication')
                if arr[ptr+1] >= len(arr) or arr[ptr+2] >= len(arr) or arr[ptr+3] >= len(arr):
                    print('Multiplication params exceeded bounds')
                    break
                ans = arr[arr[ptr+1]] * arr[arr[ptr+2]]
                arr[arr[ptr+3]] = ans
                ptr += 4
            elif arr[ptr] == 99:
                #print(arr[0])
                if arr[0] == 19690720:
                    print('Answer found:')
                    print(100*noun + verb)
                break
            else:
                print('Unrecognised instruction:', arr[ptr])
                break
