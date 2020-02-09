def to_cumsum(arr, pad=True):
    """
    1次元配列を累積和の1次元配列に変換する
    pad: 先頭に0の項を作る場合はTrue
    """
    cumsum = 0
    new = [0] * (len(arr) + (1 if pad else 0))
    for i, e in enumerate(arr):
        cumsum += e
        new[i + (1 if pad else 0)] = cumsum
    return new


N, Q = map(int, input().split())
memo = [0] * N
# いもす法で区間に対する和を計算する
# [l, r]にkを足す = memo[l]にkを足し、memo[r + 1]からkを引く、最後に累積和
for _ in range(Q):
    l, r = map(lambda x: int(x) - 1, input().split())
    memo[l] += 1
    if r + 1 < N:
        memo[r + 1] -= 1

ans = ['0' if x % 2 == 0 else '1' for x in to_cumsum(memo, pad=False)]
print(''.join(ans))
