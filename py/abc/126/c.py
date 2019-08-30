def solve(N, K):
    p = 0
    for i in range(1, N + 1):
        prob = 1 / N
        point = i
        while point < K:
            point = point * 2
            prob = prob / 2
        p += prob
    return p


N, K = map(int, input().split())
print(solve(N, K))
