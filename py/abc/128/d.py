def solve(N, K, V):
    # 右からi個、左からj個取り出す時の価値の最大値
    max_points = 0
    for i in range(N + 1):
        for j in range(min(N + 1, K - i + 1)):
            j = min(N - i, j)
            hand = list()
            hand.extend(V[N - i:])
            hand.extend(V[:j])
            points = sum(hand)
            minus = list(filter(lambda x: x < 0, hand))
            minus = sorted(minus)
            action = K - i - j
            points += abs(sum(minus) - sum(minus[action:]))
            max_points = max(max_points, points)
    return max_points


N, K = map(int, input().split())
V = list(map(int, input().split()))
print(solve(N, K, V))
