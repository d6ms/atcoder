from functools import reduce
from operator import mul


def cmb(n, r):
    r = min(n - r, r)
    if r == 0:
        return 1
    elif n < r:
        return 0
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def factorize(n):
    """
    nの値を素因数分解し、素因数とその指数をtupleにまとめたリストを返す
    e.g.
    >>> factorize(20)
    [(2, 2), (5, 1)]
    """
    b = 2
    fct = []
    while b * b <= n:
        cnt = 0
        while n % b == 0:
            cnt += 1
            n //= b
        if cnt > 0:
            fct.append((b, cnt))
        b += 1
    if n > 1:
        fct.append((n, 1))
    return fct


MOD = 10 ** 9 + 7
N, M = map(int, input().split())

# M = 2^9 * 5^7 とすると
# 9個のボールとN-1個の仕切りを並べ替える場合の数　* 7個のボールとN-1個の仕切りを並べ替える場合の数
# = 9+N-1_C_9 * 7+N-1_C_7
# で考えられるはず

ans = 1
for fct, e in factorize(M):
    c = cmb(e + N - 1, e) % MOD
    ans = (ans * c) % MOD
print(ans)
