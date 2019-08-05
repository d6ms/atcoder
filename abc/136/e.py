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


N, K = map(int, input().split())
A = list(map(int, input().split()))

d = divisors(sum(A))
d.sort(reverse=True)
