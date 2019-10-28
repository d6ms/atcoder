def divisors(n, sort=False):
    """
    nの約数をO(√n)で列挙する
    """
    d = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            d.append(i)
            if i != n // i:
                d.append(n//i)
    if sort:
        d.sort()
    return d


N = int(input())

ans = float('inf')
d = divisors(N, sort=True)
for i in range(len(d)):
    x, y = d[i], d[-i - 1]
    dist = abs(x - 1) + abs(y - 1)
    ans = min(ans, dist)
print(ans)
