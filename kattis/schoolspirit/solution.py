def score_without(scores, i, n):
    others = [scores[j] for j in range(n) if j != i]
    score = 0.2*sum(others[j]*(0.8**j) for j in range(len(others)))
    return score

def main():
    n = int(input())
    scores = [int(input()) for _ in range(n)]
    print(score_without(scores, -100, n))
    print(sum(score_without(scores, i, n) for i in range(n))/n)

main()
