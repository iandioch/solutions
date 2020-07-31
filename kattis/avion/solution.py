import sys

def main():
    nums = [(i+1) for i,line in enumerate(sys.stdin.readlines()) if 'FBI' in line]
    if len(nums) == 0:
        print('HE GOT AWAY!')
    else:
        print(' '.join(str(n) for n in nums))

main()
