import sys
from itertools import accumulate, combinations

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


H, W, K = MI()
S = [[int(x) for x in list(input())] for _ in range(H)]


def fn(hdivs):
    hdivs = list(hdivs)
    hdivs.append(H)
    slice = 0

    cnt = [0] * len(hdivs)
    for j in range(W):
        col_cnts = [0] * len(hdivs)
        for h, hdiv in enumerate(hdivs):
            lower = hdivs[h - 1] if h > 0 else 0
            upper = hdiv
            col_cnt = sum(row[j] for row in S[lower:upper])
            if col_cnt > K:
                return -1
            col_cnts[h] = col_cnt
        if not all(cnt[h] + col_cnts[h] <= K for h in range(len(hdivs))):
            slice += 1
            cnt = col_cnts
        else:
            for h in range(len(hdivs)):
                cnt[h] += col_cnts[h]
    return slice

ans = fn(tuple())
for d in range(1, H):
    for hdivs in combinations(range(1, H), d):
        min_slice = fn(hdivs)
        if min_slice > -1:
            ans = min(ans, (len(hdivs)) + min_slice)
print(ans)