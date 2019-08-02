# ACできてない

from bisect import bisect_right, bisect_left


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


N = int(input())
A = list(map(int, input().split()))

cumsum = to_cumsum(A)

ans = float('inf')
# 真ん中の切れ目をiで固定する
for i in range(2, N - 1):
    # [0, i-1]の範囲からP, Qの最適な切れ目を二分探索で求める
    mean = (cumsum[i - 1] + cumsum[0]) / 2
    idx1 = bisect_right(cumsum, mean) - 1
    idx2 = bisect_left(cumsum, mean) - 1
    P1, Q1 = cumsum[idx1], cumsum[i - 1] - cumsum[idx1]
    P2, Q2 = cumsum[idx2], cumsum[i - 1] - cumsum[idx2]

    # [i, N-1]の範囲からR, Sの最適な切れ目を二分探索で求める
    mean = (cumsum[N - 1] + cumsum[i]) / 2
    idx1 = bisect_right(cumsum, mean) - 1
    idx2 = bisect_left(cumsum, mean) - 1
    R1, S1 = cumsum[idx1] - cumsum[i], cumsum[N - 1] - cumsum[idx1]
    R2, S2 = cumsum[idx2] - cumsum[i], cumsum[N - 1] - cumsum[idx2]

    ans = min(ans, abs(max([P1, Q1, R1, S1]) - min([P1, Q1, R1, S1])))
    ans = min(ans, abs(max([P1, Q1, R2, S2]) - min([P1, Q1, R2, S2])))
    ans = min(ans, abs(max([P2, Q2, R1, S1]) - min([P2, Q2, R1, S1])))
    ans = min(ans, abs(max([P2, Q2, R2, S2]) - min([P2, Q2, R2, S2])))

print(ans)
