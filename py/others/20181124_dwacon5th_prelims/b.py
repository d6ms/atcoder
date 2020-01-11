def to_cumsum(arr):
    """
    1次元配列を累積和の1次元配列に変換する
    """
    cumsum = 0
    new = [0] * len(arr)
    for i, e in enumerate(arr):
        cumsum += e
        new[i] = cumsum
    return new


N, K = map(int, input().split())
tmp = list(map(int, input().split()))
A = [0]
A.extend(tmp)
cumsum = to_cumsum(A)
arr = list()
for i in range(N + 1):
    for j in range(i + 1, N + 1):
        arr.append(cumsum[j] - cumsum[i])

ans_str = ''
for i in reversed(range(1, cumsum[-1].bit_length() + 1)):
    tmp = list(filter(lambda a: (a >> (i - 1)) & 1, arr))
    cnt = len(tmp)
    if cnt >= K:
        ans_str += '1'
        arr = tmp
    else:
        ans_str += '0'
print(int(ans_str, 2))
