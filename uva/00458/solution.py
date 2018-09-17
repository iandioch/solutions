import sys

def main():
    for line in sys.stdin:
        print(''.join(chr(ord(c)-7) for c in line.strip()))

if __name__ == '__main__':
    main()
