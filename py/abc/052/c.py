from collections import defaultdict


def factorize2(n):
    """
    nの値を素因数分解し、素因数とその指数をtupleにまとめたリストを返す
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
N = int(input())
d = defaultdict(int)
for i in range(1, N + 1):
    for n, c in factorize2(i):
        d[n] += c

ans = 1
for n, c in d.items():
    ans *= c + 1
    ans %= MOD
print(ans)
