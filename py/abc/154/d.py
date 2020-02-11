def I(): return int(input())
def MI(): return map(int, input().split())
def LMI(): return list(map(int, input().split()))
def to_cumsum(arr, pad=True):
    """
    1次元配列を累積和の1次元配列に変換する
    pad: 先頭に0の項を作る場合はTrue
    """
    cumsum = 0
    padding = 1 if pad else 0
    new = [0] * (len(arr) + padding)
    for i, e in enumerate(arr):
        cumsum += e
        new[i + padding] = cumsum
    return new


N, K = MI()
P = LMI()
cum = to_cumsum(P, pad=True)

t = 0
for i in range(N - K + 1):
    m = cum[i + K] - cum[i]
    t = max(t, m)
print((t + K) / 2)