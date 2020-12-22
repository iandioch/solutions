def main():
    s = input()
    score = {'A': 0, 'B': 0}
    for i in range(0, len(s), 2):
        score[s[i]] += int(s[i+1])
    print(max(score, key=lambda x:score[x]))


main()
