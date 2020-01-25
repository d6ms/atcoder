def factorize(n):
    """
    nの値を素因数分解し、素因数とその指数をtupleにまとめたリストを返す
    e.g.
    factorize(20)
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


N, P = map(int, input().split())
ans = 1
for p, e in factorize(P):
    if e >= N:
        ans *= p ** (e // N)
print(ans)
