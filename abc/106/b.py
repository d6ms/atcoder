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

cnt = 0
for i in range(1, N + 1, 2):
    if len(divisors(i)) == 8:
        cnt += 1

print(cnt)
