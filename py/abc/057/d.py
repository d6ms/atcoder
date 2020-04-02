# WA

import sys
sys.setrecursionlimit(300000)

def I(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LMI(): return list(map(int, sys.stdin.readline().split()))
MOD = 10 ** 9 + 7
INF = float('inf')


def create_factorial(n):
    """
    階乗を事前計算した配列を作成します。
    :param n: [0, n]の配列を作成します
    """
    f = list()
    for i in range(n + 1):
        if i in [0, 1]:
            f.append(1)
        else:
            f.append(f[i - 1] * i)
    return f

N, A, B = MI()
V = sorted(LMI(), reverse=True)

# s = [(v0, n), (v1, m), (v2, l)...]
s = []
cur = V[0]
cnt = 0
for v in V:
    if v != cur:
        s.append((cur, cnt))
        cur = v
        cnt = 1
    else:
        cnt += 1
s.append((cur, cnt))


f = create_factorial(51)

def comb(n, r):
    return f[n] // f[n - r] * f[r]

a = list()
for i in range(A, B + 1):
    selected = 0
    sval = 0
    for v, n in s:
        if selected + n < i:
            selected += n
            sval += v * n
        else:
            sval += v * (i - selected)
            val = sval / i
            c = comb(n, i - selected)
            a.append((val, c))
            break
a.sort(reverse=True)

ans = a[0][0]
cans = 0
for val, c in a:
    if val == ans:
        cans += c
print(ans)
print(cans)


