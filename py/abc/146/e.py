from itertools import combinations

N, K = map(int, input().split())
A = list(map(int, input().split()))


def to_cumsum(arr):
    """
    1次元配列を累積和の1次元配列に変換する
    """
    cumsum = 0
    new = [0] * (len(arr) + 1)
    for i, e in enumerate(arr):
        cumsum += e
        new[i + 1] = cumsum
    return new

ans = 0
cumsum = to_cumsum(A)
for l, r in combinations(range(N + 1), 2):
    if (cumsum[r] - cumsum[l]) % K == 0:
        ans += 1
print(ans)