X = int(input())


def primes():
    """
    素数のジェネレータ
    """
    d = {}
    q = 2
    while True:
        if q not in d:
            yield q
            d[q * q] = [q]
        else:
            for p in d[q]:
                d.setdefault(p + q, []).append(p)
            del d[q]
        q += 1


for p in primes():
    if p >= X:
        print(p)
        exit(0)
