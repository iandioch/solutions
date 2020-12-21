def main():
    word = set(input())
    alph = input()

    n = 0
    for c in alph:
        if c in word:
            word.remove(c)
            if len(word) == 0:
                print('WIN')
                return
        else:
            n += 1
            if n >= 10:
                print('LOSE')
                return

main()
