from collections import defaultdict


def factorize2(n):
    """
    nの値を素因数分解し、素因数とその指数をtupleにまとめたリストを返す
    e.g.
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


# 75 = 5 * 5 * 3
# p^74 / p^24 * q^2 / p^14 * q^4 / p^4 * q^4 * r^2 の形しか七五数になりえない

N = int(input())
pf = defaultdict(int)
for i in range(1, N + 1):
    for p, n in factorize2(i):
        pf[p] += n

c74, c24, c14, c4, c2 = 0, 0, 0, 0, 0
for p, n in pf.items():
    if n >= 74:
        c74 += 1
    if n >= 24:
        c24 += 1
    if n >= 14:
        c14 += 1
    if n >= 4:
        c4 += 1
    if n >= 2:
        c2 += 1

ans = c74
ans += c24 * max(0, c2 - 1)
ans += c14 * max(0, c4 - 1)
ans += (c4 * max(0, c4 - 1) // 2) * max(0, c2 - 2)
print(ans)