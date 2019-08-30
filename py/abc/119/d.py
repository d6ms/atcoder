# リスト内を二分探索するならbisectが使える
import bisect


def nearest_pair(lst, x):
    left = None
    right = None
    idx = bisect.bisect_left(lst, x)
    if idx != 0:
        left = lst[idx - 1]
    if idx != len(lst):
        right = lst[idx]
    return left, right


def distance(l, r, x):
    if l is None:
        return abs(r - x)
    elif r is None:
        return abs(l - x)
    else:
        return min(abs(r - x), abs(l - x))


A, B, Q = map(int, input().split())
S = [int(input()) for _ in range(A)]
T = [int(input()) for _ in range(B)]
Q = [int(input()) for _ in range(Q)]

for x in Q:
    s_l, s_r = nearest_pair(S, x)
    t_l, t_r = nearest_pair(T, x)

    result1 = float('inf')
    if s_l is not None:
        result1 = abs(x - s_l)
        l, r = nearest_pair(T, s_l)
        result1 += distance(l, r, s_l)

    result2 = float('inf')
    if s_r is not None:
        result2 = abs(x - s_r)
        l, r = nearest_pair(T, s_r)
        result2 += distance(l, r, s_r)

    result3 = float('inf')
    if t_l is not None:
        result3 = abs(x - t_l)
        l, r = nearest_pair(S, t_l)
        result3 += distance(l, r, t_l)

    result4 = float('inf')
    if t_r is not None:
        result4 = abs(x - t_r)
        l, r = nearest_pair(S, t_r)
        result4 += distance(l, r, t_r)

    print(min(result1, result2, result3, result4))
