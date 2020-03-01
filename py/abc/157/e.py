from collections import defaultdict
from bisect import bisect_left, bisect_right


def I(): return int(input())


def MI(): return map(int, input().split())


def LMI(): return list(map(int, input().split()))


N = I()
S = input()
Q = I()

d = defaultdict(list)
for i, c in enumerate(S):
    d[c].append(i)


def bi(a, x):
    lo = 0
    hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


changed = dict()
for _ in range(Q):
    t, i, c = input().split()
    if t == '1':
        i = int(i) - 1
        changed[i] = c
    else:
        l, r = int(i) - 1, int(c) - 1
        ch = set()
        for c, appear in d.items():
            idx = bisect_left(appear, l)
            if idx < len(appear) and appear[idx] <= r:
                ch.add(c)
        print(cnt)
