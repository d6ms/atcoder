from time import perf_counter
t0 = perf_counter()


import sys
sys.setrecursionlimit(300000)
from collections import defaultdict
from random import randint

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def MI0(): return map(lambda s: int(s) - 1, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
def LMI0(): return list(map(lambda s: int(s) - 1, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


D = I()
C = LMI()
S = [LMI() for _ in range(D)]


# 初期解の生成
last = defaultdict(int)
ans0 = []
for d in range(D):
    m = -INF
    ans = -1
    for i in range(26):
        lans = S[d][i]
        for j in range(26):
            if i == j:
                lans -= C[j] * (d + 1 - d - 1)
            else:
                lans -= C[j] * (d + 1 - last[j])
        if lans > m:
            m = lans
            ans = i
    ans0.append(ans)


T = ans0
last = [[i + 1] * 26 for i in range(D)]
for d in range(D):
    i = T[d]
    j = 0
    for dd in range(d, D):
        last[dd][i] = j
        j += 1

def eval(d, q):
    i = T[d]
    val = S[d][q] - S[d][i]

    contrib = 0
    if d == 0:
        j = 1
    else:
        j = last[d - 1][i] + 1
    for dd in range(d, D):
        if dd > d and last[dd][i] == 0:
            break
        contrib += j - last[dd][i]
        j += 1
    val -= contrib * C[i]

    contrib = 0
    j = 0
    for dd in range(d, D):
        if last[dd][q] == 0:
            break
        contrib += last[dd][q] - j
        j += 1
    val += contrib * C[q]

    return val

def apply(d, q):
    i = T[d]

    if d == 0:
        j = 1
    else:
        j = last[d - 1][i] + 1
    for dd in range(d, D):
        if dd > d and last[dd][i] == 0:
            break
        last[dd][i] = j
        j += 1

    j = 0
    for dd in range(d, D):
        if last[dd][q] == 0:
            break
        last[dd][q] = j
        j += 1

    T[d] = q


# TLまで焼きなましで1点更新
i = 0
while perf_counter() - t0 < 1.8:
    d = randint(0, D - 1)
    q = randint(0, 25)
    if eval(d, q) > 0:
        apply(d, q)
    else:
        if randint(0, (i + 1) ** 2) == 0:
            apply(d, q)
    i += 1

for t in T:
    print(t + 1)