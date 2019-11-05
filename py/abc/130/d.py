from bisect import bisect_left


def to_cumsum(arr):
    """
    1次元配列を累積和の1次元配列に変換する
    """
    cumsum = 0
    new = list()
    for e in arr:
        cumsum += e
        new.append(cumsum)
    return new


N, K = map(int, input().split())
A = list(map(int, input().split()))

Asum = [0]
Asum.extend(to_cumsum(A))
ans = 0
for i in range(1, N + 1):
    idx = bisect_left(Asum, Asum[i - 1] + K)
    ans += N - idx + 1
print(ans)

