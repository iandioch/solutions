def main():
    from sys import stdin, stdout
    write = stdout.write
    for x in stdin.readlines()[:0:-1]:
        write(x)

main()
