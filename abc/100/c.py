def factorize2(n):
    """
    nの値を素因数分解し、素因数とその指数をtupleにまとめたリストを返す
    e.g.
    >>> factorize(20)
    [(2, 2), (5, 1)]
    """
    b = 2
    fct = []
    while b == 2:
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


N = int(input())
A = list(map(int, input().split()))

cnt = 0
for a in A:
    res = factorize2(a)
    if len(res) > 0:
        fct, num = res[0]
        if fct == 2:
            cnt += num
print(cnt)